print("Greetings!\n")
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