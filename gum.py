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

class Data():

	""" This is the standard Data object. It requires the location of the CSV file to be uploaded.
	self.data provides a dictionary of rows, so that self.data[0] provides the first row of the data.
	This could be used to extract the names for example. self.name provides the file location. 
	self.col provides a dictionary of columns, so that self.col[0] provides the first column of the
	data.
	"""

	def __init__(self, loc):
		self.name = loc
		self.data = self.data_read()
		self.ncol = self.ncol()
		self.nrow = self.nrow()
		self.col = self.colomize()

	def data_read(self):
		data = dict()
		with open(self.name, 'rb') as csvfile:
			reader = csv.reader(csvfile)
			n = 0
			for row in reader:
				data[n] = row
				n += 1
		return data

	def ncol(self):
		ncol = 0
		for row in self.data:
			if len(self.data[row]) > ncol:
				ncol = len(self.data[row])
		return ncol

	def nrow(self):
		nrow = 0
		for row in self.data:
			nrow += 1
		return nrow			

	def colomize(self):
		col_dict = dict()
		to_dict = []
		for column in range(self.ncol):
			for row in self.data:
				to_dict.append(self.data[row][column])
			col_dict[column] = to_dict
			to_dict = []
		return col_dict

	def transpose(self):
		trans_dict = dict()
		for row in self.data:
			


class App:

	def __init__(self, master):
		c = Canvas(master, width=400, height=400)
		c.grid()
		Label(master, text='Full CSV Location').grid(row=0, column=0, sticky=E)
		Entry(master).grid(row=0, column=1)

#root = Tk()
#app = App(root)
#root.mainloop()