# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#client 

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

localhost = socket.gethostbyname(socket.gethostname())
client_socket.connect((localhost, 3000))

message = input("Enter a value: ")
client_socket.sendall(message.encode())

client_socket.close()