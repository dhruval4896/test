#!/usr/bin/python

import os,socket,time,string,sys,commands

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("192.168.1.93",1234))

data=s.recvfrom(100)
data1=s.recvfrom(100)

if data[0]=='root' and data1[0]=='redhat' :
	print "Successful Authorization "
	s.sendto("Connected",data[1])
else:
	print "Check Authorization"
	s.sendto("Not Connected",data[1])

while True:
	gcmd=s.recvfrom(100)[0]
	rout=commands.getoutput(gcmd)
	s.sendto(rout,data[1])
