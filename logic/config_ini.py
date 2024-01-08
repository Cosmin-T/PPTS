import configparser

INI = '/Volumes/Samsung 970 EVO/Documents/Python/PPTS/logic/config.ini'

def con():
    config = configparser.ConfigParser()
    config.read(INI)
    return config