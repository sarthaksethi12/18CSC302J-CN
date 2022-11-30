from socket import *
host='localhost'
port = 5069
s = socket(AF_INET,SOCK_STREAM)
s.bind((host,port))
s.listen(1)
print ("Welcome:The server is now ready to receive")
while True:
  conn, address = s.accept()
  sentence = conn.recv(2049).decode()
  print(f'From Client -> {sentence}')
  message = input("Enter your message to Client: ")
  conn.send(message.encode())
  if(message == 'q'):
    conn.close()