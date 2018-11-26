#!/usr/bin/env python3

import socket
from _thread import start_new_thread

ADDRESS = ''
PORT = 55667

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((ADDRESS, PORT))
sock.listen(3)

server_time = 0
list_of_clients = []
list_of_warnings = []

"""
Connects a new client by accepting it's connection and it's address. 
Each connection is given set of procedures via if/else statements. 
The data the clients have sent are analyzed in this function and prompt
responses are given. 
If the data given is in all caps, send a warning. If data is given in 
all caps again, kick the user and lose connection. If the user prompts 
the leave command, kick the user and lose connection. Else, broadcast the 
data to all connections.
"""
def newClient(connection, addr):
    global server_time
    connection.send(str.encode("Welcome to the chat room."))
    connection.send(str.encode("To quit, type ctrl + c ."))
    kicked_clients = False
    while True:
        data = connection.recv(1024)
        data = data.decode('utf-8')
        stripped_data = data.strip()
        if data:
            if data.isupper():
                for client in list_of_warnings:
                    if client == connection:
                        connection.send(str.encode("You are kicked."))
                        print(addr[0] + " was kicked.")
                        broadcast(str.encode(addr[0] + " was kicked."), connection)
                        kicked_clients = True
                        list_of_warnings.remove(connection)
                        remove(connection)
                        connection.send(str.encode("Kick"))
                        break
                if kicked_clients is True:
                    kicked_clients = False
                else:
                    list_of_warnings.append(connection)
                    connection.send(str.encode("Warning: All caps are not allowed."))
            elif stripped_data == "!leave":
                connection.send(str.encode("You have left the chat room."))
                print(addr[0] + " has left.")
                broadcast(str.encode(addr[0] + " has left."), connection)
                connection.send(str.encode("Kick"))
                remove(connection)
            else:
                print(addr[0] + ": " + data)
                m = str.encode(addr[0] + ": " + data)
                broadcast(m, connection)
        else:
            server_time += server_time

#Removes a specific connection anythime this function is called.
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

#Broadcasts a message(data) to all connected clients.
def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            clients.send(message)

#Main loop that runs the server continuosly and accepts connections within it.
while True:
    conn, addr = sock.accept()
    list_of_clients.append(conn)
    print(addr[0] + " connected")
    start_new_thread(newClient, (conn, addr)) #Each client is seperated in threads.



