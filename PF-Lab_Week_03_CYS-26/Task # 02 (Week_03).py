num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

large = lambda a, b: a if a > b else b
result = large(num1, num2)
print("Large number is: ", result)

r = int(input("Enter the range for table: "))

def table(n, range_value):
    for i in range(1, range_value + 1):
        print(f"{n} x {i} = {n*i}")

table(result, r)