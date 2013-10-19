require(pROC)

args <- commandArgs(trailingOnly = TRUE)

arg1 <- args[1]
arg2 <- args[2]

#ten_list <- c('csu303', 'gpm551', 'AY112215', 'IDP2516', 'umc1803', 'umc1174', 'gpm249b', 'php15024')
sim <- read.csv(file=arg1,header=TRUE)
simtruth <- as.character(read.table(file=arg2,header=FALSE,stringsAsFactor=FALSE))

sim$truth <- ifelse(sim$SNP %in% simtruth, 'Pos', 'Neg')
rocobj <- roc(sim$truth~sim$UNADJ)

write(rocobj$auc,'auc.txt')