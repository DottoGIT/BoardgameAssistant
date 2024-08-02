from command import Command
from game import Game
from Player import Player
from saving import read_templates, read_games, read_game_data
from saving import save_templates, save_gamestate
import socket


class ApplicationManager():
    """
    Klasa która ma zarządzać całą logiką urządzenia,
    posiadać funkcje potrzebne do jego działania
    oraz zarządzać innymi klasami składowymi
    Posiada także główną pętle do komunikacji z urządzeniem
    """
    def __init__(self, app_window):
        # Listy zapisanych w systemie szablonów i gier
        self.saved_tamplates = self._load_templates()
        self.saved_games = self._load_games()
        # Zmienne do konfiguracji ustroja
        self.device_ip = None
        self.device_port = None
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._connected = False
        self._socket.setblocking(False)
        # Aktualna rozgrywka
        self.current_game = None
        self.value_changed = False

    def init_app_window(self, app_window):
        """Pozawa na komunikacje z oknem aplikacji ale nie jest obowiązkowe"""
        self.app_window = app_window

    def _load_templates(self):
        """ Ta funkcja ma zwracać liste templatów zapisanych na dysku w postaci listy klas Template() """
        return read_templates()

    def _load_games(self):
        """ Ta funkcja ma zwracać liste zapisanych gier w postacie klas Game() """
        return read_games()

    def start_new_game(self, player_names, template_name):
        """ Tworzy nową rozgrywkę i przypisuje ją do zmiennej current_game """
        template = self.find_template(template_name)
        resources_command = {}
        for resource in template.resources:
            resources_command[resource.name] = (resource.min_value, resource.max_value, resource.start_value)
        init = Command()
        command_string = init.send_init(template_name, template.resource_amount, resources_command, player_names, template.dice.walls, template.dice.throws)
        print(command_string)
        self._socket.send(bytes(command_string, 'utf-8'))
        players = self.create_players_from_names(player_names)
        game = Game(players, template)
        self.current_game = game
        self.saved_games.append(game)
        self.save_game()

    def create_players_from_names(self, names):
        """ dla każdej nazwy tworzy nowego gracza o podanej nazwie """
        players = []
        for name in names:
            players.append(Player(name))
        return players

    def update(self):
        """ Ta funkcja wykonuje sie co milisektundę w Application manager i nasłuchuje akcje ustroja"""
        if self._connected:
            data = None
            try:
                data = self._socket.recv(2048)
            except socket.error:
                pass
            if data:
                cmd = Command(data)
                if cmd.command == 'add':
                    print('add received')
                    player, resource, amount = cmd.process()
                    self.value_changed = True
                    if amount:
                        self.current_game.create_new_log(f'{resource} gracza {player} {"+" if amount > 0 else ""}{amount}')
                        self.current_game.get_player(player).add_resource(resource, amount)
                elif cmd.command == 'write':
                    print('write received')
                    pass
                elif cmd.command == 'diceresult':
                    print('diceresult received')
                    results = cmd.command_dict['results']
                    self.current_game.create_new_log(f'wyrzuca: {results}, czyli {sum(results)}')
                    self.value_changed = True
                    pass
                elif cmd.command == 'endturn':
                    print('endturn received')
                    self.current_game.end_turn()
                    if self.app_window is not None:
                        self.app_window.currently_shown_player_stats = self.current_game.current_player_index
                    self.value_changed = True

    def connect_to_device(self, ip: str, port: int):
        self._socket.setblocking(True)
        self._socket.settimeout(8)
        try:
            self._socket.connect((str(ip), int(port)))
            self._connected = True
        except socket.error as e:
            print(f'connection failed: {e}')
            self._connected = False

        self._socket.setblocking(False)

    def send_command(self, command):
        """ Wysyła do ustroja polecenie """
        if self._connected:
            self._socket.send(bytes(command, 'utf-8'))  # To bedzie trzeba przetestowac
        else:
            print("Connection has not been established yet")

    def add_template(self, temp):
        self.saved_tamplates.append(temp)
        save_templates(self.saved_tamplates)

    def delete_template(self, name):
        if not self.check_if_template_exists(name):
            raise ValueError("Cant delete non-existing template")
        # Create new list without template with given name
        self.saved_tamplates = [temp for temp in self.saved_tamplates if temp.name != name]
        save_templates(self.saved_tamplates)

    def check_if_template_exists(self, name):
        return len(self.saved_tamplates) != len([temp for temp in self.saved_tamplates if temp.name != name])

    def find_template(self, name):
        """ Zwraca szablon po nazwie """
        temp = [temp for temp in self.saved_tamplates if temp.name == name]
        if not temp:
            raise ValueError("Nie można zwrócić nieistniejącego szablonu")
        return temp[0]

    def load_game(self, date):
        game = [save for save in self.saved_games if save.date == date]
        all_game_data = read_game_data()
        game_data = [data for data in all_game_data if data['date'] == date][0]
        template = game_data['template']['name']
        resource_amount = len(game_data['template']['resources'])
        resources = {}
        for resource in game_data['template']['resources']:
            resources[resource['name']] = (resource['min_value'], resource['max_value'], resource['start_value'])
        players = game_data['players']
        dice = game_data['template']['dice']['walls']
        dice_amount = game_data['template']['dice']['throws']
        cmd = Command()
        cmd_string = cmd.send_load(template, resource_amount, resources, players, dice, dice_amount)
        print(cmd_string)
        self.send_command(cmd_string)
        self.current_game = game[0]

    def delete_game(self, date):
        self.saved_games = [save for save in self.saved_games if save.date != date]
        self.save_game()

    def save_game(self):
        save_gamestate(self.saved_games)
