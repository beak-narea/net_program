import ipaddress
addr = ipaddress.ip_address('192.0.2.1') # IPv4
print(addr)

addr6 = ipaddress.ip_address('2001:a8::1')
print(addr6)

print(addr.version)
print(addr6.version)

net = ipaddress.ip_network('114.71.220.0/24')
print(net)

print(net.with_netmask)
print(net.num_addresses)
print(net.netmask)
print(net.hostmask)

for x in net.hosts():
    # print(x)
    pass

print(addr in net)