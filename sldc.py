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
		self.label0 = Label(master, text='Welcome to the Stapleton Lab Data Cleaner. Please read the readme to make sure \n that your data is the proper format.\n')
		self.label0.pack()
		self.label = Label(master, text='Type full CSV location of import file')
		self.label.pack()
		self.en = Entry(master)
		self.en.pack()
		self.label2 = Label(master, text='Type full CSV location of export file')
		self.label2.pack()
		self.en2 = Entry(master)
		self.en2.pack()
		self.button = Button(master, text='Click here to transform and export', command=self.load)
		self.button.pack()

	def load(self):
		filename = self.en.get()
		export = self.en2.get()
		test = Data(filename)
		test.data_write(test.bio_data, export)

root = Tk()
root.wm_title('Stapleton Lab Data Cleaner')
app = App(root)
root.mainloop()