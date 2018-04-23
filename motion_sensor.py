#!/usr/bin/python
import urllib.request as urllib2
import json, numpy as np
from decimal import Decimal
from time import sleep
dane_obrobione = []

from motion import Motion


# Configuration --------------
ipwebcam_address = "192.168.43.1"	# ipweb cam appliation address
ile_ostatnich_pomiarow = 40		# ile zbierac z jednego pomiaru - nie mniej niz 5 nie wiecej niz 49 / how many variables from one measurement
how_many_tries = 3 			# ile pomiarow / how many measurements
interval = 	1			# czas pomiedzy pomiarami / time between measurement

# EN: Weight in calculation variable of motion sensors from app
# PL: uwglednianie pomiarow z czujnika ruchu - jezeli nie miesci sie w zbiorze to 0
treshold_weight = 1

# EN: Weight in calculation variable of drift (how many move in image)
# PL: uwglednianie pomiarow z czujnika ruchu - jezeli nie miesci sie w zbiorze to 0
drift_weight  = 10

# EN: Final detection variable lower and upper set value
# PL: Zmienne okreslajace dolna i gorna granice wykrywania 
min_final_move = 1200
max_final_move = 3000
# ---------------------------







# CODE --------------------------------------------

for y in range(0,how_many_tries):
	data = json.load(urllib2.urlopen("http://"+ipwebcam_address+":8080/sensors.json?sense=motion"))
	print("---->>>>",data)
	number_of_elements=len(data[u'motion'][u'data'])
	print ("Number of elements", number_of_elements)
	print ("Ile pomiarow", (number_of_elements-ile_ostatnich_pomiarow))

	for x in range(number_of_elements-ile_ostatnich_pomiarow,number_of_elements):
		dane_obrobione.append(float(str(data[u'motion'][u'data'][x][1]).replace('[','').replace(']','')))
		# wyswietlanie danych pomiarowych
		# print(data[u'motion'][u'data'][x][1])

	sleep(interval)
ile_danych_obrobionych = len(dane_obrobione)

# Wyliczanie sredniej
srednia = np.mean(dane_obrobione);

# Wyliczanie drift (zmienosc probek)
diff = 0
for licznik in range(1,int(ile_danych_obrobionych/2)):
	diff = diff + abs(dane_obrobione[ile_danych_obrobionych-licznik] - dane_obrobione[0+licznik])	# WYLICZANIE DRIFT
diff = abs(diff)/ile_danych_obrobionych
if (diff == 0): diff=0.1						# jezeli zerob zeby nie wplywalo na srednio dajemy 0.1

print ("Dane: ",dane_obrobione)
print ("Dane: ",dane_obrobione)
print ("Ilosc probek:", ile_danych_obrobionych)
print ("Srednia", srednia)
print ("Diff", diff)

summary = (srednia * treshold_weight + diff * drift_weight)/treshold_weight+drift_weight

print (summary)

if ((summary > min_final_move) and (summary < max_final_move)):
	print ("Motion detected: 1")
else:
	print ("Motion detected: 0")

# CODE END --------------------------------------


a = Motion("192.168.43.1", "8080", 3, 1)
listt = a.pictureData()
print("--->>>", listt)
