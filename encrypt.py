from os import walk
import pyAesCrypt
import requests

def getFiles(basePath):
	f = []
	for (dirpath, dirnames, filenames) in walk("test"):
		names = [dirpath+"/"+x for x in filenames]
		f.extend(names)
	return f


def encrypt(password, filepath, bufferSize):	
	pyAesCrypt.encryptFile(filepath, filepath+".aes", password, bufferSize) 

def decrypt(password, filepath, bufferSize):	
	pyAesCrypt.decryptFile("test/data.txt.aes", "test/dataout.txt", password, bufferSize) 


if __name__ == "__main__":
	bufferSize = 64 * 1024

password = "foopassword" 
print(getDirs('test'))
