library(ggplot2)
library(GGally)
library(kohonen)
library(RColorBrewer)

contrast <- c("#FA4925", "#22693E", "#D4D40F", "#2C4382", "#F0F0F0", "#3D3D3D") #my own, contrasting pairs
kindofpretty <- c("#B39B66", "#3B3828", "#FAE6B9", "#F2F2F2", "#86BA9F", "#135E1F", "#FFF70A", "#FFB10A", "#0498BD", "#FF780A") #my own
kindofpretty2 <- c("#B39B66", "#3B3828", "#FAE6B9", "#F2F2F2", "#F58B00", "#F5D800", "#7185A3", "#786187")

display.brewer.all() # 

#and then, e.g.:
cols <- brewer.pal(10, "Paired")
#Similarely, but a color function that will be called upon from inside other functions. Easy to change to rainbow, etc.
terraincolors <- function(n, alpha = 1) {
  terrain.colors(n, alpha=alpha)[n:1]
}

df <- read.csv(file = "/home/miki/Desktop/Docker/iNeuron/mice-protien-expression/data/final/data.csv")

head(df)

library(dplyr)
set.seed(33) #for reproducability
cols <- 1:77
df[cols] <- scale(df[cols])
df.som <- supersom(data= as.list(df), grid = somgrid(10,10, "hexagonal"), 
                dist.fct = "euclidean", keep.data = TRUE)

# df %>% mutate(across(where(is.numeric), scale))

# 
# df.som <- som(df, grid=df.grid, rlen=700, alpha=c(0.05,0.01), keep.data = TRUE)

summary(df.som)

par(mfrow=c(1,1)) #no of plots to combine
par(mar=c(5.1,4.1,4.1,2.1)) #par sets or adjusts plotting parameters. Not allways necessary. "mar" = margin.
plot(df.som, type="changes")

plot(df.som, type="count")

plot(df.som, type="dist.neighbours", palette.name=grey.colors, shape = "straight") 