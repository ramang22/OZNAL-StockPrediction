customLogTransformNegative <- function(x){
  value <- abs(min(x))
  log(x+1+value)
}

customLogTransformZero <- function(x){
  log(x+1)
}

customLogTransform <- function(x){
  log(x)
}


# pomocne funkcie
getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}

description <- function(col){
  desc <- describe(col)
  desc$var_coef <-  sd(col)/mean(col)*100
  desc$med <- median(col)
  desc$mode <-  getmode(col)
  desc$iqr <-  IQR(col)
  return(desc)
}
