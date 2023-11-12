side =int(input("Enter one side of the square: "))
area_of_square = side* side
print("Area of square: ",area_of_square)
sides = input("Enter the long and short sides of the rectangle:\n")
list = sides.split(" ")    
long_side = int(list[0])
short_side = int(list[1]) 
area_of_rectangle = long_side*short_side   
print("Area of rectangle: ",area_of_rectangle)
