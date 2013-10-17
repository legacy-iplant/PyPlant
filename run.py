for each in range(1,12):
	PLINK(usr,token,'plink-sim'+str(each),'/dalanders/simulation'+str(each)+'.ped','/dalanders/simulation'
		+str(10)+'.map','/dalanders/analyses/plink-sim'+str(each),'--assoc --adjust --allow-no-sex --out thisjob')

## 30051-30061

for each in range(1,12):
	sim = DownloadFile(usr,token,'analyses/plink-sim'+str(each)+'/thisjob.qassoc')
	sim = Data(sim)
	sim.WriteCSV('/users/dustin/documents/pyplant/saves/sim'+str(each)+'.txt')	