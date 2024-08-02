from wifi import Server, Client
from command import Command
import time, socket, errno

server = Server('ESP32')
server.bind(8080)
server.listen()
client = None
while not client:
    client = server.accept_client()
print('connection established')
server.set_blocking(False)
client.set_blocking(False)


while True:
    try:
        data = server.read(client)
        cmd = Command(data)
    except Exception as e:
        err = e.args[0]
        if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
            time.sleep(0.1)
            continue
