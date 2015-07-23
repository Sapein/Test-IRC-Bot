import socket
import time
import passGen

channels = []
def ircConnect(nick="SapeinBot|Py",realname=":An IRC Bot",host="irc.darknedgy.net",port=6667,
        channel="#darknedgy"):
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Connecting to " + server + " - " + channel + " On port " + port)
    try:
        irc.connect((host,port))
        print("Connected")
    except:
        print("Non-existant server")
        return "NE_SERV"
    servPass = passGen.rgPass() 
    irc.send(("PASS " + servPass).encode('utf-8'))
    irc.send(("NICK " + nick).encode('utf-8'))
    irc.send(("USER " + nick + " * " + "0" + realname).encode('utf-8'))
    checkForFirstPing(irc)
    time.sleep(5)
    ircJoinChannel(irc, channel)
    returnList = []
    returnList.append(irc)
    returnList.append(channels)
    return resturnList

def ircJoinChannel(sokServer, channelName):
    print("Joining, " + channelName)
    socServer.send(("JOIN " + channelName).encode('utf-8'))
    channels.append(channelName)
    return channels
def checkForFirstPing(sokConnection):
    time.sleep(2)
    checkForPing(sockConnection)

def checkForPing(sokConnection):
    print("PONG")
    rbData = sockConnection.recv(2048)
    data = rbData.decode('utf-8')
    if "PING" in str(data):
        spData = data.split(":")
        response = data[1]
        sockConnection.send(("PONG :" + response + '\r\n').encode('utf-8'))

