from command import Command
from game import Game
import json

# Przykładowe testy do inicjalizacji gry i odczytywania i dodawania informacji


def test_command_json():

    #  Format komendy do inicjalizacji gry
    dict = {
        "command": "init",
        "template": "template",
        "resource_amount": 2,
        "resources": {
            "drewno": (1, 10, 2),
            "kamien": (1, 10, 2),
        },
        "players": [
            "Damian",
            "Maciej",
        ],
        "dice": 6,
        "dice_amount": 2
    }
    command = Command(json.dumps(dict))
    assert command.command_dict["command"] == "init"
    assert command.command_dict["resources"]["kamien"][1] == 10


def test_init_game():
    dict = {
        "command": "init",
        "template": "template",
        "resource_amount": 2,
        "resources": {
            "drewno": (1, 10, 2),
            "kamien": (1, 10, 2),
        },
        "players": [
            "Damian",
            "Maciej",
        ],
        "dice": 6,
        "dice_amount": 2
    }
    cmd = Command(json.dumps(dict))
    game = Game(*cmd.process())  # cmd.process() zwróci argumenty do inicjalizacji gry
    game.define_players()
    assert game.template == "template"
    assert game.dice_amount == 2
    assert len(game.players) == 2


def test_read_resource_amount():
    dict = {
        "command": "init",
        "template": "template",
        "resource_amount": 2,
        "resources": {
            "drewno": (1, 10, 2),
            "kamien": (1, 10, 2),
        },
        "players": [
            "Damian",
            "Maciej",
        ],
        "dice": 6,
        "dice_amount": 2
    }
    cmd = Command(json.dumps(dict))
    game = Game(*cmd.process())
    game.define_players()
    dict = {
        "command": "read",
        "player": "Damian",
        "resource": "drewno"
    }

    cmd = Command(json.dumps(dict))
    assert game.read_resource(*cmd.process()) == 2


def test_add_resource():
    """
    tests the add command
    """
    dict = {
        "command": "init",
        "template": "template",
        "resource_amount": 2,
        "resources": {"drewno": (1, 10, 2), "kamien": (1, 10, 2)},
        "players": ["Damian", "Maciej"],
        "dice": 6,
        "dice_amount": 2
    }

    cmd = Command(json.dumps(dict))
    game = Game(*cmd.process())
    game.define_players()
    dict = {
        "command": "write",
        "player": "Damian",
        "resource": "drewno",
        "amount": 5
    }

    cmd = Command(json.dumps(dict))
    game.add_resource(*cmd.process())
    assert game.read_resource("Damian", "drewno") == 7


def test_add_over_max():
    dict = {
        "command": "init",
        "template": "template",
        "resource_amount": 2,
        "resources": {"drewno": (1, 10, 2), "kamien": (1, 10, 2)},
        "players": ["Damian", "Maciej"],
        "dice": 6,
        "dice_amount": 2
    }

    cmd = Command(json.dumps(dict))
    game = Game(*cmd.process())
    game.define_players()
    dict = {
        "command": "add",
        "player": "Damian",
        "resource": "drewno",
        "amount": 10
    }

    cmd = Command(json.dumps(dict))
    game.add_resource(*cmd.process())
    assert game.read_resource("Damian", "drewno") == 10


def test_write():
    """
    tests the write command
    """
    dict = {
        "command": "init",
        "template": "template",
        "resource_amount": 2,
        "resources": {"drewno": (1, 10, 2), "kamien": (1, 10, 2)},
        "players": ["Damian", "Maciej"],
        "dice": 6,
        "dice_amount": 2
    }

    cmd = Command(json.dumps(dict))
    game = Game(*cmd.process())
    game.define_players()
    dict = {
        "command": "write",
        "player": "Damian",
        "resource": "drewno",
        "amount": 5
    }

    cmd = Command(json.dumps(dict))
    game.set_resource(*cmd.process())
    assert game.read_resource("Damian", "drewno") == 5

    dict = {
        "command": "write",
        "player": "Damian",
        "resource": "drewno",
        "amount": 15
    }

    cmd = Command(json.dumps(dict))
    game.set_resource(*cmd.process())
    assert game.read_resource("Damian", "drewno") == 10


def test_send_read():
    cmd = Command()
    result = cmd.send_read("Damian", "kamien")
    dict = {
        "command": "read",
        "player": "Damian",
        "resource": "kamien"
    }

    assert result == json.dumps(dict)
