import socket

host = socket.gethostbyname(socket.gethostname())
port = 4455

s = socket.socket()

s.bind((host, port))

s.listen()
print("[LISTENING] Server is listening.")

while True:
    conn, addr = s.accept()
    print(f"[NEW CONNECTION] {addr} connected.")

    filename = conn.recv(1024).decode()
    print(f"[RECV] Receiving the filename.")
    file = open(filename, "w")
    conn.send("Filename received.".encode())

    data = conn.recv(1024).decode()
    print(f"[RECV] Receiving the file data.")
    file.write(data)
    conn.send("File data received".encode())

    file.close()

    conn.close()
