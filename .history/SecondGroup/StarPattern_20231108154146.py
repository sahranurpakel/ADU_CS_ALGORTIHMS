//Pattern1
rows = int(input("satir sayisi: "))
for i in range(1, rows + 1):
    for space in range(1, rows - i + 1):
        print("  ", end="")
    k = 0
    while k != 2 * i - 1:
        print("* ", end="")
        k += 1
    print()

//Pattern2
for satir in range(1, 13):
    for sutun in range(1, satir):
        print("*", end="")
    print(" ", end="")
    for sutun in range(11, satir, -1):
        print("*", end="")
    print()
//Pattern3

for i in range(1, 11):
    for j in range(1, i + 1):
        k = i + j
        if k == 11:
            print(" ", end="")
        else:
            print("*", end="")
    print()
//Pattern4

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
