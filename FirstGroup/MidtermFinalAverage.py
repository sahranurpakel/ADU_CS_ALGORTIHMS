vize = int(input("vize notunuzu giriniz :"))
final = int(input("final notunuzu giriniz :"))

ortalama = vize*0.4 + final*0.6
print("ortalamanız:",ortalama)
if ortalama >= 50 :
    print("dersi geçtiniz")
else :
    print("dersi geçemediniz")
