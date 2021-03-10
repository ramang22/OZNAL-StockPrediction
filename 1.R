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

#' 
#' # Analyza  (iba príjem)
#' 


getwd()

df <- read.csv(file = 'data_end/final.csv')

#
summary(df)

unique(df$symbol)