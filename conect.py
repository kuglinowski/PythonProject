import urllib.request as urllib2
import json
from time import sleep

class Motion():

    def __init__(self, ip_add, port=8080, how_many_tries=3, interval=1):
        self.ip_address = ip_add
        self.port = port
        self.how_many_tries = how_many_tries
        self.interval = interval


    def isAppWorking(self):

        return True


    def motionData(self):
        list = []
        for y in range(0, self.how_many_tries):
            data = json.load(urllib2.urlopen("http://" + self.ip_address + ":" + self.port +"/sensors.json?sense=motion"))
            list.append(data)

            sleep(self.interval)
        return list


    def savePicture(self):

        return 1