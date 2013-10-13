## Author: Dustin A. Landers
## Designed for the PyPlant project

import csv

"""
Use this Data class to turn downloaded files from the API and 
convert them in to a useable dictionary.

This Data object takes the string returned from the iPlant API,
where all the features of the data are only seperated by only some
spaces. It provides a dictionary object where each key is the row
number and each row number is a list containing that row's data.
"""

class Data:

	def __init__(self, str):
		self.data = self.ChangeToStr(self.Dataize(str), self.nrow)
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
				#print current_row
				data[row_num] = self.Rowize(current_row)
				num = point
				row_num += 1
		self.nrow = row_num - 1
		return data

	## This function changes unicode to regular stringse
	def ChangeToStr(self, data, rows):
		for row in range(rows):
			for cell in range(len(data[row])):
				data[row][cell] = str(data[row][cell])
		return data

	## This function changes numerical rows to floats
	def ChangeToFloat(self, float_col):
		for row in range(1,self.nrow):
			if isinstance(float_col, tuple):
				for cell in float_col:	
					self.data[row][cell] = float(self.data[row][cell])
			else:
				self.data[row][float_col] = float(self.data[row][float_col])

	## This function changes numerical rows to floats
	def ChangeToInt(self, int_col):
		for row in range(1,self.nrow):
			if isinstance(int_col, tuple):
				for cell in int_col:
					self.data[row][cell] = int(self.data[row][cell])
			else:
				self.data[row][int_col] = int(self.data[row][int_col])

	def Head(self):
		if self.nrow > 5:
			for row in range(5):
				print self.data[row]
		else:
			for row in range(self.nrow):
				print self.data[row]

	## This function exports the dictionary to csv
	def WriteCSV(self, file):
		with open(file, 'wb') as csvfile:
			writer = csv.writer(csvfile)
			for row in self.data:
				writer.writerow(self.data[row])

