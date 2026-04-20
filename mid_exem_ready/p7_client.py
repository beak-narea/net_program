import socket

BUFF_SIZE = 1024
port = 5555

c_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c_sock.connect(('localhost', port))

for i in range(10):
    time = 1
    count = 0
    data = 'Hello, IoT'

    while True:
        c_sock.send(data.encode())
        print('Sent: ({}): Waiting up to {} secs for ack'.format(i, time))
        c_sock.settimeout(time)

        try:
            data = c_sock.recv(BUFF_SIZE)
        except socket.timeout: # 응답 못받았을 때, 재전송 조절
            print('Timeout, ', count)
            count += 1
            if count > 2:
                break

        else:
            print('Received: ', data.decode())
            break
     