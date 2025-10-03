# KK 2nd Rock, Paper, Scissors Practice

start = '\033[1m'
end = '\033[0m'

print("Greetings.\nType 'q' to stop playing")

while True:
    choice = input(f"\n{start}Rock: 'r'\nPaper: 'p'\nScissors: 's'{end}\nWhat would you like to play?:\n").strip().lower()
