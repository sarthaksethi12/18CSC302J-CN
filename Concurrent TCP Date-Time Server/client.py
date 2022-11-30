import socket
import sys

cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
serverip = '127.0.0.1'
serverport = 9999
cs.connect((serverip,serverport))
Time = cs.recv(1024)
Time = bytes.decode(Time,'utf-8')
sys.stdout.write('{}'.format(Time))
