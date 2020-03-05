import socket
import json

print "creating a TCP Sender"

print "first step : create socket"

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print "second step : connect"

ip_address = '192.168.43.39'
port_number = 50001
receiver_address  = (ip_address,port_number)
s.connect(receiver_address)

print "third step : send data"

data = {"name":"Mohamad Ichwan Arrasid","nim":1301174580,"message":"Hadir"}
datax = json.dumps(data)
s.send(datax)

print "data", datax, "sent to", receiver_address

print "fourth step: close"
s.close()