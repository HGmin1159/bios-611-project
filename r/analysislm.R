library(tidyverse)
library(ggplot2)
library(umap)

data = read.csv("./derived_data/contrywise_economicdata.csv")

model1 = lm(New.cases/Population~Import+Export+GDPperCapita+Inflation,data=data)
model2 = lm(Deathsper100Cases~Import+Export+GDPperCapita+Inflation,data=data)
model3 = lm(Recoveredper100Cases~Import+Export+GDPperCapita+Inflation,data=data)
result_model = rbind(summary(model1)$coefficients[,4],
                     summary(model2)$coefficients[,4],
                     summary(model3)$coefficients[,4])
row.names(result_model) = c("New Cases","Deaths Per 100 Cases","Recovered per 100 Cases")
write.csv(result_model, "./table/result_lm.csv")

