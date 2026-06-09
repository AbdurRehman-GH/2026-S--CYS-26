def fahrenheit_to_celsius(f):
    c = (f - 32) * 5/9
    print("Temperature in Celsius is: ", c)

def celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    print("Temperature in Fahrenheit is: ", f)

print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    temp = float(input("Enter temperature in Fahrenheit: "))
    fahrenheit_to_celsius(temp)
elif choice == 2:
    temp = float(input("Enter temperature in Celsius: "))
    celsius_to_fahrenheit(temp)
else:
    print("Invalid choice")