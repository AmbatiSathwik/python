#  type something


import socket

# creates a server socket
server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# binds with the client  bind ((ip-addr , port-number))
server.bind((IP, 9999))

# listens to the client
server.listen(20)


while True:
    x, addr = server.accept()
    print("connected to client")
    msg = x.recv(1024).decode()
    print(f"client : {msg}")

    if msg == "Hello":
        x.send(bytes("Hi mawa", "utf-8"))
    x.close()
