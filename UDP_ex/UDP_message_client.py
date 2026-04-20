import socket

port = 3333
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('Enter the message("send mboxId message" or "receive mboxId"): ')
    sock.sendto(msg.encode(), ('localhost', port))
    msg = msg.split()
    if msg[0] == 'quit':
        break
    elif msg[0] == 'receive':
        data, addr = sock.recvfrom(BUFFSIZE)
        print(data.decode())
sock.close()