from socket import *
import struct

HOST = 'localhost'
PORT = 5050

client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST, PORT))

client.sendall(b'Hello')

data = client.recv(12)

sender_id, receiver_id, lumi, humi, temp, air, seq = struct.unpack('!HHBBBBI', data)

print(f'Sender:{sender_id}, Receiver:{receiver_id}, '
      f'Lumi:{lumi}, Humi:{humi}, Temp:{temp}, '
      f'Air:{air}, Seq:{seq}')

client.close()