# Two Way ANOVA
Two_way_ANOVA_2 <- read_excel("D:/Dhruva/Two_way_ANOVA_2.xlsx")
attach(Two_way_ANOVA_2)
str(Two_way_ANOVA_2)
Two_way_ANOVA_2$Place<-as.factor(Two_way_ANOVA_2$Place)
Two_way_ANOVA_2$Education<-as.factor(Two_way_ANOVA_2$Education)
str(Two_way_ANOVA_2)
# Two way ANOVA
Model<-aov(Sales~Place+Education,data = Two_way_ANOVA_2)
summary(Model)
Model1<-aov(Sales~Place+Education+Place:Education,data = Two_way_ANOVA_2)
summary(Model1)
TukeyHSD(Model1)
model.tables(Model1,"mean")

#---------------------------------------------
Model$residuals
shapiro.test(Model$residuals)

Model1$residuals
shapiro.test(Model1$residuals)
