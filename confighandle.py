def openConfigFile():
    try:
        config = open("config.txt", "r")
        config.close()
        values = readConfigFile()
        return values 
    except IOError as e:
        createConfigFile()
        return None

def createConfigFile():
    config = open("config.txt", "w")
    config.write("#Config File for Sapein's IRC Bot\n")
    config.write("#Version: 1.0\n")
    config.write("\n")
    config.write("##Connection##\n")
    config.write("irc server: irc.darknedgy.net\n")
    config.write("port: 6667\n")
    config.write("channel: #darknedgy\n")
    config.write("\n")
    config.write("##Bot Information##\n")
    config.write("Bot Nick: SapeinBot|Py\n")
    config.write("Threaded: False *NOT IMPLIMENTED\n")
    config.write("\n")
    config.write("##Modules##\n")
    config.write("*To add modules just add the name, ex: threading. or if it has a package include "+\
            "it in the package name\n")
    config.write("sapeinbot.standard *NOTE - This is just a psudeo import for the standard modules"+\
            "it is shorter than writing every module to include.\n")
    
def readConfigFile():
    values = []
    while open('config.txt') as config:
        for line in config:
            stuff = config.readline()
            if "#" in stuff:
                stuff.strip('\n')
                spStuff = stuff.split()
                if "1.0" in stuff:
                    version = stuff.split
                    values = readV1ConfigFile(version)
                    config.close()
                    return values
   return values
def readV1Config(version):
    values = []
    modules = []
    while open('config.txt') as config:
        for line in config:
            value = config.readline()
            try:
                value.split("#")
            else:
                spValue = value.split("*")
                value = spValue[0]
                if "Threaded" in value:
                    spValue = value.split(":")
                    values.append(spValue[1])
                if "sapeinbot.standard" in value:
                    modules.add("ircconnect")
                    modules.add("ircvalues")
            else:
                spValue = value.split(":")
                if "irc server" in spValue[0]:
                    values.append(spValue[1])
                if "port" in spValue[0]:
                    values.append(spValue[1])
                if "channel" in spValue[0]:
                    values.append(spValue[1])
                if "Nick" in  spValue[0]:
                    values.append(spValue[1])
          
            try:
                modules.append(value)
            except:
                values.append(modules)
                return values

    return values
