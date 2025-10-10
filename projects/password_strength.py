# KK 2nd Password Strength Checker Project

# intro/greeting
# strength score variable
# 5 false variables for requirements

# loop until user enters a valid password
    # user input asking for a password with .strip()

    # for loop checking user_input/password length using len()
        # set length variable to true/false
        # increase strength score if it meets requirements
    # for loop checking user_input/password for uppercase letters using .isupper()
        # set uppercase variable to true/false
        # increase strength score if it meets requirements
    # for loop checking password for lowercase letters using .islower()
        # set lowercase var to true/false
        # increase strength score if it meets requirements
    # for loop checking password for numbers using .isdigit()
        # set numbering var to true/false
        # increase strength score if it meets requirements
    # for loop checking password for symbols/special chars using .punctuation()
        # set special character variable to true/false
        # increase strength score if it meets requirements
    # CONDITIONS
    # if strength is 5, display very strong password and end the code
    # otherwise strength is 4