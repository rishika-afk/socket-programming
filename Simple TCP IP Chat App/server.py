#Simple TCP client server application
import socket

s =  socket.socket(AF_INET,SOCK_STREAM)
host = socket.gethostname()
port = 1616

s.bind((host,port))

s.listen(5)

while True:
    c,addr = s.accept()
    print("Got connection from", addr)
    c.send("Thank you for connecting, send your message".encode())
    data = c.recv(1024).decode()
    print("from connected user: ",str(data))
    c.send("Message printed on console successfully.".encode())
    c.close()
    
