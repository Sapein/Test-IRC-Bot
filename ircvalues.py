def getUsername(message):
    spMessage = message.Split("!")
    spMessage = spData[0].split(":")
    userName = spMessage[1]
    return userName

def getChannel(message):
    spMessage = message.split()
    channel = spMessage[2]
    return channel
