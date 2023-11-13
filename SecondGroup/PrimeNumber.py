def asal_mi(sayı):
    if(sayı == 1):
        return print(sayı,"asal sayı değildir.")
    elif(sayı == 2):
        return print(sayı,"asal sayıdır.")
    else:
        for i in range(2,sayı):
            if(sayı % i == 0):
                return print(sayı,"asal sayı değildir.")
        return print(sayı,"asal sayıdır.")

asal_mi(13)