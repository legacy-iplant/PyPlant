require(pROC)
require(optparse)

make_option(c('-f','--file'),type='character',dest='myfile')
myparser <- OptionParser()
parse_args(myparser)

ten_list <- c('csu303', 'gpm551', 'AY112215', 'IDP2516', 'umc1803', 'umc1174', 'gpm249b', 'php15024')
three_list <- c('IDP865','IDP285')
eleven_list <- c('mmp136','AY110248','AY111178','bnl8.33','mmp131','umc1123','gpm878a','gpm598')
nine_list <- c('IDP644','gpm699c','gpm613','gpm339c','IDP676','psr371a')
eight_list <- c('bnlg1724','gpm658','umc1260','IDP3933','gpm390a','AY104289')
known_effects_sim <- c(2,2,3,3,5,5,7,7)

run <- function(file=myfile, truth.list='ten_list') {
	sim <- read.csv(file=file,header=T)
	sim$truth <- ifelse(sim$SNP %in% truth.list, 'Pos', 'Neg')
	rocobj1 <- plot.roc(sim$truth,sim$P,main=paste("ROC Curve For",file),
		print.thres='best',percent=T,print.auc=T,col='#1c61b6')
	lines(smooth(rocobj1, method='binormal'), col='#008600', print.auc=T)
	legend("bottomright", legend = c("Empirical", "Binormal smoothing"), 
		col = c("#1c61b6", "#008600"),lwd = 2)
	print(rocobj1$auc)
}