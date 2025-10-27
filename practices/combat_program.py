# KK 2nd Combat Program Practice

import random

start = '\033[1m'
end = '\033[0m'

username = input("What's your name?\n").capitalize().strip()
fclass = input(f"{start}\n1: Warrior\n2: Wizard\n3: Rusher{end}\nChoose your class (enter the number):\n")
monster_stats = {"name": "Boreal Warden",
                 "hp": 500,
                 "attack": 28,
                 "dmg": 40,
                 "defense": 24}

# warrior
if fclass == "1":
    player_stats = {"name": username,
                    "hp": 130,
                    "attack": 35,
                    "dmg": 25,
                    "defense": 18}
# wizard
elif fclass == "2":
    player_stats = {"name": username,
                    "hp": 200,
                    "attack": 25,
                    "dmg": 25,
                    "defense": 28}
# rusher
elif fclass == "3":
    player_stats = {"name": username,
                    "hp": 170,
                    "attack": 30,
                    "dmg": 25,
                    "defense": 15}
print(f"\nYour Statistics:\nName: {player_stats["name"]}\nHealth: {player_stats["hp"]}\nAttack: {player_stats["attack"]}\nDamage: {player_stats["dmg"]}\nDefense: {player_stats["defense"]}")

def player_turn(player_stats, monster_stats):
    if player_stats["attack"] > monster_stats["defense"]:
        monster_stats["hp"] -= player_stats["attack"]
    return player_stats, monster_stats

def monster_turn(player_stats, monster_stats):
    if monster_stats["attack"] > player_stats["defense"]:
        player_stats["hp"] -= monster_stats["attack"]
    return player_stats, monster_stats

random_turn = random.choice(player_turn, monster_turn)



if random_turn == player_turn:
    print("\nIt's your turn to fight!")
    player_turn(player_stats,monster_stats)
else:
    print("The Boreal Warden attacks first.")
    monster_turn(player_stats,monster_stats)

#while monster_stats["hp"] > 0:
    

player_stats, monster_stats = player_turn(player_stats, monster_stats)