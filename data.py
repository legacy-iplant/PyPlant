## Author: Dustin A. Landers
## Designed for the PyPlant project

from decimal import *

"""
Use this Data class to turn downloaded files from the API and 
convert them in to a useable dictionary.

This Data object takes the string returned from the iPlant API,
where all the features of the data are only seperated by only some
spaces. It provides a dictionary object where each key is the row
number and each row number is a list containing that row's data.
"""

class Data:

	def __init__(self, str, header=True):
		self.data = self.Dataize(str)
		self.header = self.data[0]

	def Rowize(self, test):
		row = []
		num = 0
		start = 0
		for char in test:
			if char == ' ' and test[num-1] != ' ':
				row.append(test[start:num])
				start = num
			if char != ' ' and test[num-1] == ' ':
				start = num 
			if num == len(test)-1:
				row.append(test[start:num+1])
				start = num
			num += 1
		return row

	def Dataize(self, test):
		data = dict()
		num = 0
		row_num = 0
		for point in range(len(test)+2):
			current_row = test[num:point]
			if current_row.endswith('\n') == True:
				current_row = current_row.strip()
				print current_row
				data[row_num] = self.Rowize(current_row)
				num = point
				row_num += 1
		self.nrow = row_num - 1
		return data

## This function changes unicode to regular strings
def ChangeToStr(data, rows):
	for row in range(rows):
		for cell in range(len(data[row])):
			data[row][cell] = str(data[row][cell])
	return data

## This function exports the dictionary to csv
def DataWriteCSV(dict, file):
	with open(file, 'wb') as csvfile:
		writer = csv.writer(csvfile)
		for row in dict:
			writer.writerow(dict[row])

"""

for row in range(1,3234):
	for cell in range(2,10):
		thing.data[row][cell] = float(thing.data[row][cell])

"""