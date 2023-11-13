# Pattern1
def pattern(rows):
    for i in range(1, rows + 1):
        for space in range(1, rows - i + 1):
            print("  ", end="")
        for star in range(1,2* i):
            print("* ", end="")
        print()
    print()
pattern(5) 

# Pattern2
for row in range(1, 13):
    for column in range(1, row):
        print("*", end="")
    print(" ", end="")
    for column in range(11, row, -1):
        print("*", end="")
    print()
print()

# Pattern3
for i in range(1, 11):
    for j in range(1, i + 1):
        k = i + j
        if k == 11:
            print(" ", end="")
        else:
            print("*", end="")
    print()
print()   

for i in range(1, 11):
    if i % 2 == 1:
        for j in range(1, 11):
            if j % 2 == 1:
                print(" ", end="")
            else:
                print("*", end="")
    else:
        for k in range(1, 11):
            if k % 2 == 1:
                print("*", end="")
            else:
                print(" ", end="")
    print()
