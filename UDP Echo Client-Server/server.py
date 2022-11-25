import socket
import sys

# Create a UDP socket
s = socket.socket(AF_INET, SOCK_DGRAM)
host = socket.gethostname()
port = 5000

s.bind((host,port))

s.listen(3)

while True:
    # Wait for a connection
    c, addr = s.accept()
     try:
        print ('connection from', addr)

        # Receive the data in small chunks and retransmit it
        while True:
            data = c.recv(16)
            print ('received "%s"' ,str(data))
            if data:
                print ('sending data back to the client')
                c.sendall(data)
            else:
                print ('no more data from', addr)
                break
            
    finally:
        # Clean up the connection
        c.close()
