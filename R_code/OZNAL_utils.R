
test <- function (){
  print("kappa")
}

head(df)

getBestValue <- function(){
  df <- read.csv("data/dataset_final.csv")
  df <- df[,-2]
  repre <- df[df$symbol == 'AAPL',]
}

customBoxPlot <-function(){
  boxplot(df$score)
}

customBoxPlot()
best <- getBestValue()
head(best)
# 
# 2. Q-Q Plot
# 3. Boxplot - vsetky
# 4. Histogram - vsetky
# 5. Graf odhadu hustoty
# 6. Graf spicatosti
# P-Q plot
# Graf rozptylu 
# stock graf - svieckovy - vsetky