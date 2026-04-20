from socket import *

s = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input()
    
    s.sendto(msg.encode(), ('localhost', 9999))
    
    data = s.recvfrom(1024)[0]

    temp = int.from_bytes(data[0:2], 'big')
    humi = int.from_bytes(data[2:4], 'big')
    lumi = int.from_bytes(data[4:6], 'big')
    print(f'Temp: {temp}, Humi: {humi}, Lumi: {lumi}')
    
s.close()