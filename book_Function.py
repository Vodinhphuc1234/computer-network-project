from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import os
import array as arr
import pyodbc 
import time
import tkinter

#------------------------------------------------------Gui sach khi client yeu cau tai---------------------------------------
def sendBook(client,book_name):
    client.send(bytes("DOWNLOAD SUCCESSFULLY","utf8"))
    client.send(bytes(book_name,"utf8"))
    f=open("D:\\"+str(book_name)+".txt",'r',encoding='utf8')
    while True:
        line=f.readline()
        if not line:
            break
        client.send(bytes(line,"utf8"))
    f.close()
    client.send(bytes("{end_downloading}","utf8"))
    return
#------------------------------------------------------Gui sach khi client yeu cau doc---------------------------------------
def readBook(client,book_name):
    client.send(bytes(book_name,"utf8"))
    f=open("D:\\"+book_name+".txt",'r',encoding='utf8')
    while True:
        line=f.readline()
        if not line:
            break
        client.send(bytes(line,"utf8"))
    f.close()
    return
#------------------------------------------------------tim sach cho client ---------------------------------------------------
def find (client):
    ''' Tìm sách thông qua các cú pháp'''
    query=client.recv(BUFSIZ).decode()
    infor=query[0:query.find(' ')]
    i=0
    if infor=="F_ID":
        i=0
    if infor=="F_Name":
        i=1
    if infor=="F_Type":
        i=2
    if infor=="F_Author":
        i=3
    content=query[query.find(' ')+1:len(query)]
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-G9QD9GB\MYSQLSERVER;'
                      'Database=QLtv;'
                      'Trusted_Connection=yes;')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM SACH")

    book_name=""
    result = cursor.fetchall()
    for row in result:
        if content==str(row[i]):
            book_name=str(row[1])
            client.send(bytes(str(row)+"\n","utf8"))
    


    msg="Type {view} to read book "
    client.send(bytes('\n',"utf8"))
    client.send(bytes(msg,"utf8"))
    option = client.recv(BUFSIZ).decode()
    if str(option)=="{view}" :
        readBook(client,book_name)

    msg="Type {download} to download book."
    client.send(bytes(msg,"utf8"))
    option = client.recv(BUFSIZ).decode()
    if str(option)=="{download}":
        sendBook(client,book_name)