from socket import *

s = socket()
s.bind(('127.0.0.1', 80))
s.listen(10)

while True:
    filename = ''
    mimeType = ''
    f = ''
    c, addr = s.accept()
    
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    req = req[0].split(' ')[1]
    if(req == '/index.html'):
        filename = 'index.html'
        f = open(filename, 'r', encoding='utf-8')
        mimeType = 'text/html; charset=utf-8'
    elif(req == '/iot.png'):
        filename = 'iot.png'
        f = open(filename, 'rb')
        mimeType = 'image/png'
    elif(req == '/favicon.ico'):
        filename = 'favicon.ico'
        f = open(filename, 'rb')
        mimeType = 'image/x-icon'
    else:
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>404 Not Found</TITLE></HEAD>')
        c.send(b'<BODY>404 Not Found</BODY></HTML>')
        c.close()
        continue
    c.send(('HTTP/1.1 200 OK\r\n').encode())
    c.send(('Content-Type: ' + mimeType + '\r\n').encode())
    c.send(b'\r\n')
    data = f.read()
    f.close()
    if(filename == 'index.html'):
        c.send(data.encode())
    else:
        c.send(data)
    c.close()