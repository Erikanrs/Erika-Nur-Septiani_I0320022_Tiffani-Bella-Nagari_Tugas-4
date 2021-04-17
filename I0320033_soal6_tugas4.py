#menghitung operator bitwise
# 4 adalah 100 dalam biner dan 11 adalah 1011

x = 4
y = 11

print("Nilai: ", x,", binary", format(x, '08b'))
print("Nilai: ", y,", binary", format(y, '08b'))

#a. 4 | 11
c = 4 | 11
print("===========(4 | 11)===========")
print("Nilai: ",x,", binary", format(x, '08b'))
print("Nilai: ",y,", binary", format(y, '08b'))
print("--------------------------------(|)")
print("Nilai:",c,", binary", format(c, '08b'))

#b. 4 >> 11
c = 4 >> 11
print("===========(4 >> 11)===========")
print("Nilai: ",x,", binary", format(x, '08b'))
print("Nilai: ",y,", binary", format(y, '08b'))
print("--------------------------------(>>)")
print("Nilai:", c,", binary", format(c, '08b'))

#c. 4 ^ 11
print("===========(4 ^ 11)===========")
print("Nilai: ",x,", binary", format(x, '08b'))
print("Nilai: ",y,", binary", format(y, '08b'))
print("--------------------------------(^)")
print("Nilai:", c,", binary", format(c, '08b'))

#d. ~4
c = ~4
print("===========(~4)===========")
print("Nilai: ",x,", binary", format(x, '08b'))
print("Nilai: ",y,", binary", format(y, '08b'))
print("--------------------------------(~)")
print("Nilai:", c,", binary", format(c, '08b'))

#e. 11 & 4
c = 11 & 4
print("===========(11 & 4)===========")
print("Nilai: ",x,", binary", format(x, '08b'))
print("Nilai: ",y,", binary", format(y, '08b'))
print("--------------------------------(&)")
print("Nilai:", c,", binary", format(c, '08b'))
