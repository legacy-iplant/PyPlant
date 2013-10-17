usr = 'dalanders'
psw = 'Shadow@3876'
token = GetToken(usr,psw)

PLINK(usr,token,'plink-sim10-fisher','/dalanders/simulation10.ped','/dalanders/simulation10.map',
	'/dalanders/analyses/plink-sim10-fisher','--fisher --adjust --allow-no-sex --out thisjob')

PLINK(usr,token,'plink-sim10-model','/dalanders/simulation10.ped','/dalanders/simulation10.map',
	'/dalanders/analyses/plink-sim10-model','--model --allow-no-sex --out thisjob') ## 30043

PLINK(usr,token,'plink-sim10-modelfisher','/dalanders/simulation10.ped','/dalanders/simulation10.map',
	'/dalanders/analyses/plink-sim10-modelfisher','--modelfisher --allow-no-sex --out thisjob') ## 30044

PLINK(usr,token,'plink-sim10-bd','/dalanders/simulation10.ped','/dalanders/simulation10.map',
	'/dalanders/analyses/plink-sim10-bd','--bd --adjust --allow-no-sex --out thisjob')

PLINK(usr,token,'plink-sim10-homog','/dalanders/simulation10.ped','/dalanders/simulation10.map',
	'/dalanders/analyses/plink-sim10-homog','--homog --adjust --allow-no-sex --out thisjob')

PLINK(usr,token,'plink-sim10-linear','/dalanders/simulation10.ped','/dalanders/simulation10.map',
	'/dalanders/analyses/plink-sim10-linear','--linear --adjust --allow-no-sex --out thisjob')

PLINK(usr,token,'plink-sim10-logistic','/dalanders/simulation10.ped','/dalanders/simulation10.map',
	'/dalanders/analyses/plink-sim10-logistic','--logistic --adjust --allow-no-sex --out thisjob')

fisher = DownloadFile(usr, token, 'analyses/plink-sim10-fisher/thisjob.qassoc')
fisher = Data(fisher)
fisher.WriteCSV('/users/dustin/documents/pyplant/fisher.txt')

model = DownloadFile(usr,token,'analyses/plink-sim10-model/thisjob.qassoc')
model = Data(model)
model.WriteCSV('/users/dustin/documents/pyplant/saves/model.txt')

modelfisher = DownloadFile(usr,token,'analyses/plink-sim10-modelfisher/thisjob.qassoc')
modelfisher = Data(modelfisher)
modelfisher.WriteCSV('/users/dustin/documents/pyplant/saves/modelfisher.txt')

bd = DownloadFile(usr,token,'analyses/plink-sim10-bd/thisjob.qassoc')
bd = Data(bd)
bd.WriteCSV('/users/dustin/documents/pyplant/saves/bd.txt')

homog = DownloadFile(usr,token,'analyses/plink-sim10-homog/thisjob.homog')
homog = Data(homog)
homog.WriteCSV('/users/dustin/documents/pyplant/saves/homog.txt')

linear = DownloadFile(usr,token,'analyses/plink-sim10-linear/thisjob.assoc.linear')
linear = Data(linear)
linear.WriteCSV('/users/dustin/documents/pyplant/saves/linear.txt')

logistic = DownloadFile(usr,token,'analyses/plink-sim10-logistic/thisjob.assoc.linear')
logistic = Data(logistic)
logistic.WriteCSV('/users/dustin/documents/pyplant/saves/logistic.txt')