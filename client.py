import socket

connip = "192.168.0.101"
connport = 4000

c = socket.socket()
c.connect((connip, connport))
c.settimeout(20)

print("connected")
welcome = c.recv(1024)
print(welcome.decode())
while True:
	sender = input("fileshell> ")
	#maybe we can put a if here and if its download we can put this in download mode
	if(sender == "download"):
		choose = input("Name the file you want to download: ")
		newname = input("What name do you want to save it as? ")
		c.send(sender.encode())
		c.send(choose.encode())
		#test = c.recv(1024).decode()
		#if(test == "no file"):
		#	print("Error: the file does not exist")
		#	continue
		newfile = open(newname, "wb")
		print("File exists! Downloading file...")
		content = c.recv(1024)
		while(content):
			try:
				newfile.write(content)
				content = c.recv(1024)
			except socket.timeout:
				newfile.close()
				print("Done downloading")
				break
				continue
			except ValueError:
				break
				continue
		newfile.close()
		print("Done downloading")
		continue
	if(sender == "list"):
		sender = sender.encode()
		c.send(sender)
		warnnote = c.recv(1024)
		print(warnnote.decode())
		print(" ")
		filelist = c.recv(4096)
		filelist = filelist.decode()
		filelist = eval(filelist)
		for file in filelist:
			print(file)
		continue
	sender = sender.encode()
	c.send(sender)
	textback = c.recv(1024)
	textback = textback.decode()
	print(textback)
	
	
