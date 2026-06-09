for i in range(1, 8):
    if i <= 4:
        stars = i
    else:
        stars = 8 - i
    for j in range(1, stars + 1):
        print("*", end=" ")
    print()