def total(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print("Sum of numbers: ", sum)

total(15, 10, 25)
total(4, 6, 8)