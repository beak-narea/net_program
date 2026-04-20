from socket import *
import sys

BUF_SIZE = 1024
LENGTH = 4

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 7777))

s.send(b'Hello')

msg = s.recv(BUF_SIZE)
if not msg:
    s.close()
    sys.exit()
elif msg != b'Filename':
    print('server: ', msg.decode())
    s.close()
    sys.exit()
else:
    print('server: ', msg.decode())

filename = input('Enter filename: ')
s.send(filename.encode())

msg = s.recv(BUF_SIZE)
if not msg:
    s.close()
    sys.exit()
elif msg == b'Nofile':
    print('server: ', msg.decode())
    s.close()
    sys.exit()
else:
    rx_size = len(msg)
    data = msg
    while rx_size < LENGTH:
        msg = s.recv(BUF_SIZE)
        if not msg:
            s.close()
            sys.exit()
        data += msg
        rx_size += len(msg)
    if rx_size > LENGTH:
        s.close()
        sys.exit()
    file_size = int.from_bytes(data, 'big')
    print('server: ', file_size)

rx_size = 0
f = open(filename, 'wb')
while rx_size < file_size:
    msg = s.recv(BUF_SIZE)
    if not msg:
        break
    f.write(msg)
    rx_size += len(msg)

if rx_size < file_size:
    s.close()
    sys.exit()

print('Download complete')
s.send(b'Bye')
f.close()
s.close()
