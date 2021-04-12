#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
#https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import os
import tkinter
def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()

    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg=="{download}":
        recv_msg = client_socket.recv(BUFSIZ).decode("utf8")
        f=open("D:\\client\\"+str(recv_msg)+".txt",'w',encoding='utf8')
        while True:
            recv_msg = client_socket.recv(BUFSIZ).decode("utf8")
            if recv_msg== "{end_downloading}":
                break
            f.writelines(str(recv_msg))
    if msg == "{quit}":
        client_socket.close()
        top.quit()
def send_login():
    msg_1 = my_msg1.get()
    msg_2= my_msg2.get()

    my_msg1.set("") 
    my_msg2.set("")  # Clears input field.
    client_socket.send(bytes(msg_1, "utf8"))
    client_socket.send(bytes(msg_2, "utf8"))

def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()
#-------------------------GUI for login-----------------------------------------
login=tkinter.Tk()

login.title("LOG IN")
#-------------user name
user_frame=tkinter.Frame(login)
my_msg1 = tkinter.StringVar()  # For the messages to be sent.
my_msg1.set("")

user_frame.pack(fill=tkinter.X)
lbl1 = tkinter.Label(user_frame, text="User name", width=10)
lbl1.pack(side=tkinter.LEFT, padx=8, pady=5)           
 
entry1 = tkinter.Entry(user_frame,textvariable=my_msg1)
entry1.pack(fill=tkinter.X, padx=1, expand=True)
#---------------password
pass_frame=tkinter.Frame(login)
my_msg2 = tkinter.StringVar()  # For the messages to be sent.
my_msg2.set("")

pass_frame.pack(fill=tkinter.X)
lbl2 = tkinter.Label(pass_frame, text="Password", width=10)
lbl2.pack(side=tkinter.LEFT, padx=8, pady=5)           
 
entry2 = tkinter.Entry(pass_frame,textvariable=my_msg2)
entry2.pack(fill=tkinter.X, padx=1, expand=True)

send_button = tkinter.Button(login, text="Log in", command=send_login,bg="orange", fg="red")
send_button.pack()

#---------------------------GUI for chat room-------------------------------------

top = tkinter.Tk()

top.title("Chat room")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=500, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send,bg="orange", fg="red")
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)


#----Now comes the sockets part----
HOST = input('Enter host: ')
PORT = input('Enter port: ')
if PORT=='':
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()

tkinter.mainloop()  # Starts GUI execution.
