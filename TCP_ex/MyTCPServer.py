class TCPServer:
    def __init__(self, port):
        import socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('', port))
        self.socket.listen(5)

    def accept(self):
        self.c_sock, self.c_addr = self.socket.accept()
        return self.c_sock, self.c_addr
    
if __name__ == '__main__':
    server = TCPServer(8888)

    c, addr = server.accept()
    print('Connected by ', addr)

    c.send(b'Hello Client')
    c.close()