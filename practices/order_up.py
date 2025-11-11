# KK 2nd Order Up! Practice

# drink dictionary with 6 keys
drinks = {
    ""
}

# main course dictionary with 8 keys
main_courses = {
    "Plain Pasta": 4.30,
    "Spinach Pasta": 4.49,
    "Pizza Pasta": 4.99,
    "Alfredo Pasta": 4.99
}

# side dishes dictionary with 10 keys
sides = {
    "Tater Tots": 2.00
}

# order process FUNCTION with parameters for what dictionary is being checked and the entre
    # finished dictionary (empty in the beginning, added keys/values after input)
    # while LOOP until the user enters a valid item from 1 of 3 menus
        # prompt/input
        # if input isn't in drink dictionary, ask again
        # else break out if it's valid

    # RETURN MODIFIED FINISHED DICITONARY

# introduction explaining what to type for different actions: quit, drinks, main course, sides, tax
print("Greetings! Type:\n'Quit' to stop ordering\n'Drinks' to order a drink and see the drinks menu\n'Entrees' to order your main course and see the entree menu\n'Sides' to order 2 side dishes and see the menu")
tax = input("\nFirst off, we must take note of tax to help the economy. What is the tax percentage where you live?:\n")
# call order function 3 times w/ each menu as a parameter