# KK 2nd Basic Calculator Practice

# add
# subtract
# multiply
# divide
# intdiv
# mod 
# exponents

start = '\033[1m'
end = '\033[0m'

print("Greetings! Type 'out' if you would like to stop.\n")
while True:
    # 1st number
    num1 = input("Please give me a number:\n")
    if num1 == "out":
        print("Stopping...")
        break
    elif num1 != float(num1) and num1 != int(num1):
        print("Input a valid number!\n")
    else:
        # 2nd number
        num2 = input("Please give me a second number:\n")
        if num2 == 'out':
            print("Stopping...")
            break
        if num2 != float(num2):
            print("Input a valid number!\n")
            # asking for operation
            operation = input(f"\n{start}Your options are:{end}\nAddition\nSubtraction\nMultiplication\nDivision\nInteger Division (IntDiv)\nModulo (Mod)\nExponentation (Exp)\n{start}Which operation would you like to perform?:{end}\n").strip().lower()
            if operation == 'out':
                print("Stopping...")
                break
        
            continue
    
    match operation:
        case "addition":
            print(f"\n{num1} + {num2} = {num1+num2:.2f}")
        case "subtraction":
            print(f"\n{num1} - {num2} = {num1-num2:.2f}")
        case "multiplication":
            print(f"\n{num1} * {num2} = {num1*num2:.2f}")
        case "division":
            print(f"\n{num1} / {num2} = {num1/num2:.2f}")
        case "intdiv":
            print(f"\n{num1} // {num2} = {num1//num2:.2f}")
        case "integer division":
            print(f"\n{num1} // {num2} = {num1//num2:.2f}")
        case "modulo":
            print(f"\n{num1} % {num2} = {num1%num2:.2f}")
        case "mod":
            print(f"\n{num1} % {num2} = {num1%num2:.2f}")
        case "exp":
            print(f"\n{num1} ** {num2} = {num1**num2:.2f}")
        case "exponentation":
            print(f"\n{num1} ** {num2} = {num1**num2:.2f}")

# print("Greetings!\n")
# while True:
#     # 1st number
#     num1 = float(input("Please give me a number:\n"))
#     # 2nd number
#     num2 = float(input("Please give me a second number:\n"))
#     # asking for operation
#     operation = input(f"\n{start}Your options are:{end}\nAddition\nSubtraction\nMultiplication\nDivision\nInteger Division (IntDiv)\nModulo (Mod)\nExponentation (Exp)\n{start}Which operation would you like to perform?:{end}\n").strip().lower()
    
#     match operation:
#         case "addition":
#             print(f"\n{num1} + {num2} = {num1+num2:.2f}")
#         case "subtraction":
#             print(f"\n{num1} - {num2} = {num1-num2:.2f}")
#         case "multiplication":
#             print(f"\n{num1} * {num2} = {num1*num2:.2f}")
#         case "division":
#             print(f"\n{num1} / {num2} = {num1/num2:.2f}")
#         case "intdiv":
#             print(f"\n{num1} // {num2} = {num1//num2:.2f}")
#         case "integer division":
#             print(f"\n{num1} // {num2} = {num1//num2:.2f}")
#         case "modulo":
#             print(f"\n{num1} % {num2} = {num1%num2:.2f}")
#         case "mod":
#             print(f"\n{num1} % {num2} = {num1%num2:.2f}")
#         case "exp":
#             print(f"\n{num1} ** {num2} = {num1**num2:.2f}")
#         case "exponentation":
#             print(f"\n{num1} ** {num2} = {num1**num2:.2f}")
#         # if the input is anything other than the other cases
#         case _:
#             print(f"\nTry again. Maybe spell it correctly this time.\n")
    
    
    

