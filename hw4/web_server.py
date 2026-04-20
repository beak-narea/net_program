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
    msg = data.decode() # 예) GET /index.html HTTP/1.1 \r\n

    req = msg.split('\r\n')
    req = req[0].split(' ')[1]
    filename = req[1:]
    print(filename)
    if(req == '/index.html'):
        f = open(filename, 'r', encoding='utf-8')
        mimeType = 'text/html; charset=utf-8'
    elif(req == '/iot.png'):
        f = open(filename, 'rb')
        mimeType = 'image/png'
    elif(req == '/favicon.ico'):
        f = open(filename, 'rb')
        mimeType = 'image/x-icon'
    else: # 이상한거 달라고하면 처리할 코드
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