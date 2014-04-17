import socket
connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
connect.bind(('', 1234))
print("Waiting for data on port 1234")
while True:
	data, addr = connect.recvfrom(1024)
	#Si aucune donnee recue alors on break
	if not data:
		break
	print ("On vous dit: " + str(data))
