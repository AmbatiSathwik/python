import socket


c = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

c.connect(('2409:4070:2c83:cd61:be7c:8dce:79e7:cd43', 8951))
print("connected")


k = input()
c.send(bytes(k, 'utf-8'))
print(c.recv(1024).decode())
