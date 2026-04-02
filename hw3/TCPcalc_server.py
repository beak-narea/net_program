from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connected from ', addr)
    while True:
        msg = client.recv(1024).decode()
        if not msg:
            break
        try:
            num1, op, num2 = msg.split(' ')
            num1, num2 = int(num1), int(num2)
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                result = num1 / num2
            
            client.send(str(result).encode())
        except Exception as e:
            client.send(b'Error: ' + str(e).encode())
    client.close()

