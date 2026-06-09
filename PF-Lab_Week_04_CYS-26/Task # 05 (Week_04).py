def power(base, exponent=2):
    return base ** exponent

num = int(input("Enter a base number: "))

result1 = power(num)
print("Result without providing exponent:", result1)

exp = int(input("Enter exponent: "))
result2 = power(num, exp)
print("Result with provided exponent (",exp,") :", result2)