# KK 2nd, Flexible Calculator // Practice


# RETURN VALUE BACK TO FUNCTION WHEN PRINTING
# sum function w/ args parameter
# def sum(*values):


# # average function w/ args parameter
# def average():

# # maximum function w/ args parameter
# def maximum():

# # minimum function w/ args parameter
# def minimum():

# # multiplying/product function w/ args parameter
# def product():


# greet user with available operations 
print("Greetings! This is a flexible calculator. The available operations are:\nSum\nAverage\nMax/Maximum\nMin/Minimum\nProduct\n")
# input for what operation user would like to use 
operation_opt = input("What operation would you like to perform?:\n")
print("\nEnter the numbers you would like to perform the operation on; type 'stop' to calculate.")
# while LOOP for input of numbers until the user decides to stop
chosen_numbers = []
while True:
    # append to a list after each number
    num_choice = input("Number: ")
    chosen_numbers.append(num_choice)
    if num_choice == "stop":
        break
    else:
        continue

# conditionals checking what the user gave and calling the designated function depending on the operation
# PRINT RETURNED VALUE BY MAKING THE FUNCTION CALL BE A VARIABLE
