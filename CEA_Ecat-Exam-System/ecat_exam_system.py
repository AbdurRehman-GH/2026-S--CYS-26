
questions = [
            {"Question": "What does CPU stand for?",
                "Choices": {"A": "Central Process Unit",
                    "B": "Central Processing Unit",
                    "C": "Computer Processing Unit",
                    "D": "Control Processing Unit"},
                "Answer": "B"},

            {"Question": "What is Square root of 1089?",
            "Choices": {"A": "31",
                        "B": "32",
                        "C": "33",
                        "D": "34"},
            "Answer": "C"},

            {"Question": "Choose the correct spelling.",
            "Choices": {"A": "Recieve",
                        "B": "Receive",
                        "C": "Receeve",
                        "D": "Recive"},
            "Answer": "B"},

            {"Question": "Which symbol is used for comments in Python?",
            "Choices": {"A": "//",
                        "B": "@",
                        "C": "*",
                        "D": "#"},
            "Answer": "D"},

            {"Question": "Which of the following is Noble Gas?",
            "Choices": {"A": "Li",
                        "B": "N",
                        "C": "Ar",
                        "D": "S"},
            "Answer": "C"},

            {"Question": "Which of the following states resistance?",
            "Choices": {"A": "Coulomb's Law",
                        "B": "Ohm's Law",
                        "C": "Hooke's Law",
                        "D": "Snell's Law"},
            "Answer": "B"},

            {"Question": "Number of moles of solute dissolved in one liter of solution?",
            "Choices": {"A": "Normality(N)",
                        "B": "Molality(m)",
                        "C": "Molarity(M)",
                        "D": "None"},
            "Answer": "C"},

            {"Question": "Solve 24÷8+2.",
            "Choices": {"A": "5",
                        "B": "24/10",
                        "C": "26/8",
                        "D": "20"},
            "Answer": "A"},

            {"Question": "BANAL means:",
            "Choices": {"A": "Philosophical",
                        "B": "Original",
                        "C": "Dramatic",
                        "D": "Commonplace"},
            "Answer": "D"},

            {"Question": "Unit of Electric Field is:",
            "Choices": {"A": "V/m",
                        "B": "N/C",
                        "C": "N/V",
                        "D": "Both A & B"},
            "Answer": "D"}
        ]

all_results = []

def admin_menu():
     while True:
          print("\nADMIN MENU")
          print("1. View Questions")
          print("2. Add Questions")
          print("3. Delete Questions")
          print("4. View Results")
          print("5. Statistics")
          print("6. Logout")

          choice = int(input("Enter your choice: "))
          if choice == 1:
               print("\nALL QUESTIONS")
               for i, q in enumerate(questions, start=1):
                    print("\nQuestion", i)
                    print(q["Question"])
                    print("A.", q["Choices"]["A"])
                    print("B.", q["Choices"]["B"])
                    print("C.", q["Choices"]["C"])
                    print("D.", q["Choices"]["D"])
                    print("Correct Answer:", q["Answer"])

          elif choice == 2:
               print("\nADD NEW QUESTIONS")
               question = input("Enter a Question: ")
               op_a = input("Enter Option A: ")
               op_b = input("Enter Option B: ")
               op_c = input("Enter Option C: ")
               op_d = input("Enter Option D: ")
               correct_ans = input("Enter correct Answer: ").upper()

               new_ques = {"Question": question,
                           "Choices": {"A": op_a,
                                       "B": op_b,
                                       "C": op_c,
                                       "D": op_d},
                            "Answer": correct_ans}
               questions.append(new_ques)
               print("Question Added Successfully!")

          elif choice == 3:
               print("\nDELETE QUESTION")
               for i, q in enumerate(questions, start=1):
                    print(i, ".", q["Question"])
               delete_num = int(input("Enter Question Number to Delete: "))
               if delete_num >= 1 and delete_num <= len(questions):
                    questions.pop(delete_num - 1)
                    print("Question Deleted Successfully!")
               else:
                    print("Invalid Question Number!")

          elif choice == 4:
               print("\nSTUDENT RESULTS")
               if len(all_results) == 0:
                    print("No Reults Found!")
               else:
                    for r in all_results:
                         print("\nName:", r["Name"])
                         print("Score:", r["Score"])
                         print("Percentage:", r["Percentage"])
                         print("Grade:", r["Grade"])

          elif choice == 5:
               print("\nSTATISTICS")
               if len(all_results) == 0:
                    print("No Results Available!")
               else:
                    highest = all_results[0]["Score"]
                    lowest = all_results[0]["Score"]
                    total = 0
                    for r in all_results:
                         total += r["Score"]
                         if r["Score"] > highest:
                              highest = r["Score"]
                         if r["Score"] < lowest:
                              lowest = r["Score"]
                    average = total / len(all_results)
                    
                    print("Highest Score: ", highest)
                    print("Lowest Score: ", lowest)
                    print("Average Score: ", average)
                    print("Total Students: ", len(all_results))

          elif choice == 6:
               print("Logging Out...!")
               break
          else:
               print("Invalid Choice!") 

def admin_portal():
    attempts = 0
    while attempts < 3:
        print("Welcome to Admin Portal!")
        a = input("Enter username: ")
        b = input("Enter password: ")
        if a == "uet@admin" and b == "admin123":
            print("Login Success!")
            admin_menu()
            return True
        else:
            attempts += 1
            print("Invalid Credentials")
            print("Attempts Left: ", 3 - attempts)
        if attempts == 3:
            print("Too many wrong attempts!")
            return False

def student_portal():
    attempts = 0
    while attempts < 3:
        print("Welcome to Student Portal!")
        student_name = input("Enter your name: ")
        password = input("Enter exam password: ")
        if password == "ECAT-CYS":
            print("Login Success!")
            print("\nStart the Exam!")
            start_exam(student_name)
            return True
        else:
            attempts += 1
            print("Inavalid Credentials")
            print("Attempts Left: ", 3 - attempts)
        if attempts == 3:
            print("Too many wrong attempts!")
            return False

def start_exam(student_name):
    correct = 0
    wrong = 0
    score = 0
    skip = 0
    for q in questions:
                print()
                print(q["Question"])
                print()
                print("A.", q["Choices"]["A"])
                print("B.", q["Choices"]["B"])
                print("C.", q["Choices"]["C"])
                print("D.", q["Choices"]["D"])
                answer = input("Enter your answer: ").upper()
                print()
                print("You entered: ", answer)
                if answer == q["Answer"]:
                    score += 4
                    correct += 1
                elif answer == "S":
                    score += 0
                    skip += 1
                elif answer == "SUBMIT":
                    break
                else:
                    score -= 1
                    wrong += 1
                score = max(0, score)   
                percentage = (score * 100) / total_poss_marks
    total_questions = len(questions)
    total_poss_marks = total_questions * 4
    percentage = (score * 100) / total_poss_marks
    score = max(0, score)   
    print()
    print("Marks Obtained: ", score)
    print("Percentage: ", percentage, "%")
    if percentage >= 80:
            grade = "EXCELLENT"
    elif percentage >= 65:
            grade = "GOOD"
    elif percentage >= 50:
            grade = "AVERAGE"
    else:
            grade = "BELOW AVERAGE"
    print("Grade: ", grade)
    print("Correct Answers: ", correct)
    print("Wrong Answers: ", wrong)
    print("Skipped Answers: ", total_questions - (correct + wrong))
    result = {"Name": student_name,
              "Score": score,
              "Percentage": percentage,
              "Grade": grade}
    all_results.append(result) 

while True:
    print("\tECAT EXAM SYSTEM\n")
    print("1.Admin Portal")
    print("2.Student Portal")
    print("3.Exit")

    a = int(input("Enter your choice: "))
    if a == 1:
        admin_portal()
        break
    elif a == 2:
        student_portal()
        # break
    elif a == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid Choice")