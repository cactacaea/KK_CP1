# KK 2nd, Flexible Calculator // Practice


# RETURN VALUE BACK TO FUNCTION WHEN PRINTING
# sum function w/ args parameter
def summed(*values):
    print(f"\nCalculating the sum of:")
    for value in values:
        print(f"{value:.1f},",end=" ")
    print(" ")
    return sum(values)

# average function w/ args parameter
def average(*values):
    print(f"\nCalculating the average of:")
    for value in values:
        print(f"{value:.1f},",end=" ")
    print(" ")
    try:
        return sum(values)/len(values)
    except ZeroDivisionError:
        print("You didn't provide any numbers.")

# maximum function w/ args parameter
def maximum(*values):
    print(f"\nFinding the maximum out of:")
    for value in values:
        print(f"{value:.1f},",end=" ")
    print(" ")
    return max(values)

# minimum function w/ args parameter
def minimum(*values):
    print(f"\nFinding the minimum out of:")
    for value in values:
        print(f"{value:.1f},",end=" ")
    print(" ")
    return min(values)

# multiplying/product function w/ args parameter
def product(*values):
    print(f"\nCalculating the product of:")
    for value in values:
        print(f"{value:.1f},",end="")
    print(" ")
    multiplied_nums = 1
    for value in values:
        multiplied_nums *= value
    return multiplied_nums

# greet user with available operations 
print("Greetings! This is a flexible calculator. The available operations are:\nSum\nAverage\nMax/Maximum\nMin/Minimum\nProduct\n")
while True:
    available_operations = ["sum","average","max","maximum","min","minimum","product"]
    # input for what operation user would like to use 
    while True:
        operation_opt = input("What operation would you like to perform?:\n").lower().strip()
        if operation_opt in available_operations:
            break
        else:
            print("\nTry again. Type your choice of operation CORRECTLY.")
    print("\nEnter the numbers you would like to perform the operation on; type 'stop' to calculate.\n")
    # while LOOP for input of numbers until the user decides to stop
    chosen_numbers = []
    while True:
        # append to a list after each number, use try/except to append it if it's a number ONLY
        num_choice = input("Number: ").lower().strip()
        if num_choice == "stop":
            break
        try:
            chosen_numbers.append(float(num_choice))
        except ValueError:
            print("Hey. No. Enter a valid number.")

    # conditionals checking what the user gave and calling the designated function depending on the operation, unpacking the list with numbers
    # PRINT RETURNED VALUE BY MAKING THE FUNCTION CALL BE A VARIABLE
    if operation_opt == "sum":
        result = summed(*chosen_numbers)
    elif operation_opt == "average":
        result = average(*chosen_numbers)
    elif operation_opt in ("max","maximum"):
        result = maximum(*chosen_numbers)
    elif operation_opt in ("min","minimum"):
        result = minimum(*chosen_numbers)
    elif operation_opt == "product":
        result = product(*chosen_numbers)
    else:
        print("You entered an invalid operation. Retry!!")

    print(f"Result: {result}!")

    continue_question = input("\n(Yes/No) Would you like to complete another calculation?:\n").lower().strip()
    if continue_question == "yes":
        print(" ")
        continue
    elif continue_question == "no":
        print("\nClosing calculator...")
        break
    else:
        print("\nYou didn't pick 'yes' or 'no' therefore the calculator will be turned off. Goodbye!")
        break
