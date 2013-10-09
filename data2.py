"""
This Data object takes the string returned from the iPlant API,
where all the features of the data are only seperated by only some
spaces. It provides a dictionary object where each key is the row
number and each row number is a list containing that row's data.
"""

class Data:

	def __init__(self, str):
		self.data = self.dataize(str)

	def rowize(self, test):
		row = []
		num = 0
		start = 0
		for char in test:
			if char == ' ' and test[num-1] != ' ':
				row.append(test[start:num])
			if char != ' ' and test[num-1] == ' ':
				start = num
			num += 1
		return row

	def dataize(self, test):
		data = dict()
		num = 0
		row_num = 0
		#for point in range(len(test)):
		current_row = test[num:120]
		if current_row.endswith('\n') == True:
			print current_row
			data[row_num] = rowize(current_row)
			#num = point
			row_num += 1
		return data