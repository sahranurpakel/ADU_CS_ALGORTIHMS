def bmi(kilo,boy):
# Beden Kitle Endeksi (BMI) hesaplama formülü
    bmi = kilo / (boy ** 2)
    return bmi

bmi_sonuc = bmi(55,1.58)
# Sonucu ekrana yazdır
print("Beden Kitle Endeksiniz (BMI):", bmi_sonuc)

# BMI değerini yorumlayarak sonucu ekrana yazdır
if bmi_sonuc < 18.5:
    print("Zayıfsınız.")
elif 18.5 <= bmi_sonuc < 24.9:
    print("Normal kilodasınız.")
elif 25 <= bmi_sonuc < 29.9:
    print("Fazla kilolusunuz.")
else:
    print("Obezsiniz.")

