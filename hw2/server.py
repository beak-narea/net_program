import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)
sn = 20231313
while True:
    client, addr = s.accept()
    print('Connected from ', addr)
    client.send(b'Hello '+ addr[0].encode())
    msg = client.recv(1024)
    print(msg.decode())
    print(sn.to_bytes(4, 'big'))
    client.send(sn.to_bytes(4, 'big'))
    client.close()

