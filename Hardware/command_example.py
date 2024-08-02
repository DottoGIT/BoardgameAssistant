# Przykład jak mają działać komendy:


from command import Command
from game import Game
from Player import Player
from Resource import Resource
import socket


s = socket.socket()

# Read example:
# Laptop chce przeczytać ilość drewna Damiana Szprota:

cmd = Command()
s.send(cmd.send_read('Damian Szprot', 'drewno'))

# Ustroj:


while True:
    data = server.read(client)  # Odbiera dane przeslane przez laptopa
    cmd = Command(data)
    if cmd.command == 'read':
        amount = game.read_resource(*cmd.process())  # Odczytuje wartosc drewna
        readrespond = Command()  # Tworzy druga komende do informacji zwrotnej
        s.send(readrespond.send_readrespond(*cmd.process(), amount))  # Odsyła wartosc drewna
        break


# Laptop

while True:
    data = s.recv(1024)  # Odbiera do 1024 znakow
    cmd = Command(data)
    if cmd.command == 'readrespond':
        game.set_resource(*cmd.process())  # Ustawia wartosc odczytanego zasobu na wartosc przeslana przez ustroja


