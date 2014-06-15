import socket
import threading
import select
import os
import time
os.chdir("/home/ilan/game_server")
logFile = open("server.log", "a")
#Fonction de communication
def commute():
	while True:
		try:
			senders, wlist, xlist = select.select(clients, [], [], 0.05)
		except select.error:
			pass
		else:
			for sender in senders:
				data = sender.recv(4096)
				if sender == clients[0]:
					clients[1].send(data)
				else:
					clients[0].send(data)
#Fonction qui gere l'affichage
def echo(string):
	logFile.write(time.asctime(time.localtime()) + " - " + string + "\n")
	print(string)
#Connexions en TCP/IP
connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect.bind(('', 1234))
connect.listen(5)
echo("Waiting for connections on port 1234...")
working = True
clients = []
nick = []
while working:
	#On check les nouveaux clients
	queries, wlist, xlist = select.select([connect], [], [])
	for conn in queries:
		conn_, info = conn.accept()
		echo("Connection accepted!")
	#On ajoute le client a la liste
		clients.append(conn_)
	#On avise en fonction de sa taille
	if len(clients) == 2:
		working = False
	elif len(clients) > 2:
		echo("More than 2 clients, aborting game!")
		for client in clients:
			client.send(bytes("aborting", "utf-8"))
		clients = []
clientsToRead = []
while len(nick) < 2:
	try:
		clientsToRead, wlist, xlist = select.select(clients, [], [])
	except select.error:
		pass
	else:
		for client in clientsToRead:
			n = client.recv(1024)
			n = n.decode()
			echo("New player coming: " + n)
			nick.append(n)
echo("Game starting")
logFile.close()
for client in clients:
	client.send(bytes("game", "utf-8"))
commute()
