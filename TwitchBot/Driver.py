#This is the main driver program for the whole program. This where the command starts.

from App import * #Logger class - error logging
import os #OS path

#Initialise the app
def main():
    App = App(appDirectory)

#Store the app directory
appDirectory = os.path.dirname(os.path.realpath(__file__))

#Initialise error logging
Logger = Logger(appDirectory, 'w')

#Try to run app, otherwise log the error
try:
    main()
except:
    Logger.createLog('')
