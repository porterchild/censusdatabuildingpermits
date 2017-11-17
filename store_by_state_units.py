import csv
import sys

with open("state_units.csv", "r") as file:
	for row in csv.reader(iter(sys.stdin.readline, ''), delimiter=' '):	
		print row
		print len(row)
