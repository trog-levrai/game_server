import socket
connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
connect.bind(('', 1234))
print("Waiting for connections on port 1234...")
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
			print("Identification failed")
	elif nick2 == "":
		if data.startswith("nick:"):
			nick2 = data[5:]
			addr2 = addr
		else:
			print("Identification failed")
#Il faudra ajouter un envois des infos utiles aux joueurs (pseudos, ...)
print(nick1 + " and " + nick2 + " have joined the game.")
while True:
	data, addr = connect.recvfrom(1024)
	addr, port = addr
	#Si aucune donnee recue alors on break
	if not data:
		break
	elif addr == addr1:
		#C'est le 1 qui parle
		connect.sendto(data, (addr2, 1234))
		print(nick1 + " just sent \"" + data.decode('utf-8') + "\" to " + nick2)
	elif addr == addr2:
		#C'est le 1 qui parle
		connect.sendto(data, (addr1, 1234))
		print(nick2 + " just sent \"" + data.decode('utf-8') + "\" to " + nick1)
