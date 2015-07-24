import confighandle 
import importlib

def Main():
    configValues = []
    configValues = confighandle.openConfigFile()              
    print(configValues)
    for module in configValues[len(configValues)-1]:
        importlib.import_module(module)
        print("Module", module, "imported!")

if __name__ == "__main__":
    Main()
