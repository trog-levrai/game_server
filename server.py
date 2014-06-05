import socket
import threading
import os
import time
os.chdir("/home/ilan/game_server")
logFile = open("server.log", "a")
#Fonction de communication
def commute(addr1, addr2):
	while True:
		data, addr = connect.recvfrom(1024)
		addr, port = addr
		#Si aucune donnee recue alors on break
		if not data:
			break
		elif addr == addr1:
			#C'est le 1 qui parle
			connect.sendto(data, (addr2, 1234))
		elif addr == addr2:
			#C'est le 1 qui parle
			connect.sendto(data, (addr1, 1234))
#Fonction qui gere l'affichage
def echo(string):
	logFile.write(time.asctime(time.localtime()) + " - " + string + "\n")
	print(string)
connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
connect.bind(('', 1234))
echo("Waiting for connections on port 1234...")
nick1 = ""
nick2 = ""
addr1 = ""
addr2 = ""
while nick1 == "" or nick2 == "":
	data, addr = connect.recvfrom(1024)
	data = data.decode('utf-8')
	addr, port = addr
	#On va remplir les infos d'adresse et de pseudo
	if nick1 == "":
		if data.startswith("nick:"):
			nick1 = data[5:]
			addr1 = addr
		else:
			echo("Identification failed")
	elif nick2 == "":
		if data.startswith("nick:"):
			nick2 = data[5:]
			addr2 = addr
		else:
			echo("Identification failed")
#Il faudra ajouter un envois des infos utiles aux joueurs (pseudos, ...)
connect.sendto(bytes("nick:" + nick2, "utf-8"), (addr1, 1234))
connect.sendto(bytes("nick:" + nick1, "utf-8"), (addr2, 1234))
echo(nick1 + " and " + nick2 + " have joined the game.")
logFile.Close()
threading.Thread(None, commute, None, (addr1,addr2), {'nom':'thread1'}).start()
