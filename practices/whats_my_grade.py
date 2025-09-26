# KK 2nd What is My Grade Practice

# print("Welcome. Please type 'finish' to calculate your average.")
# print("TIP: Enter a decimal. Can be rounded.\n")
# while True:
#     grade = input("Enter your grade percentage to convert to a letter:\n")
#     collected_grades = []
    
#     if grade == "finish":
#         for grades in collected_grades:
#             avg_grade = avg_grade+grades
#         avg_grade = avg_grade/len(collected_grades)
#         if grade >= 90:
#             if grade == 100:
#                 print("Lovely! Your grade is a perfect 100% A.")
#             elif grade > 100:
#                 print("Wow, you worked hard for extra credit; you have an A+!")
#             else:
#                 print("You have an A.")
#         elif grade >= 80 and grade < 90:
#             print("You have a B")
#         break
#     else:
#         grade = int(grade)
#         collected_grades.append(grade)

# print("Welcome. Please type 'finish' to calculate your average.")
# print("TIP: Enter a decimal. Can be rounded.\n")
# while True:
#     grade = input("Enter your grade percentage to convert to a letter:\n")
#     collected_grades = []

# what's my grade 2,0

grade = float(input("What's your grade? HINT; enter a decimal:\n"))
#a
if grade >= 90:
    if grade == 100:
        print(f"Lovely! Your grade is a perfect 100% A.")
    elif grade > 100 and grade < 102:
        print(f"{grade}%! You worked hard for extra credit and you have an A!")
    elif grade >= 102:
        print(f"{grade}%? Did you cheat or are you just a genius?")
    elif grade >= 90 and grade < 92:
        print(f"{grade}% is an A-")
    else:
        print(f"{grade}%? You have an A")
#b
elif grade < 90 and grade >= 80:
    if grade < 90 and grade >=87:
        print(f"{grade}% is a B+")
    elif grade < 87 and grade >=82:
        print(f"{grade}% is a B")
    else:   
        print(f"{grade}% is a B-")
#c
elif grade < 80 and grade >= 70:
    if grade < 80 and grade >=77:
        print(f"{grade}% is a C+")
    elif grade < 77 and grade >= 72:
        print(f"{grade}% is a C")
    else:
        print(f"{grade}% is a C-")
#d
elif grade < 70 and grade >= 55:
    if grade < 70 and grade >=67:
        print(f"{grade}% is a D+")
    elif grade < 67 and grade >= 64:
        print(f"{grade}% is a D")
    else:
        print(f"{grade}% is a D-, you might want to improve that")
elif grade < 55 and grade > 0:
    print(f"{grade}% IS AN F! GO STUDY!")
else:
    print("That literally takes skill...")

