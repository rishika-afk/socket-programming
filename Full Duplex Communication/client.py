import socket

s=socket.socket()
host=socket.gethostname()
port=4000

s.connect((host,port))

message = "Hi"
while (message != "exit"):
    message = s.recv(1024).decode()
    print("Server:",str(message))
    message = input()
    s.send(message.encode())

s.close()
