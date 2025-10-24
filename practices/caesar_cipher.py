# KK 2nd Caesar Cipher Encoder & Decoder

# ascii-code.com

#intro
print("Greetings. Type 'exit' to stop.")

# encode FUNCTION w/ message & shift parameters
def encode(message, shift):
    # empty string to add encoded letters/charatcers
    ready_msg = ""
    for char in message:
    # modifying a character using chr and ord
        shifted_letter = ord(char) + shift
        if shifted_letter > 90 and char.isupper():
            shifted_letter -= 26
        if char.islower() and shifted_letter > 122:
            shifted_letter -= 26
        ready_msg += chr(shifted_letter) 
    # increased string is converted back from numbers using chr
    return ready_msg

# decode FUNCTION w/ message & shift parameters
def decode(message, shift):
    # empty string to add decoded letters
    ready_msg = ""
    for char in message:
    # modifying a character using chr and ord
        shifted_letter = ord(char) - shift
        if shifted_letter < 65 and char.isupper():
            shifted_letter += 26
        if char.islower() and shifted_letter < 97:
            shifted_letter += 26
        ready_msg += chr(shifted_letter) 
    # decreased string is turned back using char
    return ready_msg

# loop until user wants to stop
while True:
    # operation question variable asking opt 1 or 2
    operation = input("\nENCODE: 1\nDECODE: 2\nWould you like to encode or decode your message?:\n")
    if operation.lower() == "exit":
        break
    # ask for message input
    message = input("\nEnter the message you wish to decode/encode:\n")
    if message.lower() == "exit":
        break
    # ask for shift input
    shift = (input("\nEnter your shift number:\n"))
    if shift.lower() == "exit":
        break
    shift = int(shift)

    # if operation was "encode" or 1
    if operation == "1":
        # call encode with message and shift arguments
        encoded_msg = encode(message, shift)
        # display new message
        print(f"Your ENCODED message: {encoded_msg}")

    # if operation was "decode" or 2
    elif operation == "2":
        # call decode with message and shift arguments
        decoded_msg = decode(message, shift)
        # display new message
        print(f"Your DECODED message: {decoded_msg}")

    else:
        print("Invalid. Try again.")
print("\nStopping.")