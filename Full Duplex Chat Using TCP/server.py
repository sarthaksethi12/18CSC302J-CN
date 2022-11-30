from socket import *
host = 'localhost'
port = 8000
s= socket(AF_INET, SOCK_STREAM)
s.bind((host,port))
s.listen(5)

print("Starting the server")
while True:
	conn, addr = s.accept()      
	print("Connected to ", addr)
	while True:
		data = conn.recv(1024)
		if not data:                        
			break
		while data.decode().strip().lower() != 'continue':    
			print(data.decode().strip())                
			data = conn.recv(1024)   
		message = input(">")
		while message.lower() != 'go' and message != '':       
			message += '\r\n'
			conn.send(message.encode())
			message = input(">")
		else:
			if message != '':
				conn.send(message.encode())
				break
			else:
				break
	conn.close()