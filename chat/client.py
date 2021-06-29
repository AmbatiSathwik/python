import socket


c = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

c.connect((IP, 8951))
print("connected")


k = input()
c.send(bytes(k, 'utf-8'))
print(c.recv(1024).decode())
