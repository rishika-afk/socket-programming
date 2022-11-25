import socket
import sys


s = socket.socket(AF_INET, SOCK_DGRAM)

# Connect the socket to the port where the server is listening
host = socket.gethostname()
port = 5000

s.connect((host,port))

try:
    
    # Send data
    message = 'This is the message.  It will be repeated.'
    print ( 'sending ', message)
    s.sendall(message)

   
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = s.recv(16)
        amount_received += len(data)
        print ('received', data)

finally:
    s.close()
