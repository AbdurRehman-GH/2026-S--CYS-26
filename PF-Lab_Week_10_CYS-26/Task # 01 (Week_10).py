stu_dic = {}

a = int(input("Obtained Marks: "))
b = int(input("Total Marks: "))
c = a / b * 100
if c == 0:
    print("Invalid")
elif a > b:
    print("Invalid")
else:
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
students = 1
total_stu = int(input("Enter number of students: "))
for i in range(total_stu+1):
    name = input("Enter student's name: ")
    marks = input("Enter student's marks: ")
    stu_list = [(name,marks)]
    for key, value in stu_list:
        stu_dic.setdefault(key, []).append(value)
students += 1
print(stu_dic)