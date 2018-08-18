#!/usr/bin/python           
# This is client.py file

import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
# Create a socket object

port = 12345                # Reserve a port for your service.

s.connect(("127.0.0.1", port)) # connect with server running on localhost
frame=raw_input('Enter number of frames')
win=raw_input('Enter window size')
a=frame
while a>0:
	
	buf = raw_input('Enter a frame no.: ')
	s.send(buf)
	ack=s.recv(1024)
	if ack==buf:
		print ack
	else:
	        print "Resending frame "+buf	     
		s.send(buf)

