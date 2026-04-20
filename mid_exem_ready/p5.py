import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 7000))
s.listen(1)

client, addr = s.accept()
print("Connected from", addr)

for i in range(3):
    data = client.recv(1024)
    if data == b"('ping')":
        client.send(b"('pong')")

client.close()