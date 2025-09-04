# KK 2nd String Methods Notes

name = input("What's your name?: ").strip().title()
age = int(input("How old are you?: "))

# .lower() > makes all characters lowercase
# .upper() > makes all characters uppercase
# .capitalize() > capitalizes the first letter of the string
# .title() > capitalizes the first letter of every word

#print("Hello {}! Nice to meet you. It's crazy that you are {:.2f} years old.".format(name,age))
print(f"Hello {name}! Nice to meet you. It's crazy that you are {age} years old.")

# print(age.isdigit())
# print(f"Really? {age} is old.")

sentence = "The quick brown fox jumps over the lazy dog!"
#print(sentence.find("fox"))
# prints the word if it can find it in sentence
word = "brown"
start = sentence.find(word)
length = len(word)
#print(sentence[start:start+length])
# replaces the word and re-prints the sentence
print(sentence.replace(word, "orange"))
