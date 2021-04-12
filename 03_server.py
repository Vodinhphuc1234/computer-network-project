#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
# https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import os
import array as arr
import pyodbc 
import time
import tkinter
import book_Function
import log_in


#------------------------------------------------------chap nhan yeu cau ket noi cua client---------------------------------------
def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Greetings from the cave! Now type your [<username> <password>] and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


#------------------------------------------------------xu li khi client da duoc ket noi---------------------------------------------


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""
    '''while True:
        find (client)'''
    if login(client) == False:
        register(client)
    client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name
    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break

#------------------------------------------------------Gui message den tat ca client---------------------------------------


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)
def quit():  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send(bytes("{quit}", "utf8"))
    SERVER.close()
        
clients = {}
addresses = {}
#---------------------GUI----------------------------------------------------------------
top=tkinter.Tk()
top.title("SERVER")
quit_button=tkinter.Button(top,text="Quit", command=quit,bg="orange", fg="red")
quit_button.pack()
#----------------------------------------------------main------------------------------------------------------
HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    print ("Enter number of listenings : ")
    num_listening=int(input())

    SERVER.listen(num_listening)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
    top.mainloop()
