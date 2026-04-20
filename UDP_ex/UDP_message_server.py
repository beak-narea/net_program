import socket

port = 3333
BUFFSIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', port))
msg_box = {}
while True:
    data, addr = s.recvfrom(BUFFSIZE)
    msg = data.decode()
    if msg == 'quit':
        break
    else:
        msg = msg.split()
        mboxId = msg[1]
        if msg[0] == 'send':
            message = ' '.join(msg[2:])
            if mboxId not in msg_box:
                msg_box[mboxId] = []
            msg_box[mboxId].append(message)

        if msg[0] == 'receive':
            if mboxId in msg_box and len(msg_box[mboxId]) > 0:
                message = msg_box[mboxId].pop(0)
                s.sendto(message.encode(), addr)
            else:
                s.sendto('No messages'.encode(), addr)
s.close()