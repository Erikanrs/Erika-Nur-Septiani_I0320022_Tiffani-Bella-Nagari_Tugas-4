#Memeriksa berat bagasi pesawat yang diperbolehkan

#Diketahui berat yang diperbolehkan
Berat_max = 50 lbs
lbs = 0.45 kg
Beratmaxdalamkg = 50 * 0.45
print("Berat maksimum dalam kg adalah: ", Beratmaxdalamkg, "kg")

kasusA = 110
kasusB = 49

resultA = kasusA < Beratmaxdalamkg
resultB = kasusB < Beratmaxdalamkg
print("Jika berat maksimum adalah: ", Beratmaxdalamkg, 'kg', "maka dengan berat lebih dari 110 kg, hasilnya: ", resultA)
print("Jika berat maksimum adalah: ", Beratmaxdalamkg, 'kg', "maka dengan berat 49 kg, hasilnya: ", resultB)
