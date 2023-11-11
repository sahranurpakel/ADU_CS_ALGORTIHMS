sayı = int(input("bir sayı giriniz :"))
toplam = 0
for x in range(1,sayı) :
    if (sayı%x == 0) :
        toplam = toplam + x
if toplam == sayı :
    print("sayınız mükemmel sayı")
else :
    print("sayınız mükemmel sayı değil")