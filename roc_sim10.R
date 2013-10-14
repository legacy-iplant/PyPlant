## Title: Build ROC Curve for Simulation10-Simmons Datasets
## Author: Dustin Landers

sim10 <- read.csv(file='test.txt',header=T)
known_truths <- c('csu303', 'gpm551', 'AY112215', 'IDP2516', 'umc1803', 'umc1174', 'gpm249b', 'php15024')
known_effects <- c(2,2,3,3,5,5,7,7)

sim10$truth <- ifelse(sim10$SNP %in% known_truths, 'Pos', 'Neg')

TPR <- function(tab) {
  if (nrow(tab)==2 & ncol(tab)==2) {
    TP <- tab['Test Pos','Pos']
    TotalTruth <- sum(tab[,'Pos'])
    return(TP/TotalTruth)
  }
  else {
    return(NA)
  }
}

TNR <- function(tab) {
  if (nrow(tab)==2 & ncol(tab)==2) {
    TN <- tab['Test Neg','Neg']
    TotalFalse <- sum(tab[,'Neg'])
    return(TN/TotalFalse)
  }
  else {
    return(NA)
  }
}

myseq <- seq(0,1,0.00001)
holder <- matrix(nrow=length(myseq),ncol=2)

for (i in 1:length(myseq)) {
  #print(i)
  sim10$test <- ifelse(sim10$P < myseq[i],'Test Pos','Test Neg')
  mytab <- table(sim10$test,sim10$truth)
  holder[i,1] <- TPR(mytab)
  holder[i,2] <- 1-TNR(mytab)
}

plot(x=holder[,2],y=holder[,1],type='l',xlab='(1 - TNR) or FPR',ylab='TPR',main='ROC Curve for Simulation10-Simmons')