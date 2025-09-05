# KK 2nd Stupid Proofing Practice

print("Greetings!\n")
while True:
    print("hi")
    firstname = input("What's your first name?:\n").capitalize().strip()
    if firstname.isalpha():
        break
    else:
        print("Nuh uh. Type actual letters, silly.\n")
    lastname = input("What's your last name?:\n").capitalize().strip()
    if lastname.isalpha():
        break
    else:
        print("Let's try this again.. if you put your last name on a passport, what would it look like?\n")
    phone = input("What's your phone number?:\n")


