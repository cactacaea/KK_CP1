# KK 2nd Combat Program Practice

start = '\033[1m'
end = '\033[0m'

# DST CHARACTERS
username = input("What's your name?\n").capitalize().strip()
fclass = input(f"{start}\n1: Warrior\n2: Wizard\n3: Rusher{end}\nChoose your class (enter the number):\n")

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
elif fclass == "3":
    player_stats = {"name": username,}

def player_turn(player_stats, monster_stats):
    if player_stats["attack"] > monster_stats["defense"]:
        print("")
    return player_stats, monster_stats



player_stats, monster_stats = player_turn(player_stats, monster_stats)