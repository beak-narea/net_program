from socket import *
import random

# TCP 버전
# from socket import *
# s = socket(AF_INET, SOCK_STREAM)
# s.bind(('localhost', 9999))
# s.listen(1)
# while True:
#     c, addr = s.accept()
#     msg = c.recv(1024).decode()
#     data = [0, 0, 0]
#     if(msg == '1'):
#         rand_max = 50
#     elif(msg == '2'):
#         rand_max = 100
#     elif(msg == '3'):
#         rand_max = 150
#     data[int(msg)-1] = random.randint(1, rand_max)
#     c.send(data[0].to_bytes(2, 'big') + data[1].to_bytes(2, 'big') + data[2].to_bytes(2, 'big'))
#     c.close()
# s.close()
