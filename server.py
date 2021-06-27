import socket
import os
import os.path

serverpath = "/root/serv"

myip = "192.168.0.101"
myport = 4000

s = socket.socket()
s.bind((myip, myport))
s.listen(5)
sock, addr = s.accept()
print(addr)
wel = f"Welcome to {socket.gethostname()}"
sock.send(wel.encode())
while True:
	filecommand = sock.recv(1024)
	if(filecommand.decode() == "help"):
		back = "commands:\nhelp - list this\nlist - list directory\ndownload - lets you download a file\ncloseserver - close socket"
		sock.send(back.encode())
	elif(filecommand.decode() == "list"):
		note = "Note: this only lists files, dirs are not supported"
		sock.send(note.encode())
		filelist = [f for f in os.listdir(serverpath) if os.path.isfile(os.path.join(serverpath,f))]
		filelist = str(filelist)
		sock.send(filelist.encode())
	elif(filecommand.decode() == "download"):
		whatfile = sock.recv(1024).decode()
		if(os.path.exists(serverpath + "/" + whatfile)):
			#goodnote = "exists"
			#goodcheck = sock.send(goodnote.encode())
			openfile = serverpath + "/" + whatfile
			sendfile = open(openfile, "rb")
			readcontent = sendfile.read(1024)
			while(readcontent):
				sock.send(readcontent)
				readcontent = sendfile.read(1024)
			sendfile.close()
		else:
			cool = "no file"
			sock.send(cool.encode())
	elif(filecommand.decode() == "query"):
		checkfile = sock.recv(1024).decode()
		if(os.path.exists(serverpath + "/" + checkfile)):
			sock.send("Does".encode())
		else:
			sock.send("Does not".encode())	
	elif(filecommand.decode() == "closeserver"):
		s.close()
		quit()
	else:
		back = "invalid command - use help for help"
		sock.send(back.encode())
