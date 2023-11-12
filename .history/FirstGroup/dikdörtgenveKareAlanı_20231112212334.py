def area_of_square(side):

    area_of_square = side* side
    return area_of_square

def area_of_rectangle(long_side,short_side):

    area_of_rectangle = long_side*short_side   
    return area_of_rectangle

area = area_of_square(5)
area2 = area_of_rectangle(10,5) 
print("Area of square: ",area)
print("Area of rectangle: ",area2)
