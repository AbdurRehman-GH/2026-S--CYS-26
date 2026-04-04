a = int(input("Obtained Marks: "))
b = int(input("Total Marks: "))
c = a / b * 100
print(c)
if c >= 95:
    print("A+")
elif c >= 90:
    print("A")
elif c >= 85:
    print("A-")
elif c >= 80:
    print("B+")
elif c >= 75:
    print("B")
elif c >= 70:
    print("B-")
elif c >= 65:
    print("C+")
elif c >= 60:
    print("C")
elif c >= 55:
    print("C-")
elif c >= 50:
    print("D")
elif c <= 49:
    print("F")