# mengenal operasi komparasi

# data1 = int(input("masukan data a : "))
# data2 = int(input("masukan data b : "))

# # lebih besar dari
# hasil = data1 > data2 
# print("nilai", data1, ">" , data2, "=", hasil)

# # lebih kecil dari
# hasil = data1 < data2
# print("nilai", data1 , "<", data2, "=", hasil)

# # lebih dari sama dengan
# hasil = data1 >= data2
# print("nilai", data1, ">=", data2, "=", hasil)

# # kurang dari sama dengan
# hasil = data1 <= data2
# print("nilai", data1, "<=", data2, "=", hasil)


# komparasi perbandingan nilai yang sama
a = 3
b = 4

hasil = a == 4
print("nilai", a, "sama dengan", 4, "=", hasil)

hasil = b == 4
print("nilai", b, "sama dengan", 4, "=", hasil)

# perbandingan nilai yang tidak sama dengan
hasil = a != 5
print("nilai", a, "tidak sama dengan", 5, '=', hasil)

hasil = a != 3
print("nilai", a, "tidak sama dengan", 3, '=', hasil)

# perbandingan nilai objek menggunakan is
x = 4
y = 5

print('nilai', x, 'ber id', hex(id(x)))
print('nilai', y, 'ber id', hex(id(y)))

hasil = x is 4
print('x is 4 = ', hasil)

hasil = x is 5
print('x is 5 = ', hasil)

hasil = y is 5
print('y is 5 = ', hasil)

hasil = y is 4
print('y is 4 = ', hasil)


# perbandingan nilai objek menggunakan is not
x = 4
y = 5

print('nilai', x, 'ber id', hex(id(x)))
print('nilai', y, 'ber id', hex(id(y)))

hasil = x is not 4
print('x is 4 = ', hasil)

hasil = x is not 5
print('x is 5 = ', hasil)

hasil = y is not 5
print('y is 5 = ', hasil)

hasil = y is not 4
print('y is 4 = ', hasil)


