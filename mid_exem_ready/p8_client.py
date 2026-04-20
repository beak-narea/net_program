from socket import *
import sys

BUF_SIZE = 1024
LENGTH = 4

s = socket(AF_INET, SOCK_DGRAM)
s.connect(('localhost', 6789))

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
    pass
elif msg == b'No File':
    print('server: ', msg.decode())

else:
    f = open(filename, 'wb')
    f.write(msg)
    print('downloaded: ', filename)
    f.close()

s.send(b'Bye')

s.close()
sys.exit()

