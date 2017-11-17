import csv
import sys
import re

with open("state_units.csv", "r") as file:
	
	for row in iter(sys.stdin.readline, ''):	
		data = []
		regex = re.match(r"(\d+)\s+(\d+)\s+(\D+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)", row)

		if regex is None:
			pass
		else:
			data = [regex.group(1), regex.group(2), regex.group(3).strip(" "), regex.group(4), regex.group(5), regex.group(6), regex.group(7), regex.group(8), regex.group(9)]
			print data
