from Player import Player
from datetime import datetime
from random import randint


class Game():
    """
    Ta klasa posiada liste aktualnych graczy, command_log oraz aktualny template rozgrywki
    ApplicationManager oraz ustroj bierze z niej zmienne do wyświetlania statystyk na ekranie
    Gier może być sporo (bo zapisane na dysku) ta klasa zawiera wszystkie niezbędne info żeby
    można było rozgrywkę śledzić i modyfikować

    zmienna is_loaded mówi czy gra została wczytana czy stworzona została nowa rozgrywka, wpływa to
    na inicjowanie niektórych zmiennych jak np surowce graczy
    """
    def __init__(self, players, template, command_log=[], is_loaded=False, date=None):
        if not players or not template:
            raise ValueError("Nie wszystkie dane zostały podane przy utworzeniu rozgrywki")

        self.template = template
        self.players = players if is_loaded else self.init_players(players)
        self.current_player_index = 0
        self.command_log = [] if not command_log else command_log

        if not date:
            date = datetime.now().strftime('%d-%m-%Y %H:%M:%S') + ' - ' + template.name
        self.date = date

    def init_players(self, players):
        """ Ta funkcja zwraca graczy z domyślnymi wartościami surowców z szablonu """
        new_players_list = []
        for plr in players:
            new_player = Player(plr.name, self.template.resources)
            new_players_list.append(new_player)
        return new_players_list

    def get_player(self, plr_name):
        """ Zwraca gracza po jego nazwie """
        plr = [plr for plr in self.players if plr.name == plr_name]
        if not plr:
            raise ValueError("Nie mozna zwrócić nieistniejącego gracza")
        return plr[0]

    def get_current_player(self):
        return self.players[self.current_player_index]

    def create_new_log(self, command_description):
        new_log = f"{self.get_current_player().name}: {command_description}"
        self.command_log.append(new_log)

    def end_turn(self):
        self.create_new_log("Koniec tury.")
        self.current_player_index += 1
        if self.current_player_index == len(self.players):
            self.current_player_index = 0

    def write_command_log(self):
        print("\n Game Log:")
        for command in self.command_log:
            print(command)
        print("\n")

    def __str__(self):
        return_str = f"Szablon: \n{str(self.template)} \nGracze: \n"
        for plr in self.players:
            return_str += str(plr) + "\n"
        return return_str
