import socket

print "TCP Receiver"
print "first step: Create Socket"

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print "second step: bind"

ip_address= "localhost"
port_number= 50001
receiver_address = (ip_address, port_number)
sock.bind(receiver_address)

print "third step: listen"

sock.listen(1)

print "fourth step: accept"
print "waiting for connection to come..."

while True:
    conn, sender_address = sock.accept()
    print "fifth step: receiver data"
    datax = conn.recv(1024)
    try:
        data = json.load(datax)
    except ValueError:
        "bukan data json"
        
    print"received ", data, "from ", sender_address
    conn.close()


