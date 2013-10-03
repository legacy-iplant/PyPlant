"""
********************************************
* Title: Creating data manipulation w/ Gui *
* Author: Dustin A. Landers                *
* License: GNU GPL-3                       *
********************************************
"""

import os
import csv
from Tkinter import *

def cls():
	os.system('cls')

class Data:

	""" 
	This is the standard Data object. It requires the location of the CSV file to be uploaded.
	self.data provides a dictionary of rows, so that self.data[0] provides the first row of the data.
	This could be used to extract the coloumn names for example. self.name provides the file location. 
	self.col provides a dictionary of columns, so that self.col[0] provides the first column of the
	data. self.col is essentially the transposed version of self.data.
	"""

	def __init__(self, loc):
		self.name = loc
		self.data = self.data_read()
		self.ncol = self.ncol()
		self.nrow = self.nrow()
		self.col = self.transpose()
		self.bio_data = self.biodata_transform()
		self.col_ncol = self.col_ncol()
		self.col_nrow = self.col_nrow()
		self.bio_data_ncol = self.biodata_ncol()
		self.bio_data_col = self.biodata_transpose()

	## This function reads the data in to a dictionary where each key is the row number
	def data_read(self):
		data = dict()
		with open(self.name, 'rb') as csvfile:
			reader = csv.reader(csvfile)
			n = 0
			for row in reader:
				data[n] = row
				n += 1
		return data

	## This function returns the number of columns in self.data
	def ncol(self):
		ncol = 0
		for row in self.data:
			if len(self.data[row]) > ncol:
				ncol = len(self.data[row])
		return ncol

	## This function returns the number of rows in self.data
	def nrow(self):
		nrow = 0
		for row in self.data:
			nrow += 1
		return nrow

	## This function returns the number of columns in self.col
	def col_ncol(self):
		ncol = 0
		for row in self.col:
			if len(self.col[row]) > ncol:
				ncol = len(self.col[row])
		return ncol

	## The function returns the number of rows in self.col
	def col_nrow(self):
		nrow = 0
		for row in self.col:
			nrow += 1
		return nrow			

	## This function provides a dictionary of lists (vectors in R) for each 
	## of the columns (as opposed to each of the row which is what self.data is)
	def transpose(self):
		col_dict = dict()
		to_dict = []
		for column in range(self.ncol):
			for row in self.data:
				to_dict.append(self.data[row][column])
			col_dict[column] = to_dict
			to_dict = []
		return col_dict

	## This function tranposes the data to the proper format
	def biodata_transform(self):
		trans_dict = dict()
		row_num = 0
		for row in self.data:
			use_range = range(len(self.data[row])-2)
			replicate = 1
			for i in use_range:
				use_range[i] = use_range[i] + 2
			for each in use_range:
				trans_dict[row_num] = [replicate, self.data[row][0], self.data[row][1], self.data[row][each]]
				row_num += 1
				replicate += 1
		return trans_dict

	## This function exports the dictionary to csv
	def data_write(self, dict, file):
		with open(file, 'wb') as csvfile:
			writer = csv.writer(csvfile)
			for row in dict:
				writer.writerow(dict[row])

class App:

	""" 
	This builds the GUI app which will eventually be put to an executable. 
	"""

	def __init__(self, master):
		c = Canvas(master, width=400, height=400)
		c.grid()
		Label(master, text='Full CSV Location').grid(row=0, column=0, sticky=E)
		Entry(master).grid(row=0, column=1)

#root = Tk()
#app = App(root)
#root.mainloop()