#!/usr/local/bin/python

import os
import socket
import sys


server_socket = socket.socket()
server_socket.bind(('', 8080))
server_socket.listen(10)

for i in range(4):
    child_pid = os.fork()
    if child_pid == 0:
        try:
            while True:
                client_socket, remote_address = server_socket.accept()
                request = client_socket.recv(1024)
                client_socket.send(request.upper())
                print '(child {}) {} : {}'.format(os.getpid(), client_socket.getpeername(), request)
                client_socket.close()
        except KeyboardInterrupt:
            sys.exit()

try:
    os.waitpid(-1, 0)
except KeyboardInterrupt:
    sys.exit()
