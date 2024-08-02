import network
import socket

class Client():
    def __init__(self, socket: socket, address):
        self._socket = socket
        self._address = address

    def write(self, data):
        self._socket.send(bytes(data, 'utf-8'))

    def socket(self):
        return self._socket

    def address(self):
        return self._address

    def set_blocking(self, bool):
        self._socket.setblocking(bool)


class Server():
    def __init__(self, name):
        self.ap = network.WLAN(network.AP_IF)
        self.ap.active(True)
        self.ap.config(essid=name, password='1234')
        self._socket = None

    def socket(self):
        return self._socket

    def bind(self, port):
        self._socket = socket.socket()
        self._socket.bind(('', port))

    def listen(self):
        if self._socket:
            self._socket.listen()

    def accept_client(self):
        client_socket, client_address = self._socket.accept()
        return Client(client_socket, client_address)

    def read(self, client):
        client_socket = client.socket()
        data = client_socket.recv(2048)
        return data.decode('utf-8')

    def write(self, data, client):
        client_socket = client.socket()
        client_socket.send(bytes(data, 'utf-8'))

    def set_blocking(self, bool):
        self._socket.setblocking(bool)
