from Resource import Resource
from Player import Player
from random import choice  # from random import choices


class Game:
    """
    Main class of the game.
    will initialize a game if a proper command is given from a remote host.
    """
    def __init__(self, template, resource_amount: int, resources: dict, players: list, dice: int, dice_amount: int, player_data = None):
        self._template = template  # Template name
        self._resource_amount = resource_amount  # Amount of resources (nie wiem czy sie przyda ale jest)
        self._resources_raw = resources if resources else {}  # Dict with resource definition instructions
        self._players_raw = players if players else []  # Dict with player definition istructions
        self._dice = dice  # Dice type
        self._dice_amount = dice_amount  # Dice amount
        self._players = {}
        self._last_throws = None
        self._player_data = player_data

    @property
    def template(self):
        return self._template

    @property
    def resource_amount(self):
        return self._template

    @property
    def players(self):
        return self._players

    @property
    def dice(self):
        return self._dice

    @property
    def dice_amount(self):
        return self._dice_amount

    @property
    def last_throws(self):
        return self._last_throws

    def player(self, player: str):
        return self._players[player]

    def define_resources(self):
        resources = {}
        for resource in self._resources_raw:
            min_value = self._resources_raw[resource][0]
            max_value = self._resources_raw[resource][1]
            default_value = self._resources_raw[resource][2]
            resources[resource] = (Resource(resource, default_value, min_value, max_value))
        return resources

    def define_players(self):
        self._players = {}
        for player in self._players_raw:
            resources = self.define_resources()
            self._players[player] = Player(player, resources)

    def read_resource(self, player, resource):
        resource_object = self._players[player].get_resource(resource)
        return resource_object.get_value()

    def add_resource(self, player, resource, amount):
        self._players[player].add_resource(resource, amount)

    def set_resource(self, player, resource, amount):
        self._players[player].set_resource(resource, amount)

    def throw_dice(self):
        results = [choice(range(1, self._dice + 1)) for n in range(self._dice_amount)] # w esp32 nie ma choices()
        self._last_throws = results

    def load_data(self):
        for player in self._players:
            data = [name for name in self._player_data if name['name'] == player][0]
            for resource in data['resources']:
                self.set_resource(data['name'], resource['name'], resource['value'])
