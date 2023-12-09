library(tidyverse)
library(ggplot2)
library(umap)

set.seed(0)
data = read.csv("./derived_data/contrywise_economicdata.csv")
colnames(data)[15] = "New_cases"
umapResult = umap(scale(data[c("GDPchange","GDPperCapita","Import","Export","Population")]))
umapdata = cbind(data[c("Country","WHO.Region","New_cases","Deathsper100Cases","Recoveredper100Cases")],data.frame(umapResult$layout))
colnames(umapdata) = c("Country","WHO.Region","New_cases","Deaths","Recovered","umap1","umap2")
km = kmeans(scale(data[c("GDPchange","GDPperCapita","Import","Export","Population")]),6)
umapdata = cbind(umapdata,"cluster"= km$cluster)

png("./figure/clusterandumap2.png",width=1000)
p1 = umapdata %>%
  ggplot(aes(x=umap1,y=umap2,color=Deaths)) +
  geom_point() +
  scale_color_gradient(low = "blue", high = "white")+
  theme(legend.position = "bottom")

p2 = umapdata %>%
  ggplot(aes(x=umap1,y=umap2,color=Recovered)) +
  geom_point() +
  scale_color_gradient(low = "red", high = "white")+
  theme(legend.position = "bottom")

gridExtra::grid.arrange(p2,p1,nrow=1)

dev.off()