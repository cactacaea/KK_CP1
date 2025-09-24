# KK 2nd What is My Grade Practice

print("Welcome. Please type 'finish' to calculate your average.")
print("TIP: Enter a decimal. Can be rounded.\n")
while True:
    grade = input("Enter your grade percentage to convert to a letter:\n")
    collected_grades = []
    
    if grade == "finish":
        grade = int(grade)
        collected_grades.append(grade)
        if grade >= 90:
            if grade == 100:
                print("Lovely! Your grade is a perfect 100% A.")
            elif grade > 100:
                print("Wow, you worked hard for extra credit; you have an A+!")
            else:
                print("You have an A")
        elif grade >= 80 and grade < 90:
            print("You have a B")
        break
    else:
        print("What?")