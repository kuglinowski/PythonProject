import urllib.request as urllib2
import json
from time import sleep, time
import cv2
import numpy as np

class SensorException(Exception):
    def __init__(self, sensor):
        super().__init__("Error: Sensor {} is not switched on".format(sensor))


class Motion():

    def __init__(self, ip_add, port=8080, how_many_tries=3, interval=1):
        self.ip_address = ip_add
        self.port = port
        self.how_many_tries = how_many_tries
        self.interval = interval


    def isAppWorking(self):
        try:
            link = urllib2.urlopen("http://" + self.ip_address + ":" + self.port + "/sensors.json?sense=motion")
        except Exception:
            print('Error: Application is not working')
            return False
        else:
            data = json.load(link)
            if len(data) == 0:
                raise SensorException('motion')

        return True


    def motionData(self):
        list = []
        try:
            link = urllib2.urlopen("http://" + self.ip_address + ":" + self.port + "/sensors.json?sense=motion")
            for y in range(0, self.how_many_tries):
                data = json.load(link)
                list.append(data)
                sleep(self.interval)
        except Exception:
            print('Error: Application is not working')

        return list


    def savePicture(self):
        import os
        def createFolder(directory):
            try:
                if not os.path.exists(directory):
                    os.makedirs(directory)
            except OSError:
                print('Error: Creating directory. ' + directory)
        createFolder('./tmp_img/')

        tmp_url = ''
        try:
            url = "http://" + self.ip_address + ":" + self.port + "/shot.jpg"
            imgResp = urllib2.urlopen(url)
            imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
            img = cv2.imdecode(imgNp, -1)
            tmp_url = "./tmp_img/" + str(int(time())) + ".jpg"
            cv2.imwrite(tmp_url, img)
        except Exception:
            print('Error: Application is not working')

        return tmp_url
