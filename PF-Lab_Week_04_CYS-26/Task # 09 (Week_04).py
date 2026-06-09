def average(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    avg = total / len(numbers)
    print("Average is:", avg)

average(10, 15, 20)