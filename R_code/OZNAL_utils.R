d <- read.csv("../data/dataset_final.csv")
summary(d)

# NAHRADIT SENTIMENT ZA NAZOV STLPCA
# qqplot
ggplot(d, mapping = aes(sample=sentiment)) + stat_qq() + stat_qq_line()

# boxplot 
ggplot(d, aes(x=log(sentiment))) + geom_boxplot(notch=TRUE) + coord_flip()

# histogram
ggplot(d, aes(x=log(sentiment))) + geom_histogram(color="black", fill="white")

# density estimate
ggplot(d, aes(x=log(sentiment))) + geom_density(color="black", fill="pink", alpha=.3)
  

# pomocne funkcie
getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}

description <- function(col){
  desc <- describe(col)
  desc$var_coef = sd(col)/mean(col)*100
  desc$mode = getmode(col)
  desc$iqr = IQR(col)
  return(desc)
}

# print stats
description(d$sentiment)
