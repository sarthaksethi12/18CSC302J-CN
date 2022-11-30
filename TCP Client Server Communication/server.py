import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=4952
s.bind((host,port))
s.listen(3)
while True:
    c,add=s.accept()
    print("connected to",add)
    c.send(bytes("hello client",'utf-8'))
    c.close()