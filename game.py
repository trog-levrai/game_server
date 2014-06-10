import socket
import select
class Game:
	"""Object created when a game is started
	- (nick1,nick2)
	- (addr1,addr2)"""
	def __init__(arg, connect):
		conn = connect
		client1 = arg[0]
		client2 = arg[1]
	def commute():
        	while True:
			clients, wlist, xlist = select.select([conn], [], [])
			for client in clients:
				data = client.recv(1024)
				if client == client1:
					client2.send(data)
				else:
					client1.send(data)
				
