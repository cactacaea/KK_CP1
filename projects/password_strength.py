# KK 2nd Password Strength Checker Project

import random
import string
# intro/greeting
print("Greetings! Welcome to the program that checks your password strength")

# list of symbols/unique characters
characters = ["!","&","*","@","$","%","~","#","?","(","+","_"]
start = '\033[1m'
end = '\033[0m'

# loop until user enters a valid password
while True:
    # strength score variable
    strength_score = 0
    # 5 false variables for requirements
    length_requirement = False
    upper_requirement = False
    lower_requirement = False
    numbers_requirement = False
    symbol_requirement = False
    # user input asking for a password with .strip()
    usr_password = input("\nPlease create a password:\n").strip()
    # password length determined
    password_length = len(usr_password)
    if password_length >= 8:
        # set length variable to true/false
        length_requirement = True
        # increase strength score if it meets requirements
        strength_score += 1
            
    # for loop checking user_input/password for uppercase letters using .isupper()
    for i in usr_password:
        if i.isupper():
        # set uppercase variable to true/false
            upper_requirement = True
        # increase strength score if it meets requirements
            strength_score += 1
            break
    # for loop checking password for lowercase letter{end}s using .islower()
    for i in usr_password:
        if i.islower():
        # set lowercase var to true/false
            lower_requirement = True
        # increase strength score if it meets requirements
            strength_score += 1
            break
    # for loop checking password for numbers using .isdigit()
    for i in usr_password:
        if i.isdigit():
        # set numbering var to true/false
            numbers_requirement = True
        # increase strength score if it meets requirements
            strength_score += 1
            break
    # for loop checking password for symbols/special chars using .punctuation()
    for i in usr_password:
        if i in string.punctuation:
        # set special character variable to true/false
            symbol_requirement = True
        # increase strength score if it meets requirements
            strength_score += 1
            break
    # CONDITIONS
    # if strength is 5, display very strong password and end the code
    if strength_score == 5:
        print(f"\n{start}Strength Score: 5/5\nPassword Strength: Very Strong\nYou made a great password!{end}")
        break
    # otherwise strength is 4, display fairly strong
    elif strength_score == 4:
        print(f"\n{start}Strength Score: 4/5\nPassword Strength: Fairly Strong, could use improvement{end}")
        # if len == False
        if length_requirement == False:
            # suggest adding 8-user_input more characters
            print(f"\n{start}Try adding {8-password_length} more characters!{end}")
        # if upper == False
        if upper_requirement == False:
            # suggest random letter change to capital
            print(f"\n{start}Try changing a letter in your password to a capital letter!{end}")
        # if lower == False
        if lower_requirement == False:
            # suggest random letter change to a lowercase
            print(f"\n{start}Try changing a letter in your password to a lowercase letter!{end}")
        # if numbers == False
        if numbers_requirement == False:
            # suggest adding random number 1-100 to the end
            num_suggestion = random.randint(1,100)
            print(f"\n{start}Try adding {num_suggestion} to the end or to the beginning of your password!{end}")
        # if characters == False
        if symbol_requirement == False:
            # suggest a random character to the end/beginning of the password from an existing list of symbols
            char_suggestion = random.choice(characters)
            print(f"\n{start}Try adding {char_suggestion} to the end or to the beginning of your password!{end}")
    # otherwise strength is 3, display decent password/needs improvement
    elif strength_score == 3:
        print(f"\n{start}Strength Score: 3/5\nPassword Strength: Decent, would need improvement")
        # if len == False
        if length_requirement == False:
            # suggest adding 8-user_input more characters
            print(f"\n{start}Try adding {8-password_length} more characters!{end}")
        # if upper == False
        if upper_requirement == False:
            # suggest random letter change to capital
            print(f"\n{start}Try changing a letter in your password to a capital letter!{end}")
        # if lower == False
        if lower_requirement == False:
            # suggest random letter change to a lowercase
            print(f"\n{start}Try changing a letter in your password to a lowercase letter!{end}")
        # if numbers == False
        if numbers_requirement == False:
            # suggest adding random number 1-100 to the end
            num_suggestion = random.randint(1,100)
            print(f"\n{start}Try adding {num_suggestion} to the end or to the beginning of your password!{end}")
        # if characters == False
        if symbol_requirement == False:
            # suggest a random character to the end/beginning of the password from an existing list of symbols
            char_suggestion = random.choice(characters)
            print(f"\n{start}Try adding {char_suggestion} to the end or to the beginning of your password!{end}")
    # otherwise strength is 2, display weak password
    elif strength_score == 2:
        print(f"\n{start}Strength Score: 2/5\nPassword Strength: Weak. You need improvement")
        # if len == False
        if length_requirement == False:
            # suggest adding 8-user_input more characters
            print(f"\n{start}Try adding {8-password_length} more characters!{end}")
        # if upper == False
        if upper_requirement == False:
            # suggest random letter change to capital
            print(f"\n{start}Try changing a letter in your password to a capital letter!{end}")
        # if lower == False
        if lower_requirement == False:
            # suggest random letter change to a lowercase
            print(f"\n{start}Try changing a letter in your password to a lowercase letter!{end}")
        # if numbers == False
        if numbers_requirement == False:
            # suggest adding random number 1-100 to the end
            num_suggestion = random.randint(1,100)
            print(f"\n{start}Try adding {num_suggestion} to the end or to the beginning of your password!{end}")
        # if characters == False
        if symbol_requirement == False:
            # suggest a random character to the end/beginning of the password from an existing list of symbols
            char_suggestion = random.choice(characters)
            print(f"\n{start}Try adding {char_suggestion} to the end or to the beginning of your password!{end}")
    # otherwise strength is 1, display extremely weak password
    elif strength_score == 1:
        print(f"\n{start}Strength Score: 1/5\nPassword Strength: Extremely Weak. You need improvement desperately.")
        # if len == False
        if length_requirement == False:
            # suggest adding 8-user_input more characters
            print(f"\n{start}Try adding {8-password_length} more characters!{end}")
        # if upper == False
        if upper_requirement == False:
            # suggest random letter change to capital
            print(f"\n{start}Try changing a letter in your password to a capital letter!{end}")
        # if lower == False
        if lower_requirement == False:
            # suggest random letter change to a lowercase
            print(f"\n{start}Try changing a letter in your password to a lowercase letter!{end}")
        # if numbers == False
        if numbers_requirement == False:
            # suggest adding random number 1-100 to the end
            num_suggestion = random.randint(1,100)
            print(f"\n{start}Try adding {num_suggestion} to the end or to the beginning of your password!{end}")
        # if characters == False
        if symbol_requirement == False:
            # suggest a random character to the end/beginning of the password from an existing list of symbols
            char_suggestion = random.choice(characters)
            print(f"\n{start}Try adding {char_suggestion} to the end or to the beginning of your password!{end}")