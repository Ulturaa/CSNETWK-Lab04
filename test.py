import socket
import threading

PORT = 3901
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)