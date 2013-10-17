dat<- read.table('Ann_largemarker.csv',sep=',',header=TRUE)
col.names<-dat[,1]
new.dat<-dat[,6:length(dat[1,])]
markers<-t(new.dat)
colnames(markers)<-col.names

QTL.num<-8
QTL.effects<-c(2,2,3,3,2,3,7,7)
mu<-35



length.marker<-length(markers[1,])
QTL.place<-sample(length.marker,QTL.num,replace=FALSE)
QTL.markers<-markers[,QTL.place[1]]
if (QTL.num > 1)
  {for (i in 2:QTL.num)
	{QTL.markers<-cbind(QTL.markers,markers[,QTL.place[i]]) }
	new.QTL<-matrix(nrow=length(QTL.markers[,1]),ncol=length(QTL.markers[1,]))
	new.QTL<-ifelse(QTL.markers=="A",1,new.QTL)
	new.QTL<-ifelse(QTL.markers=="B",0,new.QTL)
	new.QTL<-ifelse(QTL.markers=="-",NA,new.QTL)	
QTL.cor<-cor(new.QTL,use="pairwise.complete.obs")

repeat.code<-1
while (repeat.code==1)
{max.cor<-0
for (i in 1:(QTL.num-1))
  {for (j in (i+1):QTL.num)
    {if (QTL.cor[i,j] > max.cor) max.cor<-QTL.cor[i,j]}}

if (max.cor < 0.80) repeat.code<-0}
}

sim.val<-rep(mu,length(markers[,1]))
err.norm<-rnorm(length(markers[,1]))
sim.val<-sim.val+err.norm

if (QTL.num>1)
{
for (i in 1:length(markers[,1]))
  {for (j in 1:QTL.num)
    {if (QTL.markers[i,j]=="A") sim.val[i]<-sim.val[i] + QTL.effects[j]*(-0.5)
     if (QTL.markers[i,j]=="B") sim.val[i]<-sim.val[i] + QTL.effects[j]*(0.5)
}}}

if (QTL.num==1)
{for (i in 1:length(markers[,1]))  
{if (QTL.markers[i]=="A") sim.val[i]<-sim.val[i] + QTL.effects*(-0.5)
     if (QTL.markers[i]=="B") sim.val[i]<-sim.val[i] + QTL.effects*(0.5) }}

col.names[QTL.place]
QTL.place
QTL.effects

simulations<-cbind(simulations,sim.val)

write.table(simulations,"simulations_manymarker.csv",sep=",",row.names=FALSE,col.names=TRUE)
