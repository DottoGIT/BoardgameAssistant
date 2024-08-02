import json
from Dice import Dice
from Resource import Resource
from Template import Template
from Player import Player
from game import Game


def temp_to_dict(temp):
    """Zamiana Template w slownik do json"""
    data = {
        'name': temp.name,
        'resources': [res.__dict__ for res in temp.resources],
        'dice': temp.dice.__dict__ if temp.dice else None
    }
    return data


def save_templates(templates):
    """Usuniecie Template z pliku"""
    data = [temp_to_dict(temp) for temp in templates]
    with open('Aplikacja/templates.json', 'w') as fh:
        json.dump(data, fh, indent=2)


def build_resource(res):
    """Tworzenie Resource z danych json"""
    name = res['name']
    start_value = res['start_value']
    min_value = res['min_value']
    max_value = res['max_value']
    value = res['value']
    resource = Resource(name, start_value, min_value, max_value, value)
    return resource


def build_template(temp_data):
    """Tworzenie Template z danych json"""
    temp_name = temp_data['name']
    temp_dice_data = temp_data['dice']
    if temp_dice_data:
        throws = temp_dice_data['throws']
        walls = temp_dice_data['walls']
        temp_dice = Dice(walls, throws)
    else:
        temp_dice = None
    temp_res_data = temp_data['resources']
    temp_resources = []
    for res in temp_res_data:
        resource = build_resource(res)
        temp_resources.append(resource)
    return Template(temp_name, temp_resources, temp_dice)


def read_templates():
    """Odczytywanie istniejacych templatow"""
    with open('Aplikacja/templates.json') as file_handle:
        try:
            data = json.load(file_handle)
        except Exception:
            data = []
        templates = [build_template(temp_data) for temp_data in data]
    return templates


def game_to_dict(game):
    """Zamiana Game w slownik do json"""
    temp = temp_to_dict(game.template)
    players = []
    for player in game.players:
        player_data = {
            'name': player.name,
            'resources': [res.__dict__ for res in player.resources]
        }
        players.append(player_data)
    game_data = {
        'date': game.date,
        'template': temp,
        'players': players,
        'command_log': game.command_log
    }
    return game_data

def read_game_data():
    with open('Aplikacja/games.json') as fp:
        data = json.load(fp)
    return data


def read_games():
    """Odczytanie zapisanych gier z pliku"""
    games = []
    with open('Aplikacja/games.json') as fh:
        data = json.load(fh)
        for game_data in data:
            game_date = game_data['date']
            game_template = build_template(game_data['template'])
            players_data = game_data['players']
            command_log = game_data['command_log']
            players = []
            for player_data in players_data:
                name = player_data['name']
                resource_data = player_data['resources']
                resources = [build_resource(res) for res in resource_data]
                player = Player(name, resources)
                players.append(player)
            game = Game(players, game_template, command_log, True, game_date)
            games.append(game)
    return games


def save_gamestate(games):
    """Zapisanie stanu gry"""
    data = [game_to_dict(game) for game in games]
    with open('Aplikacja/games.json', 'w') as fh:
        json.dump(data, fh, indent=2)
