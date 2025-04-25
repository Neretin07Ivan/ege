from ipaddress import *
ad = ip_address('217.168.246.2')
net = ip_network('217.168.246.2/255.255.255.0',0)
print(net.network_address)
print(net.broadcast_address)
net = ip_network('146.212.200.55/255.255.240.0',0)
print(net.network_address)
print(net.num_addresses)
net = ip_network('1.1.1.1/255.255.255.224',0)
print(net.num_addresses)
net = ip_network('206.158.124.67/255.255.224.0',0)
k = -1
for ip in net:
    k += 1
    if str(ip) == "206.158.124.67":
        print(k)
