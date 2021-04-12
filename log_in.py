from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import os
import array as arr
import pyodbc 
import time
import tkinter

#------------------------------------------------------Ham dang ki cho client---------------------------------------
def register(client):
    client.send(bytes("Login falied, register a new account: ","utf8"))
    f = open("D:\\login.txt",'r+',encoding = 'utf-8')
    infor =client.recv(BUFSIZ).decode("utf8")
    while True:
        line=f.readline()
        if line == "":
            f.writelines("\n"+infor)
            client.send(bytes("Register successfully !!! ","utf8"))
            break
        if line==infor:
            client.send(bytes("Register again","utf8"))
            infor =client.recv(BUFSIZ).decode("utf8")


#------------------------------------------------------dang nhap client---------------------------------------



def login(client):
    f = open("D:\\login.txt",'r',encoding = 'utf-8')
    infor =client.recv(BUFSIZ).decode("utf8")
    while True:
        line=f.readline()
        if line == "":
            return False
            f.close()
        if line==infor:
            client.send(bytes("login successfully","utf8"))
            return True