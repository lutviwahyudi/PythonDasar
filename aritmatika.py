a = 10
b = 3

# operasi tambah
hasil = a + b
print(a, '+', b, '=', hasil)

# operasi pengurangan
hasil = a - b
print(a, '-', b, '=', hasil)

# operasi perkalian
hasil = a * b
print(a, 'x', b, '=', hasil)

# operasi pembagian
hasil = a / b
print(a, ':', b, '=', hasil)

# operasi eksponen pangkat
hasil = a ** b
print(a, '**', b, '=', hasil)

# operasi modulus
hasil = a % b
print(a, '%', b, '=', hasil)

# operasi floor division //
hasil = a // b
print(a, '//', b, '=', hasil)

# prioritas operasi

'''
1. () tanda kurung
2. eksponen
3. perkalian dan teman-temannya **, /
4. pertambahan dan pengurangan +-
'''
x = 3
y = 2
z = 4

hasil = x ** y + z / y - z // x
print(hasil)