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
		self.bio_data = self.biodata_transform()

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
		self.label = Label(master, text='Type full CSV location below \n Example: C:\Users\Dustin\Documents\Github\PyPlant \n')
		self.label.pack()
		self.en = Entry(master)
		self.en.pack()
		self.button = Button(master, text='Click here to transform and export as export.csv', command=self.load)
		self.button.pack()

	def load(self):
		filename = self.en.get()
		test = Data(filename)
		test.data_write(test.bio_data, 'export.csv')

root = Tk()
root.wm_title('Stapleton Lab Data Cleaner')
app = App(root)
root.mainloop()