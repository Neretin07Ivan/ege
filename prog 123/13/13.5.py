#172.16.160.0 и маской сети 255.255.240.0.
from ipaddress import *
net = ip_network("172.16.160.0/255.255.240.0",0)
n = [f"{i:b}" for i in net]
k = 0
for i in n:
    if i.count("1") % 3 != 0:
        k += 1
print(k)