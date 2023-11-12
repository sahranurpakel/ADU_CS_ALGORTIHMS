def ortalama(vize,final):

    ortalama = vize*0.4 + final*0.6
    return ortalama
not_ortalaması = ortalama(78,65)
if not_ortalaması >= 50 :
    print("dersi geçtiniz")
else :
    print("dersi geçemediniz")
