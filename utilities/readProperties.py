import configparser

config=configparser.RawConfigParser()

config.read(".\\Configurations\\config.ini")

class ReadConfig():
    # to access method (getApplicationURL) directly using class (ReadConfig), we have define as Staticmethod
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password