//Pattern1
for satir in range(1, 13):
    for sutun in range(1, satir):
        print("*", end="")
    print(" ", end="")
    for sutun in range(11, satir, -1):
        print("*", end="")
    print()
//Pattern2
for i in range(1, 11):
    for j in range(1, i + 1):
        k = i + j
        if k == 11:
            print(" ", end="")
        else:
            print("*", end="")
    print()
//Pattern3
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
