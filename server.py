import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.11.45', 12345))
s.listen(5)

while True:
    print("accept...")
    conn, addr = s.accept()
    data = conn.recv(1024)
    print("data: {}, addr: {}" .format(data, addr))
    conn.sendall(b"Received: " + data)

s.close()