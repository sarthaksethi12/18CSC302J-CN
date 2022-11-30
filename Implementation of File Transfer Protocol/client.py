import socket
host= 'localhost'
port = 4455
FORMAT = "utf-8"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
file = open ("sarthak.txt", "r")
data = file.read()
print(data)
s.send("sarthak.txt".encode(FORMAT))
msg = s.recv(1024).decode(FORMAT)
print("server:",msg)
s.send(data.encode(FORMAT))
msg = s.recv(1024).decode(FORMAT)
print("server:",msg)
file.close()
s.close()
