def _checkForExistance():
    try: 
        config = open('config.txt', 'r')
        config.close
        return True
    except IOError as e:
        return False

def _beginStage1Start():
    while open('config.txt') as config:
        print("hello")
        config.close()

def load_config():
    conf = _checkForExistance()
    if conf == True:
        _beginStage1Start()
    else:
        print("Pie")

