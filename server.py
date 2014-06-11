import socket
import threading
import select
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
		echo("lol")
	#On ajoute le client a la liste
		clients.append(conn_)
	#On avise en fonction de sa taille
	if len(clients) == 2:
		working = False
	#elif len(clients) > 2:
	#	echo("More than 2 clients, aborting game!")
	#	for client in clients:
	#		client.send(bytes("aborting", "utf-8"))
	#	clients = []
#for client in clients:
#	client.send(bytes("accepted", "utf-8"))
clientsToRead = []
while len(nick) < 2:
	try:
		clientsToRead, wlist, xlist = select.select(clients, [], [], 0.05)
	except select.error:
		pass
	else:
		for client in clientsToRead:
			n = client.recv(1024)
			n = n.decode()
			echo(n + " joined the gqme")
			nick.append(n)
for client in clients:
	client.send(bytes(nick[0], "utf-8"))
	client.send(bytes(nick[1], "utf-8"))
echo("Game starting")
logFile.Close()
game = Game(clients, connect)
threading.Thread(None, game.commute, None, (), {'nom':'thread1'}).start()
