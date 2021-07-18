import hashlib
from getpass import getpass

passw = getpass("Enter new password (will not be echoed): ")
passwc = getpass("Confirm new password: ")

if(passw == passwc):
	pass
else:
	print("passwords do not match")
	quit()

key = hashlib.md5(passw.encode("utf-8"))
	
print(" ")
print(key.hexdigest())

