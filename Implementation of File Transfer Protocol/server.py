import socket
host= 'localhost'
port = 4455
FORMAT = "utf-8"
print("Server is starting.")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen()
print("Server is listening.")

while True:
    conn, addr = s.accept()
    print("connected to:",addr)
    filename = conn.recv(1024).decode(FORMAT)
    print("Receiving the filename.")
    file = open(filename, "w")
    conn.send("Filename received.".encode(FORMAT))
    data = conn.recv(1024).decode(FORMAT)
    print("Receiving the file data.")
    file.write(data)
    print(data)
    conn.send("File data received".encode(FORMAT))
    file.close()
    conn.close()
    print("disconnected .",addr)