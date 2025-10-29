# KK 2nd Combat Program Practice

import random
import time

start = '\033[1m'
end = '\033[0m'

username = input("What's your name?\n").capitalize().strip()
fclass = input(f"{start}\n1: Warrior\n2: Wizard\n3: Rusher{end}\nChoose your class (enter the number):\n")
monster_stats = {"name": "Boreal Warden",
                 "hp": 300,
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
else:
    print("Invalid option! Defaulting to WARRIOR")
    player_stats = {"name": username,
                    "hp": 130,
                    "attack": 35,
                    "dmg": 25,
                    "defense": 18}
print(f"\nYour Statistics:\nName: {player_stats["name"]}\nHealth: {player_stats["hp"]}\nAttack: {player_stats["attack"]}\nDamage: {player_stats["dmg"]}\nDefense: {player_stats["defense"]}")
time.sleep(1)

def player_turn(player_stats, monster_stats):
    time.sleep(3)
    combat_choice = input("\n1: Normal Attack\n2: Wild Attack (double damage, but you too, take damage)\n3: Healing Vial (regain 10 HP)\n4. Run for your life (50/50 chance of survival)\n\nChoose a way to go about your turn:\n")
    # NORMAL
    if combat_choice == "1":
        if player_stats["attack"] > monster_stats["defense"]:
            monster_stats["hp"] -= player_stats["attack"]
            print(f"You hit the {monster_stats["name"]}, dealing {player_stats["attack"]} damage.\n")
            time.sleep(1.5)
            print(f"The Boreal Warden has {monster_stats["hp"]} HP")
            print(f"{player_stats["name"]} has {player_stats["hp"]} HP")
        else:
            print("Your attack failed..")
    # WILD ATTACK
    elif combat_choice == "2":
        if player_stats["attack"] > monster_stats["defense"]:
            monster_stats["hp"] -= player_stats["attack"] * 2
            player_stats["hp"] -= player_stats["dmg"]
            print(f"Wild card! You dealt {player_stats["attack"] * 2} damage to the Boreal, but lost {player_stats["dmg"]} damage yourself")
            time.sleep(1.5)
            print(f"The Boreal Warden has {monster_stats["hp"]} HP")
            print(f"{player_stats["name"]} has {player_stats["hp"]} HP")
        else:
            player_stats["hp"] -= player_stats["dmg"]
            print(f"You lost {player_stats["dmg"]} health")
            time.sleep(1.5)
            print(f"The Boreal Warden has {monster_stats["hp"]} HP")
            print(f"{player_stats["name"]} has {player_stats["hp"]} HP")
    # HEALING VIAL
    elif combat_choice == "3":
        player_stats["hp"] += 10
        print("You gained 10 health. Phew!")
        time.sleep(1.5)
        print(f"The Boreal Warden has {monster_stats["hp"]} HP")
        print(f"{player_stats["name"]} has {player_stats["hp"]} HP")
    # RUN
    elif combat_choice == "4":
        running_decider = ["run","die"]
        random.choice(running_decider)
        if running_decider == "run":
            print("Good job. You ran away safely")
            monster_stats["hp"] = 0
        else:
            player_stats["hp"] -= 60
            print("Ouch. You lost 60 health while failing to escape")
            time.sleep(1.5)
            print(f"The Boreal Warden has {monster_stats["hp"]} HP")
            print(f"{player_stats["name"]} has {player_stats["hp"]} HP")

    return player_stats, monster_stats

def monster_turn(player_stats, monster_stats):
    if monster_stats["attack"] > player_stats["defense"]:
        player_stats["hp"] -= monster_stats["attack"]
        print(f"\nThe Boreal hit you. You lost {monster_stats["attack"]} health")
    else:
        print("The Boreal swings at you...")
        time.sleep(1)
        print("It missed! You didn't lose any health")
        print(f"\nThe Boreal Warden has {monster_stats["hp"]} HP")
        print(f"{player_stats["name"]} has {player_stats["hp"]} HP")
    return player_stats, monster_stats

# TURN LOOP
turn = random.choice([player_turn, monster_turn])
while monster_stats["hp"] > 0:
    if turn == player_turn:
        player_stats, monster_stats = player_turn(player_stats,monster_stats)
        turn = monster_turn
    elif turn == monster_turn:
        monster_turn(player_stats,monster_stats)
        turn = player_turn

    if player_stats["hp"] <= 0:
        print(f"{username} was killed. The Boreal Warden wins")
        break

if monster_stats["hp"] <= 0:
    print(f"{username} defeated the Warden!")

