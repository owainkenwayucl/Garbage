temps = read.csv("temp.dat")

png(file="temperature.png", width=1024, height=720)

plot(temps$Temperature, xlab="Minutes since login", ylab="Temperature (°C)", main="Temperature of idling Raspberry Pi 4")

dev.off()