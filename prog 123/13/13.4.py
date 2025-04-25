from ipaddress import *
for i in range(32,1,-1):
    net = ip_network(f'98.162.75.183/{i}',0)
    if str(net.network_address) == "98.162.75.128":
        print(net.num_addresses)


