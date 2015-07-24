import botConfigs 
def openConfigFile():
    botConfigs.load_config()

def _openConfigFile():
    try:
        values = []
        values = readConfigFile()
        return values 
    except IOError as e:
        createConfigFile()
        return None

def createConfigFile():
    config = open("config.txt", "w")
    config.write(":Config File for Sapein's IRC Bot\n")
    config.write("Version: 1.0\n")
    config.write("\n")
    config.write("::Connection::\n")
    config.write("irc server: irc.darknedgy.net\n")
    config.write("port: 6667\n")
    config.write("channel: #darknedgy\n")
    config.write("\n")
    config.write("::Bot Information::\n")
    config.write("Bot Nick: SapeinBot|Py\n")
    config.write("\n")
    config.write("::Modules::\n")
    config.write("sapeinbot.standard\n")
    
def readConfigFile():
    values = []
    version = ""
    conf = open('config.txt', "r")
    conf.readline()
    version = conf.readline()
    version = version.strip('\n')
    spVersion = version.split(":")
    version = spVersion[1]
    if "1.0" in version:
        conf.close()
        values = readV1Config(version)
        return values
    return values
def readV1Config(version):
    values = []
    modules = []
    config = open('config.txt', 'r')
    for line in config:
        print(line)
        value = config.readline()
        config(value)
        value = value.strip('\n')
        spValue = value.split(":")
        if "sapeinbot.standard" in spValue:
            modules.append("ircconnect")
            modules.append("ircvalue")
        if "irc server" in spValue:
            print(spValue[1])
            values.append(spValue[1])
            print('i')
        if "port" in spValue:
            values.append(spValue[1])
        if "channel" in spValue:
            values.append(spValue[1])
        if "Nick" in  spValue:
            values.append(spValue[1])
          
        try:
            modules.append(value)
        except:
            values.append(modules)
            return values
    print(modules)
    print(values)
    return values
