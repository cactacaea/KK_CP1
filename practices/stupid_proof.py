# KK 2nd Idiot Proof Practice

# intro & first name loop (keeps asking until the input has only letters)
print("\nGreetings!\n")
while True:
    #print("Hellow")
    firstname = input("What's your first name?:\n").capitalize().strip()
    if firstname.isalpha():
        break
    else:
        print("Nuh uh. Type actual letters, silly.\n")

# last name loop (keeps asking until the input has only letters)
while True:
    lastname = input("What's your last name?:\n").capitalize().strip()
    if lastname.isalpha():
        break
    else:
        print("Let's try this again.. if you put your last name on a passport, what would it look like?\n")

# phone number loop (keeps asking until the input is 10 letters)
while True:
    phone = input("What's your phone number?:\n").strip()
    length_phone = len(phone)
    if phone.isdigit() and length_phone == 10:
        break
    else:
        print("Try again please. This time type 10 numbers.\n")

# gpa loop (keeps asking until input is a digit/float)
while True:
    gpa = float(input("What's your GPA this term?:\n"))
    if gpa == float(gpa):
        
        break
    else: 
        print("Nope, only numbers are allowed here.\n")

# outputs
print("\n Cool cool cool. Here is your data!:\n")
print("Name:", firstname, lastname)
print("Phone:", phone[0:3], phone[3:6], phone[6:10])
print("GPA:", round(gpa, 1))
