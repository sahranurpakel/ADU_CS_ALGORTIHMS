def maxNumber(sayi1,sayi2,sayi3):

    en_buyuk = sayi1
    if sayi2>en_buyuk:
        en_buyuk = sayi2
    if sayi3>en_buyuk:
        en_buyuk = sayi3
    return en_buyuk    

print("En büyük sayı: ",maxNumber(34,78,12))        
