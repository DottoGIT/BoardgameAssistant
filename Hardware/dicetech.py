from wifi import Server
import time
import errno
from command import Command
from game import Game
from oled import Oled


def main():
    server = Server('ESP32')
    server.bind(8080)
    server.listen()
    client = None

    # To jest pewnie tymczasowe i trzeba to bedzie lepiej ogarnac ale dziala
    while not client:
        client = server.accept_client()
        time.slep(0.2)
    print('connection established')

    server.set_blocking(False)
    client.set_blocking(False)
    # disabling socket blocking will prevent the code from stopping when listening/reading requests

    cmd = None
    game = None
    game_initiated = False

    oled = Oled()

    while True:
        # Main loop of the program
        try:
            # Normalnie wywala blad jak nie dostaje danych bez blokowania wiec trzeba skurwysyna wylapac
            data = server.read(client)
            cmd = Command(data)
        except Exception as e:
            err = e.args[0]
            if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                time.sleep(0.2)
                continue

        if cmd is not None:
            if cmd.command == 'init':
                game = Game(*cmd.process())
                game.define_players()
                game_initiated = True

        if cmd is not None and game_initiated:
            if cmd.command == 'read':
                amount = game.read_resource(*cmd.process())
                with Command() as readrespond:
                    # Ten write nie wiem czy zadziała trzeba przetestowac
                    server.write(readrespond.send_readrespond(*cmd.process(), amount), client)
            elif cmd.command == 'add':
                game.add_resource(*cmd.process())
            elif cmd.command == 'write':
                game.set_resource(*cmd.process())

        if not game_initiated:
            oled.oled.text('Oczekiwanie na rozpoczącie gry...', 0, 0)
            oled.show_display()
        else:
            oled.oled.text('Rozpoczęto!', 0, 0)
            oled.show_display()
        # Tutaj trzeba teraz bedzie zrobic skrypty do oleda i ustroja
        # 1. Jak nie zaczela sie gra (game_initiated == False)
        # 2. Jak juz sie zaczela


if __name__ == "__main__":
    main()
