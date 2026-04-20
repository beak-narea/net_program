import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 7000))

for i in range(3):
    sock.send(b"('ping')")
    time_start = time.time()
    data = sock.recv(1024)
    if data == b"('pong')":
        time_end = time.time()
        print(f"Success (RTT: {time_end - time_start:.6f})") # 소수점 6자리까지 출력

sock.close()