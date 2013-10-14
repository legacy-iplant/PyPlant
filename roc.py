## Just a script for messing with roc in matplotlib

from pyplant import *
import numpy as np 
import matplotlib.pyplot as mat 

usr = 'dalanders'
psw = 'Shadow@3876'

token = ListTokens(usr,psw,True)[1]
myfile = DownloadFile(usr,token,'analyses/plink-sim10-out/simulation1_--assoc.qassoc.adjusted')
sim10 = Data(myfile)
sim10.ChangeToFloat( tuple(range(2,10)) )
sim10.ChangeToInt(0)

known_truths = ['csu303', 'gpm551', 'AY112215', 'IDP2516', 'umc1803', 'umc1174', 'gpm249b', 'php15024']
SNP = sim10.data['SNP']
UNADJ = sim10.data['UNADJ']
BONF = sim10.data['BONF']


def seq(start, end, by):
	seq = []
	iterations = int((end-start)/by)
	#print iterations
	for each in range(iterations):
		seq.append(start)
		start = start + by
		#print start
	return seq

def roc(thres, thres_var):
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
		if thres_var[row] < thres:
			test.append(1)
		else:
			test.append(0)

	## Buidling table
	tp = 0.0
	tn = 0.0
	fp = 0.0
	fn = 0.0
	total_truth = sum(truth)
	total_false = len(truth)-total_truth
	for row in range(nrow):
		if truth[row] == 0 and test[row] == 0:
			tn += 1
		if truth[row] == 1 and test[row] == 0:
			fn += 1
		if truth[row] == 0 and test[row] == 1:
			fp += 1
		if truth[row] == 1 and test[row] == 1:
			tp += 1
	TPR = tp/(tp+fn)
	FPR = fp/(fp+tn)

	x = TPR
	y = FPR

	return (x,y)

plot_list_x = []
plot_list_y = []
for threshold in seq(0,1,0.001):
	tup = roc(threshold, UNADJ)
	plot_list_x.append(tup[0])
	plot_list_y.append(tup[1])
mat.plot(plot_list_x,plot_list_y)
mat.plot([0,1],[0,1])
mat.show()

"""plot_list_x = []
plot_list_y = []
for threshold in seq(0,1,0.001):
	tup = roc(threshold, BONF)
	plot_list_x.append(tup[0])
	plot_list_y.append(tup[1])
mat.plot(plot_list_x,plot_list_y)
mat.plot([0,1],[0,1])
mat.show()"""

