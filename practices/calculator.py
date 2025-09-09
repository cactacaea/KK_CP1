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
    num1 = input("Please give me a number:\n")
    num2 = input("Please give me a second number:\n")
    operation = input(f"\n{start}Your options are:{end}\nAddition\nSubtraction\nMultiplication\nDivision\nInteger Division (IntDiv)\nModulo (Mod)\nExponentation (Exp)\n{start}Which operation would you like to perform?:{end}\n").strip().lower()
    match operation:
        case "addition":
            print(f"\n{num1} + {num2} = {num1+num2}")
        case "subtraction":
            print(f"\n{num1} - {num2} = {num1-num2}")
        case "multiplication":
            print(f"\n{num1} + {num2} = {num1+num2}")
        case "divison":
            print(f"\n{num1} + {num2} = {num1+num2}")
        case "intdiv":
            print(f"\n{num1} + {num2} = {num1+num2}")
        case "integer division":
            print(f"\n{num1} + {num2} = {num1+num2}")
        case "modulo":
            print(f"\n{num1} + {num2} = {num1+num2}")
        case "mod":
            print(f"\n{num1} + {num2} = {num1+num2}")
        case "exp":
            print(f"\n{num1} + {num2} = {num1+num2}")
        case _:
            print(f"\nTry again.")
    if num1 or num2 or operation == 'out':
        break
    
    

