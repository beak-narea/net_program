from socket import *

s = socket(AF_INET, SOCK_STREAM)
addr = ('localhost', 9000)
s.connect(addr)
while True:
    msg = input('Number to calculate: ')
    if msg == 'q':
        break
    
    s.send(msg.encode())
    
    print('Result: ', s.recv(1024).decode())
    
s.close()