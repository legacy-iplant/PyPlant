## Just a script for messing with roc in matplotlib

execfile('pyplant.py')
execfile('data.py')

token = GetToken(usr,psw)
sim = DownloadFile(usr,token,'analyses/plink-sim10-out/simulation1_--assoc.qassoc.adjusted')

sim = Data(sim)
ChangeToStr(sim.data,sim.nrow)
ChangeToFloat(sim.data,sim.nrow)

