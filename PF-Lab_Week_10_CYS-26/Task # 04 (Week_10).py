# 01
for i in range(1, 10):
    for j in range(1, i+1):
        print("*",end="")
    print()


# 02
stars = 10
for i in range(stars):
    spaces = stars - i - 1
    print(' ' * spaces + '*' * (2*i + 1))
