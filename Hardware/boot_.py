from machine import Pin, ADC
from command import Command
from game import Game
from oled import Oled
from joystick import Joystick
from wifi import Server
import time


def main():
    server = Server('ESP32')
    server.bind(8080)
    server.listen()
    client = None

    oled = Oled()
    oled.oled.text('waiting for', 0, 0)
    oled.oled.text('connection...', 0, 10)
    oled.show_display()

    while not client:
        client = server.accept_client()  # Client socket
        time.sleep(0.2)
    print('connection established')

    server.set_blocking(False)
    client.set_blocking(False)

    cmd = None
    game = None
    game_initiated = False
    value_change = 0

    place = ''
    joy = Joystick(34, 35)

    selected_player = None
    selected_player_index = 0

    while True:
        # Main loop of the program
        joy.get_input()

        if cmd is not None:
            if cmd.command == 'init':
                game = Game(*cmd.process())
                game.define_players()
                game_initiated = True

                cmd = None
                place = 'menu'
            elif cmd.command == 'load':
                game = Game(*cmd.process())
                game.define_players()
                game.load_data()
                game_initiated = True

                cmd = None
                place = 'menu'

        if cmd is not None and game_initiated:
            if cmd.command == 'read':
                amount = game.read_resource(*cmd.process())
                with Command() as readrespond:
                    server.write(readrespond.send_readrespond(*cmd.process(), amount), client)
            elif cmd.command == 'add':
                game.add_resource(*cmd.process())
            elif cmd.command == 'write':
                game.set_resource(*cmd.process())
            cmd = None

        if not game_initiated:
            oled.oled.text('Oczekiwanie na rozpoczącie gry...', 0, 0)
            oled.show_display()
        else:
            if place == 'menu':
                oled.move_cursor(joy.state)
                oled.display_menu()
                if joy.state == 'right':
                    if oled.selected_option == 0:
                        place = 'dice'
                        game.throw_dice()
                    elif oled.selected_option == 1:
                        place = 'list_of_players'
                        oled.selected_option = selected_player_index
                    elif oled.selected_option == 2:
                        cmd = Command()
                        cmd_string = cmd.send_endturn()
                        server.write(cmd_string, client)

            elif place == 'dice':
                oled.display_dice_result(game.last_throws)
                if joy.state == 'left':
                    place = 'menu'
                elif joy.state == 'right':
                    place = 'dice'
                    game.throw_dice()
                    cmd = Command()
                    cmd_string = cmd.send_diceresult(game.last_throws)
                    server.write(cmd_string, client)

            elif place == 'list_of_players':
                oled.display_list_of_players(game.players.values())  # bierzemy wartosci slownika bo inaczej zwraca stringi
                oled.move_cursor(joy.state)
                if joy.state == 'right':
                    selected_player = list(game.players.values())[oled.selected_option]
                    place = 'player_resources'
                    selected_player_index = oled.selected_option
                    oled.selected_option = 0
                elif joy.state == 'left':
                    place = 'menu'
                    oled.selected_option = 1

            elif place == 'player_resources':
                oled.display_player_resources(selected_player)
                oled.move_cursor(joy.state)
                if joy.state == 'left':
                    place = 'list_of_players'
                    oled.selected_option = selected_player_index
                elif joy.state == 'right':
                    place = 'resource'

            elif place == 'resource':
                oled.display_player_resources(selected_player, True)
                if joy.state == 'left':
                    place = 'player_resources'
                    add_cmd = Command()
                    resource = list(selected_player.get_resources().values())[oled.selected_option]
                    add_string = add_cmd.send_add(selected_player.get_name(), resource.get_name(), value_change)
                    server.write(add_string, client)
                    value_change = 0

                elif joy.state == 'up':
                    resource = list(selected_player.get_resources().values())[oled.selected_option]
                    value_change += resource.add_amount(1)
                elif joy.state == 'down':
                    resource = list(selected_player.get_resources().values())[oled.selected_option]
                    value_change += resource.add_amount(-1)

        try:
            # Normalnie wywala blad jak nie dostaje danych bez blokowania wiec trzeba wylapac
            data = server.read(client)
            cmd = Command(data)
        except Exception as e:
            err = e.args[0]
            pass


if __name__ == "__main__":
    main()
