kenar =int(input("Enter one side of the square: "))
karenin_alani = kenar* kenar
print("karenin alanı: ", karenin_alani)
kenarlar = int(input("Enter the long and short sides of the rectangle:\n"))  
liste = kenarlar.split(" ")    
uzun_kenar = int(liste[0])
kisa_kenar = int(liste[1]) 
dikdörtgenin_alani = liste[0]*liste[1]   
print("Dikdörtgenin alanı: ",dikdörtgenin_alani)
