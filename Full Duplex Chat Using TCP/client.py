from socket import 
host = 'localhost'                
port = 8000
s = socket(AF_INET, SOCK_STREAM)
s.connect((host,port))
while True
    message = input(enter the message)             
    if message == ''
        break
    while message.lower() != 'go'
        message += 'rn'
        s.send(message.encode())
        message = input()
        if message == ''
                break
    else
        message = 'continuern'
        s.send(message.encode())
    data = s.recv(1024)
    data = data.decode().strip()
    if not data
            break
    while data.lower() != 'continue'
        print(data)
        data = s.recv(1024)
        data = data.decode().strip()
s.close()