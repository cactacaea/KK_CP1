# KK 2nd, Factorial Calculator // Practice

# defining all the user's inputs to get the orginal/answer
# def factorial (user)
def factorial(user_input):
# for x
    ## have a number variable to start at (1)
    num = 1
    ## change to for x in range(1,num+1?) to iterate over the range of the factorial
    for x in range(1,user_input+1):
        ## multiply num and iterated numbers, assigning num the value in the process
        num *= x
    ## return number after for loop finds factorial solution
    return num

# getting the user's information
# user = input("hello, please put in your numbers")

print("Greetings!")
# while True:
while True:
    # if user = not a float(int)
    ## change to using try/except to make life easier
    ## try printing number, calling the factorial function
    try:
        ## change to an input of only 1 number since we don't need more values, nad inside a loop for error handling
        user_input = int(input("\nEnter a number to find the factorial of it:\n"))
        print(f"\n{user_input}! = {factorial((user_input))}")
    # print("put a whole number")
    # elif user = is a float
    ## except valueerror because the user needs to enter a valid number, rather than using if/else
    except ValueError:
        print("\nEnter an integer..")