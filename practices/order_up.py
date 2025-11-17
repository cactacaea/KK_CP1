# KK 2nd Order Up! Practice
import time

# drink dictionary with 6+ keys
drinks = {
    "Iced Tea": 5.05,
    "Coffee": 5.25,
    "Hot Cocoa": 4.40,
    "Sparkling Water": 4.10,
    "Coke": 4.55,
    "Sprite": 4.55,
    "Rockbeer": 4.55,
    "Fanta": 4.55
}

# main course dictionary with 8 keys
main_courses = {
    "Chow Mein": 15.75,
    "Pho": 13.25,
    "Shrimp Fried Rice": 12.50,
    "Grilled Teriyaki Chicken": 15.75,
    "California Roll": 9.00,
    "Summer Roll": 10.00,
    "Vegas Roll": 11.00,
    "Spicy Yellowtail": 10.00
}

# side dishes dictionary with 10 keys
sides = {
    "Edamame": 5.65,
    "Spicy Edamame": 5.65,
    "Springrolls": 8.25,
    "Gyoza": 8.55,
    "Miso Soup": 4.75,
    "Egg Drop Soup": 4.75,
    "Squid Salad": 6.95,
    "House Salad": 5.75,
    "White Rice": 4.00,
    "Rocket Shrimps": 7.25
}

# order process FUNCTION with parameters for what dictionary is being checked and the final bill
def order(drinks, main_courses,sides):
    # empty final bill dictionary
    finished_bill = {}
    # while loops until the user enters a valid item from 1 of 3 menus

    while True:
        # prompt/input for the drink with a conditional checking if said input is in the drinks dictionary
        drink_choice = input("\nWhat drink would you like to order?:\n").title().strip()
        if drink_choice not in drinks:
            print("This item is not on the menu, re-order.")
        else: 
            # add item to bill and break loop
            finished_bill[drink_choice] = drinks[drink_choice]
            print("Your drink has been added to the bill.")
            break

    while True:
        # prompt/input for main course with a conditional checking if said input is in the main courses dictionary
        entree_choice = input("\nWhat would you like to order for your entree?:\n").title().strip()
        if entree_choice not in main_courses:
            print("This item is not on the menu, re-order.")
        else:
            # add item to bill and break loop
            finished_bill[entree_choice] = main_courses[entree_choice]
            print("Your main course has been added to the bill.")
            break

    while True:
        # 2 prompts for sides with a nested conditional/loop for the second side
        side_choice1 = input("\nWhat would you like to order for your first side dish?:\n").title().strip()
        if side_choice1 not in sides:
            print("This item is not on the menu, re-order.")
        else:
            # add first side to bill and tell user it's been added
            finished_bill[side_choice1] = sides[side_choice1]
            print("Your first side has been added to the bill.")
            while True:
                side_choice2 = input("\nWhat would you like to order for your second side dish?:\n").title().strip()
                if side_choice2 not in sides:
                    print("This item is not on the menu, re-order.")
                else: 
                    # add item to bill and break loop
                    finished_bill[side_choice2] = sides[side_choice2]
                    print("Your second side has been added to the bill.")
                    break
        break
    time.sleep(1)
    print("\nPlease hold as we calculate your due balance...")
    time.sleep(3)
    # RETURN MODIFIED BILL
    return finished_bill


# introduction explaining different actions: quit, tax, order, see each of the 3 menus
print("Welcome to your local sushi and noodle house!")
# tax
tax = input("\nTo begin, we must take note of tax to help the economy. What is the tax percentage where you live? Enter the plain number w/o a percent symbol.\nEx: 4.55\n")
# while LOOP so the user enters a valid option
while True:
    choice = input("\nType:\n'Quit' to stop ordering\n'Order' to place your order\n'Drinks' to view the drinks menu\n'Entrees' to view the main courses menu\n'Sides' to view the side dishes menu\n\nWhat would you like to do?:\n").lower().strip()
    # if user picks to quit, stop the code
    if choice == "quit":
        break
    # if user picks to see drinks menu, make a for LOOP showing the drinks menu
    elif choice == "drinks":
        print("\n - - - DRINKS - - - ")
        for key,value in drinks.items():
            print(f"{key}: ${value:.2f}")
        time.sleep(3.5)
    # if user picks the entrees menu, print the entrees menu nicely using a for LOOP
    elif choice == "entrees":
        print("\n - - - ENTREES - - - ")
        for key,value in main_courses.items():
            print(f"{key}: ${value:.2f}")
        time.sleep(3.5)
    # if user picks the sides menu, print the sides menu nicely using a for LOOP
    elif choice == "sides":
        print("\n - - - SIDE COURSES/APPETIZERS - - - ")
        for key,value in sides.items():
            print(f"{key}: ${value:.2f}")
        time.sleep(3.5)
    # if user picks to order, ask which menu they would like to order from
    elif choice == "order":
        final_bill_note = order(drinks,main_courses,sides)
        print(f"\n- - Final Order - -\n")
        for key,value in final_bill_note.items():
            print(f"{key}: ${value:.2f}")
        print(f"\nTotal: ${sum(final_bill_note.values())}")
        break

        # time.sleep(2)
        # while True:
        #     menu_choice = input("\n'Drinks': order a drink\n'Entrees': order a main dish\n'Sides': order 2 side dishes\nWhat menu would you like to order from?:\n").lower().strip()
        #     if menu_choice == "drinks":
        #         order(drinks,finished_bill)
        #         break
        #     elif menu_choice == "entrees":
        #         order(main_courses,finished_bill)
        #         break
        #     elif menu_choice == "sides":
        #         order(sides,finished_bill)
        #         break
        #     else:
        #         print("\nChoose a valid option >:(")
    # else, ask again
    else:
        print("\nInvalid choice, silly. Pick again")
        time.sleep(2)