from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import os
import array as arr
import pyodbc 
import time
import tkinter

#----------------------------------------------------GUI-------------------------------------------------------
'''
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

top.protocol("WM_DELETE_WINDOW", on_closing)'''