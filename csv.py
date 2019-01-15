#!/usr/bin/env python3
import csv
import sys
with open("NYC_Free_Public_WiFi_03292017.csv", "rb") as f:
	  cr = csv.DictReader(f)
	  for row in cr:
	  	x = row['BORONAME']
	  	print (x)