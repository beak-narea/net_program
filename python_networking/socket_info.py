import socket
import binascii

name = socket.gethostname()
print(name)
print(socket.gethostbyname(name))
print(socket.gethostbyname('home.sch.ac.kr'))

print(socket.gethostbyname_ex('home.sch.ac.kr'))

# print(socket.getfqdn('220.69.189.125'))
# print(socket.getfqdn('www.daum.net'))

string_address = '114.71.220.95'
packed = socket.inet_aton(string_address)
print('Original:', string_address)
print('Packed : ', binascii.hexlify(packed))
print('Unpacked:', socket.inet_ntoa(packed))