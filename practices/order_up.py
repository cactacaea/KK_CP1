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

# empty final bill dictionary
finished_bill = {}

# order process FUNCTION with parameters for what dictionary is being checked and the final bill
def order(dictionary,finished_bill):
    # while LOOP until the user enters a valid item from 1 of 3 menus
    while True:
        # prompt/input
        food_decision = input("What would you like to order?:\n")
        # if input isn't in dictionary, ask again
        if food_decision not in dictionary:
            print("Item isn't in menu, re-order:\n")
        # else break out if it's valid
        else:
            finished_bill
            break

    # RETURN MODIFIED BILL


# introduction explaining different actions: quit, tax, order, see each of the 3 menus
print("Welcome to Fredbear's Family Diner!")
# tax
tax = input("\nTo begin, we must take note of tax to help the economy. What is the tax percentage where you live? Enter the plain number w/o a percent symbol\nEx: 4.55\n")
# while LOOP so the user enters a valid option
while True:
    choice = input("Type:\n'Quit' to stop ordering\n'Order' to place your order\n'Drinks' to view the drinks menu\n'Entrees' to view the main courses menu\n'Sides' to view the side dishes menu\n\nWhat would you like to do?:\n").lower().strip()
    # if user picks to quit, stop the code
    if choice == "quit":
        break
    # if user picks to see drinks menu, make a for LOOP showing the drinks menu
    elif choice == "drinks":

    # if user picks the entrees menu, print the entrees menu nicely using a for LOOP
    elif choice == "entrees":

    # if user picks the sides menu, print the sides menu nicely using a for LOOP
    elif choice == "sides":

    # if user picks to order, ask which menu they would like to order from
    elif choice == "order":
        while True:
            menu_choice = input("'Drinks': order a drink\n'Entrees': order a main dish\n'Sides': order 2 side dishes\nWhat menu would you like to order from?:\n").lower().strip()
            if menu_choice == "drinks":
                order(drinks,finished_bill)
            elif menu_choice == "entrees":
                order(main_courses,finished_bill)
            elif menu_choice == "sides":
                order(sides,finished_bill)
            else:
                print("Choose a valid option >:(")
    # else, ask again
    else:
        print("Invalid choice, silly. Pick again")