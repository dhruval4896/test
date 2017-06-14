#!/usr/bin/python

import socket

s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_ip="192.168.1.93"
server_port=4444

while True :	
	msg=raw_input("Enter A Message:  ")
	s.sendto(msg,(server_ip,server_port))
	print s.recvfrom(100)

