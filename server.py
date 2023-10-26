# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:49:26 2023

@author: User
"""
#server

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#localhost = socket.gethostbyname(socket.gethostname())                               
server_socket.bind(('localhost', 3000))

server_socket.listen(5)

conn, addr = server_socket.accept()
print('Connected by', addr)

data = conn.recv(1024)
print('Received value:', data.decode())

n = data.decode()            
arr = []                     
for i in range(n):           
    if i==0:                 
        a = 0
    elif i==1:              
        a = 1
        arr = [0, 1]        
    else:                    
        a = arr[i-1] + arr[i-2]            
        arr.append(a)        
    print(a, end=',')        

conn.close()

server_socket.close()