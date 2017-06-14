#!/usr/bin/python2

import os
import time
import string
import getpass

print "Welcome To Cloud Project"
time.sleep(2)

print "_________________________"
print"###########################"

#user for my project
user=raw_input(" Enter User Name: ")

#user password for project verification
password=getpass.getpass("Password: ")


if user == 'root' and password == 'redhat' :
	print " Access Granted "
	print " Please Wait "
	time.sleep(2)
	

else :
	print " Check Your Authentication"
	time.sleep(3)
	
