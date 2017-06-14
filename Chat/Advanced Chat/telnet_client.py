#!/usr/bin/python

import os,socket,time,string,sys,commands,getpass

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s_ip="192.168.1.93"
s_port=1234

#telnet server username

user=raw_input("Enter User Name: ")
password=getpass.getpass("Enter User Password: ")

s.sendto(user,(s_ip,s_port))
s.sendto(password,(s_ip,s_port))

print s.recvfrom(100)
while True:
	cmd=raw_input("root@station150#")
	s.sendto(cmd,(s_ip,s_port))
	print s.recvfrom(100)[0]
