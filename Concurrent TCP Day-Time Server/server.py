import socket
import time
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
hostip = '127.0.0.1'
port = 9999
s.bind((hostip,port))
s.listen(5)
while(True):
    c,address = s.accept()
    Time = time.ctime() + '\r\n'
    c.send(str.encode(Time))
    sys.stdout.write('Time stamp sent to the address : {}\n'.format(address))
    c.close()