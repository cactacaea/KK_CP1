# KK 2nd Average Grade Practice

while True: # repeats until user enters a number
    grade_inputs = input("How many classes are you taking?:\n")
    collected_grades = []
    if grade_inputs.isdigit(): # checks if input was a number
        converted_classes = int(grade_inputs)
        #print(converted_classes)

        for period in range(converted_classes):

            while True: # continues asking for a valid input
                classes_number = input(f"What is your grade for period {period+1}?: ")
                
                if classes_number.isdigit():
                    collected_grades.append(int(classes_number))
                    break
                else:
                    print("Input a number, silly.")

        average_grade = 0
        for grades in collected_grades:
            average_grade=average_grade+grades
        average_grade=average_grade/len(collected_grades)
        print(average_grade)
            
        print(f"Your average grade is: {average_grade}")
        break
    else:
        print("Wrong data type! Please input a number.")

# avg grade 2.0

# period1 = float(input("What is your grade for your first class?: "))
# period2 = float(input("What is your grade for your second class?: "))
# period3 = float(input("What is your grade for your third class?: "))
# advisory = float(input("What is your grade for your advisory class?: "))
# period6 = float(input("What is your grade for your sixth class?: "))
# period7 = float(input("What is your grade for your seventh class?: "))
# period8 = float(input("What is your grade for your eighth class?: "))

# average = ((period1+period2+period3+advisory+period6+period7+period8)/7)
# print("Your average grade is: ")
# print(round(average,2))