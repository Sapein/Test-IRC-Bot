import socket
import passGen
import passGen

def ircConnect(host="irc.darknedgy.net",port=6667):
	irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		irc.connect((host,port))
	except:
		print("Non-existant server")
		return "NE_SERV"
	servPass = passGen.grPass() 
	irc.send(("PASS " + servPass).encode('utf-8')
	irc.send(("NICK
