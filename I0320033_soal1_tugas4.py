# Operator Aritmatika

x = 15
y = 4

# Output: x + y = 19
print('x + y =', x + y)

# Output: x - y = 11
print('x - y =', x - y)

# Output: x * y = 60
print('x * y =', x * y)

# Output: x / y = 3.75
print('x / y =', x / y)

# Output: x // y = 3
print('x // y =', x // y)

# Output: x ** y = 19
print('x ** y =', x ** y)

x = 10
y = 12

# Output: x > y is False
print('x > y is', x > y)

# Output: x < y is True
print('x < y is', x < y)

# Output: x == y is False
print('x == y is', x == y)

# Output: x != y is True
print('x != y is', x != y)

# Output: x >= y is False
print('x >= y is', x >= y)

# Output: x <= y is True
print('x <= y is', x <= y)

#Operasi Logika

x = True
y = False

print('x and y is',x and y)

print('x or y is',x or y)

print('not x is', not x)

#OPERATOR STRING
#Contact Strings

#Strings

str1 = "Hello"
str2 = "World"

#contact

result = str1 + ' ' + str2

#Output

print(result):

#OPERATOR STRING
#Merep strings

#Strings

str = "HA"

# replicate

result = str * 3

# Output

print(result)

#OPERATOR STRING
Pengecekan membership-in

#strings

needle = "lo"
haystack = "Hello World"

#Check
if needle in haystack:
    print(needle,"is present in the string",haystack)
else:
    print("not found")

#OPERATORSTRING
#checking membership - not in

#Strings

needle = "HA"
haystack = "Hello World"

#Check
if needle in haystack
    print(needle,"is present in the string",haystack)
else:
    print("not found")

#OPERATOR STRING
#Mengakses karakter dalam string

# string
str =" Jane Doe"

#character
ch = str[1]

#Outout
print(ch) #a

#OPERATOR STRING
#Substring

#string
str = "Hello World"

#substring
substr = str[3:5]

#output
print(substr) #lo

#OPERATOR STRING
#Skipping character

str ="Hello World"

#skip
new_str = str[0:2]
print(new_str)

#OPERATOR STRING
#Reverse string

#string
str = "Hello World"

#reverse
result = str[::-1]

#output
print(result)

#OPERATOR BITWISE

a = 60          # 60 = 0011 1100
b = 13          # 13 = 0000 1101
c = 0

c = a & b;      # 12 = 0000 1100
print("line 1 - value of c is", c)

c = a | b;      # 61 = 0011 1101
print("line 2 - value of c is", c)

c = a ^ b;      # 49 = 0011 0001
print("line 3 - value of c is", c)

c = ~a;         # -61 = 1100 0011
print("line 4 - value of c is", c)

c = a << 2;      # 240 = 1111 0000
print("line 5 - value of c is", c)

c = a >> 2;      # 15 = 0000 1111
print("line 6 - value of c is", c)
