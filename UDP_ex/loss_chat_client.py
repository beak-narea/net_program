import socket

BUFF_SIZE = 1024
port = 5555

c_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c_sock.connect(('localhost', port))

while True:
    time = 2
    count = 0
    msg = input('->')

    while count <= 5:
        data = str(count) + ' ' + msg
        c_sock.sendto(msg.encode(), addr)
        print('Sent: ({}): Waiting up to {} secs for ack'.format(i, time))
        c_sock.settimeout(time)

        try:
            data, addr = c_sock.recvfrom(BUFF_SIZE)
        except socket.timeout: # 응답 못받았을 때, 재전송 조절
            print('Timeout, ', count)
            count += 1
            continue

        else:
            break
     