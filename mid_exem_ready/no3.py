from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
    
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    filename = msg.split()[1][1:]
    try:
        if filename == 'index.html':
            mimeType = 'text/html'
            f = open(filename, 'r', encoding='utf-8')
            content = f.read().encode('euc-kr')
        elif filename == 'iot.png':
            mimeType = 'image/png'
            f = open(filename, 'rb')
            content = f.read()
        elif filename == 'favicon.ico':
            mimeType = 'image/x-icon'
            f = open(filename, 'rb')
            content = f.read()
        elif 'exam' in filename:
            mimeType = 'text/html'
            q = filename.split("?q=")[-1]
            content = ('<HTML><HEAD></HEAD><BODY>Hello, ' + q + '</BODY></HTML>').encode()
        else:
            raise FileNotFoundError

        header = f'HTTP/1.1 200 OK\r\nContent-Type: {mimeType}\r\n\r\n'
        c.send(header.encode())
        c.send(content)

    except FileNotFoundError:
        header = 'HTTP/1.1 404 Not Found\r\n\r\n'
        body = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
        c.send(header.encode() + body.encode())

    c.close()