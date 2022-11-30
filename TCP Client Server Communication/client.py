import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=4952
s.connect((host,port))
msg=s.recv(1024).decode()
print(msg)
s.close()