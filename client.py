import socket
import hashlib
import ast
from getpass import getpass

connip = "192.168.0.101"
connport = 4000

c = socket.socket()
c.connect((connip, connport))
c.settimeout(4)

print("connected")
welcome = c.recv(1024)
isauth = c.recv(1024).decode()
print(welcome.decode())

if(isauth == "auth is active"):
    print(isauth)
    sendpass = getpass("Enter password (will not be echoed): ")
    passcheck = hashlib.md5(sendpass.encode("utf-8")).hexdigest()
    c.send(passcheck.encode())
    check = c.recv(1024).decode()
    if(check == "correct"):
        print("correct password")
    else:
        print("incorrect password")
        quit()


while True:
    sender = input("fileshell> ")
    if(sender == "download"):
        choose = input("Name the file you want to download: ")
        newname = input("What name do you want to save it as? ")
        #check if file exists
        c.send("query".encode())
        c.send(choose.encode())
        check = c.recv(1024)
        check = check.decode()
        if(check == "Does not"):
            print("The file does not exist")
            continue
        c.send(sender.encode())
        c.send(choose.encode())
        print("File exists! Downloading file...")
        newfile = open(newname, "wb")
        content = c.recv(1024)
        while(content):
            try:
                newfile.write(content)
                content = c.recv(1024)
            except socket.timeout:
                newfile.close()
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
        filelist = ast.literal_eval(filelist)
        for file in filelist:
            print(file)
        continue
    sender = sender.encode()
    c.send(sender)
    textback = c.recv(1024)
    textback = textback.decode()
    print(textback)
    
    
