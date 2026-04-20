from socket import *
import os

BUF_SIZE = 1024
LENGTH = 4

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('localhost', 6789))

while True:
    data, addr = sock.recvfrom(BUF_SIZE)

    if not data:
        break
    elif data != b'Hello':
        print('client: ', data.decode())
        continue
    else:
        print('client: ', data.decode())
    sock.sendto(b'Filename', addr)

    data, addr = sock.recvfrom(BUF_SIZE)
    if not data:
        continue
    filename = data.decode()
    print('client: ', filename)
    
    try:
        filesize = os.path.getsize(filename)
    except:
        sock.sendto(b'No File', addr)
        continue
    else:
        f = open(filename, 'rb')
        data = f.read()
        for i in range(3):
            sock.sendto(b'Filename', addr)
            data, addr = sock.recvfrom(BUF_SIZE)
            if data == b'Bye':
                break

        f.close()

    print('client: ', data.decode()) 
    
