from socket import *
import random
import struct

HOST = 'localhost'
PORT = 5050

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print('서버 실행 중...')

while True:
    client, addr = server.accept()
    print('접속:', addr)

    msg = client.recv(1024)

    if msg == b'Hello':
        print('Hello 수신')

        sender_id = random.randint(1, 50000)
        receiver_id = random.randint(1, 50000)

        lumi = random.randint(1, 100)
        humi = random.randint(1, 100)
        temp = random.randint(1, 100)
        air = random.randint(1, 100)

        seq = random.randint(1, 100000)

        # ! = network byte order (big-endian)
        # H = 2 bytes unsigned short
        # B = 1 byte unsigned char
        # I = 4 bytes unsigned int
        packet = struct.pack('!HHBBBBI', # '!2H4BI' 와 같음
                             sender_id,
                             receiver_id,
                             lumi,
                             humi,
                             temp,
                             air,
                             seq)

        client.sendall(packet)

    client.close()