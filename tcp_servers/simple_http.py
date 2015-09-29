#!/usr/local/bin/python

import os
import socket


def get_filename(request):
    first_line = request.splitlines()[0]
    filename = first_line.split(' ')[1][1:]
    return filename

def get_response(filename):
    files = os.listdir('.')
    if filename == '':
        return '<br>'.join('<a href="{}">{}</a>'.format(f, f) for f in files)
    elif filename in files:
        return '<a href="/">Back</a><pre>{}</pre>'.format(open(filename, 'r').read())
    else:
        return '404 Not found'


server_socket = socket.socket()
server_socket.bind(('', 8080))
server_socket.listen(10)

while True:
    client_socket, remote_address = server_socket.accept()
    try:
        request = client_socket.recv(1024)
        filename = get_filename(request)
        client_socket.send(get_response(filename))
        print '{} REQUESTED {}'.format(client_socket.getpeername(), filename)
        client_socket.close()
    except:
        pass

server_socket.close()