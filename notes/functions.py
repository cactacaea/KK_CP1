# KK 2nd Functions Notes

# all imports
# set global varaibles
# define functions
# rest of the code

num = 0
player_hp = 100
monster_hp = 100

def add(x,y):
    return x+y

def initials(name):
    names = name.split(" ")
    initial = ""
    for name in names:
        initial += name[0]
    return initial

def attack(dmg, turn):
    if turn == "player":
        return monster_hp - dmg, player_hp
    else:
        return monster_hp, player_hp - dmg

while num < add(5,5):
    print("duck!")
    num += 1
print("goose!")
print(f"results are: {add(220,848)}")
total = add(8535394,9981)
print(add(add(3.14,.85),10))
add(42,7)

print(f"Tia's initials are: {initials("Tia LaRose")}")
print(f"Xavier's initials are : {initials("Xavier LaRose")}")
print(f"Kris' initials are: {initials("Krispy Kreme")}")
print("")

monster_hp, player_hp = attack(15, "monster")
print(f"Player Health: {player_hp}")
print(f"Monster Health: {monster_hp}")

monster_hp, player_hp = attack(15, "player")
print(f"Player Health: {player_hp}")
print(f"Monster Health: {monster_hp}")

print(f"a = {ord("a")}")
print(f"100 = {chr(100)}")