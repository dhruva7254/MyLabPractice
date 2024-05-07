# Data Visualization using R
data(mtcars)
attach(mtcars)
View(mtcars)
# Histograms
hist(mtcars$mpg)
hist(mtcars$mpg, xlab = "Miles/gallon", main = "Histogram of MPG (mtcars)", breaks =12, col = "lightseagreen", border = "darkorange")
#Bar Plot
barplot(table(mtcars$cyl))
barplot(table(mtcars$am))
barplot(table(mtcars$cyl), xlab = "Number of cylinders", ylab = "Frequency", main = "mtcars dataset", col = "lightseagreen", border = "darkorange")
# Boxplot
boxplot(mtcars$wt)
boxplot(mpg ~ cyl , data = mtcars)
boxplot(mpg ~ cyl, data = mtcars,
        xlab = "Number of cylinders",
        ylab = "Miles/(US) gallon",
        main = "Number of cylinders VS Miles/(US) gallon",
        pch = 20,
        cex = 2,
        col = "lightseagreen",
        border = "red")
# Scatter Plots:
plot(mpg~disp, data=mtcars)
plot(mpg ~ disp, data = mtcars,
     xlab = "Displacement",
     ylab = "Miles Per Gallon",
     main = "MPG vs Displacement",
     pch = 20,
     cex = 2,
     col = "red")
v <- c(7,12,28,3,41)

# Give the chart file a name.
png(file = "line_chart.jpg")

# Plot the bar chart. 
plot(v,type = "o")

# Save the file.
dev.off()
counts <- table(mtcars$vs, mtcars$gear)
barplot(counts, main="Car Distribution by Gears and VS",
        xlab="Number of Gears", col=c("darkblue","red"),
        legend = rownames(counts))

#Calculate the frequency of different carb values using table function
mtcarscarb = table(mtcars$carb)
#Create percent label values
percentlabels<- round(100*mtcarscarb/sum(mtcarscarb), 1)
#Create labels for each pie in the chart
pielabels<- paste(percentlabels, "%", sep="")
#R code to create the Pie Chart
pie(mtcarscarb,col = rainbow(length(mtcarscarb)), labels = pielabels , main = 'Pie Chart for MTCars distribution of Carburetors', cex = 0.8)
#Legend for the pie chart
legend("topright", c("Carburetor-1","Carburetor-2","Carburetor-3","Carburetor-4","Carburetor-6","Carburetor-8"), cex=0.6, fill=  rainbow(length(mtcarscarb)))






