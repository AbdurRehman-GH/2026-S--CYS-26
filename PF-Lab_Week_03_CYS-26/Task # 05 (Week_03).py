def calculate_gpa():
    subjects = int(input("Enter the number of subjects: "))

    total_grade_points = 0
    total_credit_hours = 0
    
    for i in range(subjects):
        print("Subject", i+1)
        
        grade_point = float(input("Enter Grade Point: "))
        credit_hours = int(input("Enter Credit Hours: "))
        total = grade_point * credit_hours
        total_grade_points = total_grade_points + total
        total_credit_hours = total_credit_hours + credit_hours
        gpa = total_grade_points / total_credit_hours
    
    print("Your GPA for this semester is:", gpa)
calculate_gpa()