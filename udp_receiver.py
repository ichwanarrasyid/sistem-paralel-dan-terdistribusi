import socket

print "starting our socket UDP receiver"

print "start with prayer"

print "first step: Create socket"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#AF_INET: internet is used
#SOCK_DGRAM: UDP is used

print "second step: bind"

ip_address= "localhost"
port_number= 50000

receiver_address = (ip_address, port_number)
sock.bind((receiver_address))

print "third step: receive data from sender"
print "waint for something to arive..."

data, sender_address = sock.recvfrom(1024)

print "received data", data, 
print "from ", sender_address