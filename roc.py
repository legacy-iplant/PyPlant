## Just a script for messing with roc in matplotlib

from pyplant import *
import numpy as np 
import matplotlib as mat 

usr = 'dalanders'
psw = 'Shadow@3876'

#token = ListTokens(usr,psw,True)[1]
#myfile = DownloadFile(usr,token,'analyses/plink-sim10-out/simulation1_--assoc.qassoc.adjusted')
sim10 = Data(myfile)

known_truths = ['csu303', 'gpm551', 'AY112215', 'IDP2516', 'umc1803', 'umc1174', 'gpm249b', 'php15024']
SNP = sim10.data['SNP']
UNADJ = sim10.data['UNADJ']
for each in range(len(UNADJ)):
	UNADJ[each] = float(UNADJ[each])

## Building truth list
truth = []
for row in range(3234):
	if SNP[row] in known_truths:
		truth.append(1)
	else:
		truth.append(0)

## Building test list
test = []
for row in range(3234):
	if UNADJ[row] < 0.01:
		test.append(1)
	else:
		test.append(0)

## Buidling table
tp = 0
tn = 0
fp = 0
fn = 0
for row in range(nrow):
	if truth[row] == 0:
		

def table(var1, var1_values, var2, var2_values, nrow):
	zerozero = 0
	zeroone = 0
	onezero = 0
	oneone = 0
	for row in range(nrow):
		if var1[row] == str(var1_values[0]):
			if var2[row] == str(var2_values[0]):
				zerozero += 1
		if var1[row] == str(var1_values[0]):
			if var2[row] == str(var2_values[1]):
				zeroone += 1
		if var1[row] == str(var1_values[1]):
			if var2[row] == str(var2_values[0]):
				onezero += 1
		if var1[row] == str(var1_values[1]):
			if var2[row] == str(var2_values[1]):
				oneone += 1
	mytable = dict()
	mytable['00'] = zerozero
	mytable['01'] = zeroone
	mytable['10'] = onezero
	mytable['11'] = oneone
	return mytable

