# One Way ANOVA
One_Way_Anova_CBSE_2 <- read_excel("D:/Dhruva/One_Way_Anova_ CBSE_2.xlsx")
attach(One_Way_Anova_CBSE_2)
str(One_Way_Anova_CBSE_2)
One_Way_Anova_CBSE_2$Stream<-as.factor(One_Way_Anova_CBSE_2$Stream)
str(One_Way_Anova_CBSE_2)
library(car)
leveneTest(Marks~Stream,data = One_Way_Anova_CBSE_2)
# One way ANOVA
Model<-aov(Marks~Stream,data = One_Way_Anova_CBSE_2)
summary(Model)
# TukeyHSD pOST HOC tEST
TukeyHSD(Model)
model.tables(Model,"mean")
Model$residuals
shapiro.test(Model$residuals)
