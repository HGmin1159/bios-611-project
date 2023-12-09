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

png("./figure/clusterandumap.png",width=1000)
p1 = umapdata %>%
  ggplot(aes(x=umap1,y=umap2,color=WHO.Region)) +
  geom_point() +
  theme(legend.position = "bottom")
p2 = umapdata %>%
  ggplot(aes(x=umap1,y=umap2,color=factor(cluster))) +
  geom_point() +
  theme(legend.position = "bottom")
gridExtra::grid.arrange(p1,p2,nrow=1)
dev.off()