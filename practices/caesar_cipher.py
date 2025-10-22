# KK 2nd Caesar Cipher Encoder & Decoder

# ascii-code.com

def encode():
    message = input("Enter a message that you would like to encode into a Caesar cipher:\n")
    shift = int(input("Enter a number.\nHow many times would you like to shift this down the alphabet?:\n"))

def decode():
    message = input("Enter a message that you would like to decode from Caesar cipher to English:\n")
    shift = int(input("Enter a number.\nHow many times was this shifted down the alphabet?:\n"))

# operation question variable asking 1/2

# encode FUNCTION w/ message & shift parameters
    # numbered string using ord held in a variable
    # numbered string is increased by shift (stored in another variable)
    # increased string is converted back from numbers using char

# decode FUNCTION w/ message & shift parameters
    # numbered string using ord held in a variable
    # numbered string is decreased by the shift (stored in another variable)
    # decreased string is turned back using char

# if operation was "encode" or 1
    # ask for message input
    # ask for shift input
    # call encode with message and shift arguments
    # display new message
# if operation was "decode" or 2
    # ask for message input
    # ask for shift input
    # call decode with message and shift arguments
    # display new message