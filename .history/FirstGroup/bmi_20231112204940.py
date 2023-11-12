def bmi(kilo,boy):
# Beden Kitle Endeksi (BMI) hesaplama formülü
    bmi = kilo / (boy ** 2)
    return bmi

bmi(kilo,boy)
# Sonucu ekrana yazdır
print("Beden Kitle Endeksiniz (BMI):", bmi)

# BMI değerini yorumlayarak sonucu ekrana yazdır
if bmi < 18.5:
    print("Zayıfsınız.")
elif 18.5 <= bmi < 24.9:
    print("Normal kilodasınız.")
elif 25 <= bmi < 29.9:
    print("Fazla kilolusunuz.")
else:
    print("Obezsiniz.")
