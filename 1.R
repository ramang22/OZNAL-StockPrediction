#' ---
#' title: "Analyza"
#' subtitle: "OZNAL"
#' author: "William Brach a Tomas Bedej"
#' date: "08.03.2021"
#' output: 
#'    prettydoc::html_pretty:
#'      toc: true    
#'      theme: default
#' ---
#+  include=FALSE
# obsah tohoto bloku sa v riešení nezobrazí
knitr::opts_chunk$set(collapse = TRUE)  # zlúčenie regiónov vstupu a výstupu
`%>%` <- magrittr::`%>%`  # pipe operátor
library("readxl")
library(magrittr)
library(corrplot)
library(ggplot2)
#' 
#' # Analyza
#' 

df <- read.csv(file = 'data_end/final.csv')

#' nazvy vsetkych features
colnames(df)
#' sumary jednotlvych features
summary(df)

head(df)
#' upvote ratio
hist(df$upvote_ratio)

#' vsetky symboly ktore spracovavame
unique(df$symbol)

# score
barplot(prop.table(table(df$score)), las=2, cex.names=.8, col=rgb(0.2,0.4,0.6,0.6),main="Barplot for feature Score")
boxplot(df$score)
# awards
barplot(prop.table(table(df$awards)), las=2, cex.names=.8, col=rgb(0.2,0.4,0.6,0.6),,main="Barplot for feature Awards")

#
dfX <- df[ -c(1,3,4) ]
res <- cor(dfX)
res
corrplot(res, type="lower", method="color", tl.col="black")

df$diff <- with(df, df$Close - df$Open )
ggplot(df, aes(x=diff, y=score)) + 
  geom_point() + ggtitle("APPLE STONKS : Score X (Close - Open) ")


x <- df[df$symbol == 'AAPL',]
x$diff <- with(x, x$Close - x$Open )
x
ggplot(x, aes(x=diff, y=score)) + 
  geom_point() + ggtitle("APPLE STONKS : Score X (Close - Open) ")
