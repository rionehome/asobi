import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.11.45', 12345))

msg = input("input: ")
s.sendall(msg.encode('utf-8'))
data = s.recv(1024)
print(data)

s.close()