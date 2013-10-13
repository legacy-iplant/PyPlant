## Just a script for messing with roc in matplotlib
"""
execfile('pyplant.py')

token = GetToken(usr,psw)
sim_original = DownloadFile(usr,token,'analyses/plink-sim10-out/simulation1_--assoc.qassoc.adjusted')

sim = Data(sim_original)
sim.ChangeToFloat(tuple(range(2,10)))
sim.ChangeToInt(0)

assoc = Data(DownloadFile(usr,token,'analyses/plink-sim10-out/simulation1_--assoc.qassoc'))
assoc.ChangeToFloat(tuple(range(2,10)))
assoc.ChangeToInt(0)
"""
def FindLow(object, point, p=8, marker=1):
	my_markers = list()
	num = 0
	for row in range(object.nrow):
		if object.data[row][8] < point:
			num += 1
			my_markers.append(object.data[row][marker])
	print num
	return my_markers

