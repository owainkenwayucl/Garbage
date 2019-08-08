temps_g <- read.csv("temp_gorillapi.dat")
temps_e <- read.csv("temp_easycargo_20mm.dat")
png(file="temperature.png", width=1024, height=720)


colours <- c(2,4)
plot(0,0,xlim=c(0,120), ylim=c(30,70), type="n", xlab="Minutes since login", ylab="Temperature (°C)", main="Temperature of idling Raspberry Pi 4")
lines(temps_g$Temperature, col = colours[1], type="b")
lines(temps_e$Temperature, col = colours[2], type="b")
legend("topleft", legend=c("GorlliaPi", "EasyCargo 20mm"), col = colours, pch=1)
dev.off()