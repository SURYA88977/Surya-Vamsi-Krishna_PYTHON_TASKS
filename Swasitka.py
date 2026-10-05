for i in range(1, 8):
    for j in range(1, 8):
        if ((j == 1 and i <= 4) or
            i == 4 or
            (j == 7 and i >= 4) or
            (i == 1 and j >= 4) or
            j == 4 or
            (i == 7 and j <= 4)):
            print("*", end="")
        else:
            print(" ", end="")
    print()