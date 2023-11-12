
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
sayi3 = float(input("Üçüncü sayıyı girin: "))

if sayi1 >= sayi2 and sayi1 >= sayi3:
    en_buyuk_sayi = sayi1
elif sayi2 >= sayi1 and sayi2 >= sayi3:
    en_buyuk_sayi = sayi2
else:
    en_buyuk_sayi = sayi3

print("En büyük sayı:", en_buyuk_sayi)
