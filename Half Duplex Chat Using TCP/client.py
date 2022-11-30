from socket import *
host = 'localhost'
port = 5069
s = socket(AF_INET, SOCK_STREAM)
s.connect((host,port))
while True:
  sentence = input("Enter Your message to server :")
  s.send(sentence.encode())
  message = s.recv(2049)
  print ("From Server -> ", message.decode())
  if(sentence == 'bye'):
    s.close()