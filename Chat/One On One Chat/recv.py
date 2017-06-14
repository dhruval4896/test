#!/usr/bin/python

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("192.168.1.93",4444))

while True :
	data= s.recvfrom(100)
	print "Msg From Client : ",data[0]
	print "Client Address : ",data[1][0]
	r=raw_input("Your reply")
	s.sendto(r,data[1])

