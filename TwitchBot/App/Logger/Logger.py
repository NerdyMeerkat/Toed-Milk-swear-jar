#Error logging class: Logs to appDirectory/logs/error.logs

#Imports
import logging #Log errors
import os #For filesystem paths

#Error logging class

class Logger(object):
    modeHint = "'a' for append errors, 'w' for most recent error"

    #Constructors takes appDirectory
    def __init__(self, appDirectory: str, mode: modeHint):
        self.appDirectory = appDirectory
        self.logDirectory = appDirectory + "/logs"
        self.logFile = self.logDirectory + "/error.log"
        self.mode = mode #Append or write over

        #Call method to setup logger
        self.setupLogger()

    #Method creates directory if it doesn't exist
    def setupDirectory(self):
        if(not(os.path.isdir(self.logDirectory))):
            os.makedirs(self.logDirectory, mode = 0755)

    #Method creates file if it doesn't exist
    def setupFile(self):
        if(not(os.path.exists(self.logfile))):
            file = open(self.logFile, 'w')
            file.close()

    #Method to setup logging format
    def setupFormat(self):
        errorFormat = '%(asctime)s - %(levelname)s - %(message)s'
        dateFormat = '%m/%d/%Y %I:%M:%S %p'
        logging.basicConfig(filename = self.logFile, \
                            filemode = self.mode, \
                            level = logging.DEBUG, \
                            format = errorFormat, \
                            datefmt = dateFormat)

    #Method setups logger
    def setupLogger(self):
        self.setupDirectory()
        self.setupFile()
        self.setupFormat()

    #Method to create log in file
    def createLog(self, message : str) -> None:
        logging.exception(message)
