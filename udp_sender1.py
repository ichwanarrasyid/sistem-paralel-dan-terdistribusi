import socket

print "first step: Create socket"

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print "no need to bind"
print "second step: send data"

ip_address= "localhost"
port_number= 50000
reciver_address = (ip_address, port_number)

data = "heloo mr. Aji, your welcome !"

sock.sendto(data, reciver_address)

print "data ", data, " send to ", reciver_address
