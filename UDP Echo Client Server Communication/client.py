import socket

msgFromClient = "Hello UDP Server"

bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1",20001)
buffersize = 1024

UDPClientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDPClientSocket.bind(("127.0.0.1",20002))
UDPClientSocket.sendto(bytesToSend,serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(buffersize)
msg = "Message from Server{}".format(msgFromServer[0])