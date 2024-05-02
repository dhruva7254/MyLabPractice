# Step wise Regression
MLR2 <- read_excel("D:/Dhruva/MR1.xlsx")
attach(MLR2)
# model considering all variables
mlrfitall <- lm(Buying~.,data = MLR2)
summary(mlrfitall)
mlrfitfirst <- lm(Buying~1,data = MLR2)
summary(mlrfitfirst)
# Step wise regression
# Forward selection
step(mlrfitfirst,direction = "forward",scope = formula(mlrfitall))
# Backward Elimination
step(mlrfitall,direction = "backward")
# Bi Directional
step(mlrfitfirst,direction = "both",scope = formula(mlrfitall))
