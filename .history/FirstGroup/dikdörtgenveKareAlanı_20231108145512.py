kenar =int(input("Enter one side of the square: "))
print("karenin alanı: " + str(kenar * kenar))
kenarlar = int(input("Enter the long and short sides of the rectangle:\n"))  
liste = kenarlar.split(" ")    
uzun_kenar = int(liste[0])
kisa_kenar = int(liste[1])      
print("Dikdörtgenin alanı: " + str(liste[0]*liste[1]))
input("Press Enter to exit...")