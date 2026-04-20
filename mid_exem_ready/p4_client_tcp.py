from socket import *

# TCP 버전
# from socket import *

# s = socket(AF_INET, SOCK_STREAM)
# s.connect(('localhost', 9999))

# while True:
#     msg = input()
#     s.send(msg.encode())
#     data = s.recv(1024)
#     temp = int.from_bytes(data[0:2], 'big')
#     humi = int.from_bytes(data[2:4], 'big')
#     lumi = int.from_bytes(data[4:6], 'big')
#     print(f'Temp: {temp}, Humi: {humi}, Lumi: {lumi}')    
# s.close()
