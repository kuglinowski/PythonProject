import urllib.request as urllib2
import cv2
import numpy as np
import time

# url = 'http://192.168.0.220:8080/shot.jpg'
# import os
#
# def createFolder(directory):
#     try:
#         if not os.path.exists(directory):
#             os.makedirs(directory)
#     except OSError:
#         print('Error: Creating directory. ' + directory)
#
# # Example
# createFolder('./data/')


# while True:

# Use urllib2 to get the image and convert into a cv2 usable format
# imgResp = urllib2.urlopen(url)
# imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
# img = cv2.imdecode(imgNp, -1)

# put the image on screen
# cv2.imshow('MyIPWebcam', img)

# To give the processor some less stress
# time.sleep(0.1)


# if cv2.waitKey(1) & 0xFF == ord('q'):
#     cv2.imwrite('asdf221.png', img)
#     break

from time import time, sleep

print(int(time()))
sleep(2)
print(int(time()))
