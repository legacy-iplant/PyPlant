require(pROC)

sim10 <- read.csv(file='test.txt',header=T)
known_truths <- c('csu303', 'gpm551', 'AY112215', 'IDP2516', 'umc1803', 'umc1174', 'gpm249b', 'php15024')
known_effects <- c(2,2,3,3,5,5,7,7)

sim10$truth <- ifelse(sim10$SNP %in% known_truths, 'Pos', 'Neg')

plot.roc(sim10$truth,sim10$P,main='Simmons-Simulation10',print.thres='best',percent=T,print.auc=T,col='#1c61b6')