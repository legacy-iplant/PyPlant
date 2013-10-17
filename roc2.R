## Title: Build ROC Curve for Simulation10-Simmons Datasets
## Author: Dustin Landers

sim10 <- read.csv(file='/users/dustin/documents/pyplant/saves/sim10.txt',header=T)
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

myseq <- sim10$P[order(sim10$P)]
holder <- matrix(nrow=length(myseq),ncol=2)

for (i in 1:length(myseq)) {
  #print(i)
  sim10$test <- ifelse(sim10$P < myseq[i],'Test Pos','Test Neg')
  mytab <- table(sim10$test,sim10$truth)
  holder[i,1] <- 1-TNR(mytab)
  holder[i,2] <- TPR(mytab)
}

plot(x=holder[,1],y=holder[,2],xlab='FPR',ylab='TPR',main='Simulation10-Simmons ROC Curve',type='l')
abline(a=0,b=1,lty=4)

holderq <- qnorm(holder)
holderq <- na.omit(holderq)

