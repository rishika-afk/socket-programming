import socket

s = socket.socket(AF_INET,SOCK_STREAM)
host = socket.gehostname()
port = 1616

s.connect((host,port))

print("server says:",s.recv(1024).decode())
i = input()
s.send(i.encode())
print(s.recv(1024).decode())
s.close()
