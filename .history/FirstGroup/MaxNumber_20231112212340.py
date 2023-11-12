def maxNumber(sayi1,sayi2,sayi3):

    if sayi1 >= sayi2 and sayi1 >= sayi3:
        en_buyuk_sayi = sayi1
    elif sayi2 >= sayi1 and sayi2 >= sayi3:
        en_buyuk_sayi = sayi2
    else:
        en_buyuk_sayi = sayi3
    return en_buyuk_sayi    

print("En büyük sayı:", maxNumber(25,89,167))
