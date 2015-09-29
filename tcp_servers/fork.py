#!/usr/local/bin/python

import os
import socket
import sys


server_socket = socket.socket()
server_socket.bind(('', 8080))
server_socket.listen(10)

while True:
    client_socket, remote_address = server_socket.accept()
    child_pid = os.fork()
    if child_pid == 0:
        request = client_socket.recv(1024)
        client_socket.send(request.upper())
        print '(child {}) {} : {}'.format(client_socket.getpeername(), request)
        client_socket.close()
        sys.exit()
    else:
        client_socket.close()

server_socket.close()
