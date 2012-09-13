__author__ = 'pato'
import urllib, json, urllib2

class VPNMonitor:
    username = ''
    password = ''
    server = ''
    token = ''
    user = ''
    verbose = False

    def __init__(self, configFile = 'UKServer.conf', verbose = False):
        """
        @params: configFile

        Initialisation of parameters necessary for the Connectivity Test.
        """
        self.verbose = verbose
        self.__readConfig(configFile)

    def notificationTest(self):
        """
        @params:None

        Simple test of notification system.
        """
        message = "Test Notification VPNMonitor"
        params = urllib.urlencode({"token": self.token, "user": self.user, "message": message.encode('utf-8')})
        try:
            req = urllib2.Request("https://api.pushover.net/1/messages.json")
            handle = urllib2.urlopen(req, params)
            handle.close()
        except urllib2.URLError, e:
            print e

    def __readConfig(self, configFile):
        """
        @params configFile

        Reads a config file containing different parameters and loads them into the appropriate local parameters.
        """
        self.__printLog('Reading config file...')
        try:
            tempData = open(configFile, 'r')
            data = json.load(tempData)
            self.username = data['username']
            self.server = data['server']
            self.password = data['password']
            self.token = data['token']
            self.user = data['user']
            self.__printLog('Config file successfully loaded.')
        except Exception as exc:
            print('Config file could not be loaded!')
            print exc
            print('File not present or badly formatted JSON.')
            exit(1)

    def __printLog(self, out):
        """
        @params out

        Prints a LOG output if the verbose flag is raised.
        """
        if self.verbose:
            print(out)
        else:
            pass


monitorTest = VPNMonitor(configFile="UKServer.conf", verbose=True)
monitorTest.notificationTest()
