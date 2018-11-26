#!/usr/bin/env python3


import socket
import sys
import select

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ADDRESS = '127.0.0.1'
PORT = 55667

socket.connect((ADDRESS, PORT))
#Runs the client by sending data to the server and recieving from the server
while True:
    sockets_list = [sys.stdin, socket]
    read, write, error = select.select(sockets_list, [], [])
    for i in read:
        if i == socket:
            message = socket.recv(2048)
            if message.decode('utf-8') == "Kick":
                socket.close()
                sys.exit(0)
            else:
                print(message.decode('utf-8'))
        else:
            message = sys.stdin.readline()
            m = str.encode(message)
            socket.send(m)
            sys.stdout.write(ADDRESS + " (You): ")
            sys.stdout.write(message)
            sys.stdout.flush()

