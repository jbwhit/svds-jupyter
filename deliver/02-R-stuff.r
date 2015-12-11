
library(dplyr)

library(ggplot2)

head(economics)

a <- ggplot(data = economics, aes(x = date, y = unemploy))
a <- a + geom_line()
a

a <- ggplot(data = economics, aes(x = date, y = unemploy))
a <- a + geom_line()
a <- a + geom_smooth(method = "loess")
a

df <- data.frame(birth_state=c("Illinois", "Arizona", NA),
                 data_scientist=c("Kevin", "Matt", "Jonathan"))

df

df$birth_state == "Arizona"

just_Arizona <- df[df$birth_state=="Arizona",]

just_Arizona

really_just_Arizona <- df[which(df$birth_state=="Arizona"),]

really_just_Arizona

a <- -5

a

a<-5

a


