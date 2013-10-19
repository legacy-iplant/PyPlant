require(optparse)
require(pROC)

options <- list(make_option(c('-f','--file'),type='character',dest='myfile'),
				make_option(c('-t','--truth'),type='character',dest='truthlist'))
myparser <- OptionParser(option_list=options)
myargs <- parse_args(myparser)
myfile <- myargs$myfile
truthlist <- myargs$truthlist

#ten_list <- c('csu303', 'gpm551', 'AY112215', 'IDP2516', 'umc1803', 'umc1174', 'gpm249b', 'php15024')
sim <- read.csv(file=myfile,header=TRUE)
simtruth <- as.character(read.table(file=truthlist,header=FALSE,stringsAsFactor=FALSE))

sim$truth <- ifelse(sim$SNP %in% simtruth, 'Pos', 'Neg')
rocobj <- roc(sim$truth~sim$P)

write(rocobj$auc,'auc.txt')