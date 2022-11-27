import socket

s=socket.socket()
host=socket.gethostname()
port=4000

s.bind((host,port))

s.listen(5)

while True:
    c,add = s.accept()
    print("Connected to :",add)
    message = input()
    while (message != "exit"):
        c.send(message.encode())
        message = c.recv(1024).decode()
        print("Client:",str(message))
        message = input()
    c.close()
