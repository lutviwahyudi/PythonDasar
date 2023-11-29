# latihan konversi satuan temperatur

# program konversi celcius ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("masukan suhu dalam celcius :"))
print("suhu adalah", celcius, "C")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reammur adalah", reamur, "reamur")

#farenheit
farenheit = ((9/5) * celcius) + 32
print("suhu dalam farenheit adalah", farenheit)

#kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah", kelvin)