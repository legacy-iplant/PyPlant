## Just a script for messing with roc in matplotlib

from pyplant import *
import numpy as np 
import matplotlib as mat 

usr = 'dalanders'
psw = 'Shadow@3876'

#token = GetToken(usr,psw)
myfile = DownloadFile(usr,token,'analyses/plink-sim10-out/simulation1_--assoc.qassoc.adjusted')
sim10 = Data(myfile)

def table(var1, var1_values, var2, var2_values, data, nrow):
	zerozero = 0
	zeroone = 0
	onezero = 0
	oneone = 0
	for row in range(nrow-1):
		if data[var1][row] == str(var1_values[0]):
			if data[var2][row] == str(var2_values[0]):
				zerozero += 1
		if data[var1][row] == str(var1_values[0]):
			if data[var2][row] == str(var2_values[1]):
				zeroone += 1
		if data[var1][row] == str(var1_values[1]):
			if data[var2][row] == str(var2_values[0]):
				onezero += 1
		if data[var1][row] == str(var1_values[1]):
			if data[var2][row] == str(var2_values[1]):
				oneone += 1
	mytable = dict()
	mytable['00'] = zerozero
	mytable['01'] = zeroone
	mytable['10'] = onezero
	mytable['11'] = oneone
	return mytable

