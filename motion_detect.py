import urllib.request as urllib2
import json, numpy as np
from decimal import Decimal
from time import sleep

class MotionDetect():
    def __init__(self, data, how_many_tries=3, interval=1):
        self.data = data
        self.how_many_tries = how_many_tries
        self.interval = interval

    def isMotionDetect(self):
        print(self.data)
        ile_ostatnich_pomiarow = 40
        dane_obrobione = []

        self.data.remove("[{'motion': {'unit': ''")
        print(self.data)
        number_of_elements = len(self.data[z][u'motion'][u'data'])
        #print("Number of elements", number_of_elements)
        #print("Ile pomiarow", (number_of_elements - ile_ostatnich_pomiarow))
        for z in range(0,3):

            for x in range(number_of_elements - ile_ostatnich_pomiarow, number_of_elements):
                dane_obrobione.append(float(str(data[u'motion'][u'data'][x][1]).replace('[', '').replace(']', '')))

                return True#dane_obrobione
class Motion():

    def __init__(self, ip_add, port="8080", how_many_tries=3, interval=1):
        self.ip_address = ip_add
        self.port = port
        self.how_many_tries = how_many_tries
        self.interval = interval


    def isAppWorking(self):

        return True

    def motionData(self):
        list=[]
        for y in range(0, self.how_many_tries):
            data = json.load(
                urllib2.urlopen("http://" + self.ip_address + ":" + self.port + "/sensors.json?sense=motion"))
            list.append(data)

            sleep(self.interval)
        return list


    def savePicture(self):

        return 1

connect=Motion("192.168.43.1")
motion_detect=MotionDetect(connect.motionData())
motion_detect.isMotionDetect()