import json


class Command():
    """"
    Command class
    will process the data sent between the devices
    """
    def __init__(self, command=None):
        if command is not None:
            if type(command) is not dict:
                self._command_dict = json.loads(command)
                self._command_string = command
            else:
                self._command_string = json.dumps(command)
                self._command_dict = command
            self._command = self._command_dict['command']
        else:
            self._command_dict = None
            self._command_string = None
            self._command = None

    @property
    def command_dict(self):
        return self._command_dict

    @property
    def command(self):
        return self._command

    @property
    def command_string(self):
        return self._command_string

    def process(self):
        """
        process method for processing received commands,
        for use as Game class methods argument (test_command.py for more info)
        """
        if self._command == 'init':  # zwraca wszystkie dane potrzebne do inicjalizacji gry
            template = self._command_dict["template"]
            resource_amt = self._command_dict["resource_amount"]
            resources = self._command_dict["resources"]
            players = self._command_dict["players"]
            dice = self._command_dict["dice"]
            dice_amount = self._command_dict["dice_amount"]
            return template, resource_amt, resources, players, dice, dice_amount

        elif self._command == 'load':
            template = self._command_dict["template"]
            resource_amt = self._command_dict["resource_amount"]
            resources = self._command_dict["resources"]
            players_data = self._command_dict['players']
            players = [player['name'] for player in players_data]
            dice = self._command_dict["dice"]
            dice_amount = self._command_dict["dice_amount"]
            return template, resource_amt, resources, players, dice, dice_amount, players_data

        elif self._command == 'read':  # sending a readrespond will be expected after receiving this
            player = self._command_dict["player"]
            resource = self._command_dict["resource"]
            return player, resource

        elif self._command == 'add' or self._command == "write":
            player = self._command_dict["player"]
            resource = self._command_dict["resource"]
            amount = self._command_dict["amount"]
            return player, resource, amount

        elif self._command == 'readrespond':  # Response to a read command
            resource = self._command_dict["resource"]
            player = self._command_dict["player"]
            amount = self._command_dict['amount']
            return player, resource, amount

        elif self._command == 'diceresult':
            results = self._command_dict['results']
            return results

    def send_read(self, player, resource):
        """
        Send a read command.
        """
        command = {}
        command['command'] = 'read'
        command['player'] = player
        command['resource'] = resource
        self._command = 'read'
        self._command_dict = command
        self._command_string = json.dumps(self._command_dict)
        return self._command_string

    def assemble_manipulate_resources(self, command, player, resource, amount):
        """
        Assembles a command containing 'command' 'player' 'resource' and 'amount' values
        currently used by write, add, readrespond
        """
        command['player'] = player
        command['resource'] = resource
        command['amount'] = amount
        self._command_dict = command
        self._command_string = json.dumps(self._command_dict)
        return self._command_string

    def send_write(self, player, resource, amount):
        command = {}
        command['command'] = 'write'
        self._command = 'write'
        self.assemble_manipulate_resources(command, player, resource, amount)
        return self._command_string

    def send_add(self, player, resource, amount):
        command = {}
        command['command'] = 'add'
        self._command = 'add'
        self.assemble_manipulate_resources(command, player, resource, amount)
        return self._command_string

    def send_readrespond(self, player, resource, amount):
        command = {}
        command['command'] = 'readrespond'
        self._command = 'readrespond'
        self.assemble_manipulate_resources(command, player, resource, amount)
        return self._command_string

    def send_diceresult(self, results):
        command = {}
        command['command'] = 'diceresult'
        self._command = 'diceresult'
        command['results'] = results
        self._command_dict = command
        self._command_string = json.dumps(command)
        return self._command_string

    def send_endturn(self):
        command = {}
        command['command'] = 'endturn'
        self._command = 'endturn'
        self._command_dict = command
        self._command_string = json.dumps(command)
        return self._command_string