
sayilar = input("Sayıları virgülle ayırarak girin: ")
sayi_listesi = list(map(int, sayilar.split(',')))
en_buyuk_sayi = max(sayi_listesi)
print("En büyük sayı:", en_buyuk_sayi)
