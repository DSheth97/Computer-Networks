#!/usr/bin/python           
# This is server.py file

import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
# Create a socket object
port = 12345                # Reserve a port for your service.
s.bind(('', port))        # Bind to the port
s.listen(5)    
c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr             # Now wait for client connection.
while True:
	buf=c.recv(1024)
	print 'received ' + buf + '\n'
	ack=raw_input('Enter acknowledgement of received frame')
	c.send(ack)
	

