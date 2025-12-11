# KK 2nd, Text Based Adventure Game Final // Project

import random
import time
from enum import Enum, auto
from colorama import Fore, Back, Style, init
from random import shuffle
init(autoreset=True)

class Locations(Enum):
    SPAWN = auto()
    GRASSLANDS = auto()
    DECIDUOUS_FOREST = auto()
    SWAMP = auto()
    GRAVEYARD = auto()
    DESERT = auto()
    ROCKYLANDS = auto()
    STALAGMITE_TERRAIN = auto()
    OCEAN = auto()

location_names = {
    Locations.SPAWN: "Spawn",
    Locations.GRASSLANDS: "Grasslands",
    Locations.DECIDUOUS_FOREST: "Deciduous Forest",
    Locations.SWAMP: "Swamp",
    Locations.GRAVEYARD: "Graveyard",
    Locations.DESERT: "Desert",
    Locations.ROCKYLANDS: "Rockylands",
    Locations.STALAGMITE_TERRAIN: "Stalagmite Terrain",
    Locations.OCEAN: "Ocean"
}

Time = 12
day_counter = 0
night = Time >= 0 and Time < 12
if Time>24:
    day_counter += 1
    Time = 0

def main():
    bold = '\033[1m'
    end = '\033[0m'
    playername = input("Welcome to the Retreat Island! First off we need to get to know you. Enter your name or player username:\n").capitalize().strip()
    intro = "\nYou get knocked out by what seemed to be a human in a black mask--at least that's what you saw from the corner of your eye.\nAfter an unknown period of time passes, your eyes don't decieve you--you find yourself laying next to a red portal, sluggishly getting the ability to move your muscles and limbs.\nA fellow townsperson runs up to you in fear.\n\n'Save our island!'\n\nThe little boy runs away as your fuzzy brain gains awareness. You spot wooden posts nailed to trees with biome names; maybe they can be your guide...\n"
    directions = f"{bold} - - DIRECTIONS - -{end}\nCollect scrolls from each biome to find the code word. Keep trap of clues and line up the number to the letter.\nWatch out for nighttime.\nDon't let your sanity deplete too far.\nScariness may be useful in combat.\nUse your brain.\nPerhaps don't be stupid.\n"
    # CHANGE
    shadow_guardian = {
        "hp": 800,
        "dmg": 30,
        "attack_dmg": random.randint(15,25),
        "defense": 22,
        "passive_dialogue": {
            "1": "Hm.",
            "2": "Oh..",},
        "aggressive_dialogue": {
            "1": "You're actually pathetic!",},
        "attack_type": {
            "normal": 1,
            "shockwave": 2,
            "shadow_clone": 3,
            "stalactite ambush": 4,
        }
    }
    # CHANGE
    abyssal_echo = {
        "hp": 260,
        "dmg": 20,
        "attack_dmg": random.randint(15,25),
        "defense": 22,
        "passive_dialogue": {
            "1": "Hm.",
            "2": "Oh..",},
        "aggressive_dialogue": {
            "1": "You're actually pathetic!",},
        "attack_type": {
            "normal": 1,
            "ripples": 2,
            "underwater": 3,
            "wave": 4,
        }
    }
    player = {
        "name": playername,
        "hp": 150,
        "dmg_taken": 18,
        "attack_dmg": random.randint(15,28),
        "defense": 20,
        "sanity": 100,
        "scariness": 1,
        "inventory": []
    }
    
    current_loc = Locations.SPAWN

    status = {
        "player": player,
        "boss": shadow_guardian,
        "mob": abyssal_echo,
        "current_loc": current_loc
    }
    display_stats = f"{bold} - - PLAYER STATISTICS - - {end}\nUser: {bold}{player['name']}\n{end}Health: {bold}{player['hp']}{end}\nDamage: {bold}{player['dmg']}{end}\nSanity: {bold}{player['sanity']}{end}\nScariness: {bold}{player['scariness']}{end}"

    print(intro)
    time.sleep(0)
    print(directions)
    time.sleep(0)
    print(f"{display_stats}")
    time.sleep(1)
    while True:
        location = status["current_loc"]
        print(Fore.BLUE + f"\n{bold}Current Location: {location_names[location]}{end}")
        time.sleep(1)

        location_function = location_funcs[location] # if location is the class value, location function becomes the object (ex. spawn funct) from the location functions dictionary
        new_location = location_function(status) 

        if new_location in Locations:
            status['current_loc'] = new_location

def playerTurn(status, enemy):
    player_stats = status['player']
    monster_stats = enemy
    bold = '\033[1m'
    end = '\033[0m'  
    combat_choice = input(f"It's your turn to attack! What will you choose to do?\n\n#1: {bold}Normal Attack{end} - Attack with base damage\n#2: {bold}Wild Card{end} - Deal double damage to enemy but you also take damage\n#3: {bold}Stun{end} - Single use; give yourself another turn if the stun ability is unlocked\n#4: {bold}Healing{end} - Gain 15 health if you collected healing resources\n#5: {bold}Ranged Attack{end} - Throw rocks, berries, sand bags, acorns, or mushrooms at enemy if you collected said resources, recieve another turn; low damage and 4 uses\n#6: {bold}Flee{end} - Abyssal Echo only, 50/50 chance of losing health or exiting the combat sequence.\n\nEnter your choice as a number:\n")
    # 1 normal attack
    if combat_choice == "1":
        if player_stats["attack"] > monster_stats["defense"]:
            monster_stats["hp"] -= player_stats["attack"]
            print(f"You dealt {player_stats["attack_dmg"]} to the {monster_stats['name']}!")
            time.sleep(2)
            print(f"The {monster_stats['name']}: {monster_stats["hp"]} HP")
            print(f"{player_stats["name"]}: {player_stats["hp"]} HP")
    # 2 wild card
    # elif combat_choice == "2":
    # # 3 stun (if unlocked)
    # elif combat_choice == "3":
    # # 4 healing
    # elif combat_choice == "4":
    # # 5 ranged attack
    # elif combat_choice == "5":
    # # 6 flee
    # elif combat_choice == "6":
    else:
        print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")

def monsterTurn(status, enemy):
    player_stats = status['player']
    monster_stats = enemy
    bold = '\033[1m'
    end = '\033[0m'
def spawn(status):
    bold = '\033[1m'
    end = '\033[0m'

    print(f"\n{bold}Where do you want to go?{end} (Enter the number)")
    options = [
        Locations.DECIDUOUS_FOREST, 
        Locations.DESERT, 
        Locations.GRASSLANDS, 
        Locations.GRAVEYARD, 
        Locations.OCEAN, 
        Locations.ROCKYLANDS, 
        Locations.SWAMP, 
        Locations.STALAGMITE_TERRAIN]
    for i, x in enumerate(options):
        print(f'{i}. {location_names[x]}')
    while True:
        try:
            loc_num = int(input("\n?: ").strip().lower())
            if 0 <= loc_num <len(options):
                return options[loc_num]
            else:
                print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
        except ValueError:
            print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")

def grasslands(status):
    # options to go to spawn, stalagmite terrain, desert
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","search","scavenge","unscramble"]
    easy_words = []
    hard_words = []
    print("\nThe grasslands feature....")
    while True:
        action_choice = input(f"\nWhat would you like to do?\n - {bold}Walk{end} to another location\n - {bold}Search{end} for a scroll\n - {bold}Scavenge{end} for food and mobs\n - {bold}Unscramble{end} words to find weapons or lore\n\nEnter the bolded word for your action:\n").strip().lower()
        if action_choice in avail_actions:
            break
        else:
            print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
    if action_choice == "walk":
        print(f"\n{bold}Where do you want to go?{end} (Enter the number)")
        options = [
            Locations.SPAWN,
            Locations.STALAGMITE_TERRAIN,
            Locations.DESERT]
        for i, x in enumerate(options):
            print(f'{i}. {location_names[x]}')
        while True:
            try:
                loc_num = int(input("\n?: ").strip().lower())
                if 0 <= loc_num <len(options):
                    return options[loc_num]
                else:
                    print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
            except ValueError:
                print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
    elif action_choice == "search":
        print("Type 'exit' if you're unable to guess the word")
        
    elif action_choice == "scavenge":
        print("placeholder")
    elif action_choice == "unscramble":
        print("placeholder")
    else:
        print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")


def deciduousForest(status):
    # options to go to spawn, graveyard, desert
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","chop","pick","search"]
    print("\nThe deciduous forest features....")
    while True:
        action_choice = input(f"\nWhat would you like to do?\n - {bold}Walk{end} to another location\n - {bold}Search{end} for a scroll\n - {bold}Chop{end} trees for logs\n - {bold}Pick{end} mushrooms\n\nEnter the bolded word for your action:\n").strip().lower()
        if action_choice in avail_actions:
            break
        else:
            print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
    if action_choice == "walk":
        print(f"\n{bold}Where do you want to go?{end} (Enter the number)")
        options = [
            Locations.SPAWN,
            Locations.GRAVEYARD,
            Locations.DESERT]
        for i, x in enumerate(options):
            print(f'{i}. {location_names[x]}')
        while True:
            try:
                loc_num = int(input("\n?: ").strip().lower())
                if 0 <= loc_num <len(options):
                    return options[loc_num]
                else:
                    print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
            except ValueError:
                print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
    elif action_choice == "chop":
        print("placeholder")
    elif action_choice == "pick":
        print("placeholder")
    elif action_choice == "search":
        print("placeholder")
    else:
        print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")

def swamp(status):
    # options to go to spawn, ocean, stalagmite terrain
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","search","socialize"]
    print("\nThe swamp features....")
    while True:
        action_choice = input(f"\nWhat would you like to do?\n - {bold}Walk{end} to another location\n - {bold}Search{end} for a scroll\n - {bold}Socialize{end} with townspeople for resources and help\n\nEnter the bolded word for your action:\n").strip().lower()
        if action_choice in avail_actions:
            break
        else:
            print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")

    if action_choice == "walk":
        print(f"\n{bold}Where do you want to go?{end} (Enter the number)")
        options = [
            Locations.SPAWN,
            Locations.STALAGMITE_TERRAIN,
            Locations.OCEAN]
        for i, x in enumerate(options):
            print(f'{i}. {location_names[x]}')
        while True:
            try:
                loc_num = int(input("\n?: ").strip().lower())
                if 0 <= loc_num <len(options):
                    return options[loc_num]
                else:
                    print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
            except ValueError:
                print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
    elif action_choice == "search":
        print("placeholder")
    elif action_choice == "socialize":
        print("placeholder")
    else:
        print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
    
def graveyard(status):
    # options to go to deciduous forest, rockylands, spawn
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","search","dig"]
    print("\nThe graveyard features....")
    while True:
        action_choice = input(f"\nWhat would you like to do?\n - {bold}Walk{end} to another location\n - {bold}Search{end} for a scroll\n - {bold}Dig{end} graves for aid in combat or fragments of lore\n\nEnter the bolded word for your action:\n").strip().lower()
        if action_choice in avail_actions:
            break
        else:
            print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
    if action_choice == "walk":
        print(f"\n{bold}Where do you want to go?{end} (Enter the number)")
        options = [
            Locations.SPAWN,
            Locations.DECIDUOUS_FOREST,
            Locations.ROCKYLANDS]
        for i, x in enumerate(options):
            print(f'{i}. {location_names[x]}')
        while True:
            try:
                loc_num = int(input("\n?: ").strip().lower())
                if 0 <= loc_num <len(options):
                    return options[loc_num]
                else:
                    print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
            except ValueError:
                print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
    elif action_choice == "search":
        print("placeholder")
    elif action_choice == "dig":
        print("placeholder")
    else:
        print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")

def desert(status):
    # options to go to forest, spawn, grasslands
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","search","seek"]
    print("\nThe desert features....")
    while True:
        action_choice = input(f"\nWhat would you like to do?\n - {bold}Walk{end} to another location\n - {bold}Search{end} for a scroll\n - {bold}Seek{end} for weapons and lore fragments in the sand\n\nEnter the bolded word for your action:\n").strip().lower()
        if action_choice in avail_actions:
            break
        else:
            print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
    if action_choice == "walk":
        print(f"\n{bold}Where do you want to go?{end} (Enter the number)")
        options = [
            Locations.SPAWN,
            Locations.DECIDUOUS_FOREST,
            Locations.GRASSLANDS]
        for i, x in enumerate(options):
            print(f'{i}. {location_names[x]}')
        while True:
            try:
                loc_num = int(input("\n?: ").strip().lower())
                if 0 <= loc_num <len(options):
                    return options[loc_num]
                else:
                    print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
            except ValueError:
                print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
    elif action_choice == "search":
        print("placeholder")
    elif action_choice == "dig":
        print("placeholder")
    else:
        print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")


def rockylands(status):
    # options to go to ocean, spawn, graveyard
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","search","build","mine"]
    print("\nThe rockylands feature....")
    while True:
        action_choice = input(f"\nWhat would you like to do?\n - {bold}Walk{end} to another location\n - {bold}Search{end} for a scroll\n - {bold}Build{end} weapons from resources\n - {bold}Mine{end} boulders for rocks\n\nEnter the bolded word for your action:\n").strip().lower()
        if action_choice in avail_actions:
            break
        else:
            print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
    if action_choice == "walk":
        print(f"\n{bold}Where do you want to go?{end} (Enter the number)")
        options = [
            Locations.SPAWN,
            Locations.OCEAN,
            Locations.GRAVEYARD]
        for i, x in enumerate(options):
            print(f'{i}. {location_names[x]}')
        while True:
            try:
                loc_num = int(input("\n?: ").strip().lower())
                if 0 <= loc_num <len(options):
                    return options[loc_num]
                else:
                    print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
            except ValueError:
                print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
    elif action_choice == "search":
        print("placeholder")
    elif action_choice == "build":
        print("placeholder")
    elif action_choice == "mine":
        print("placeholder")
    else:
        print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")


def stalagmiteTerrain(status):
    shadow_guardian = status['boss']
    # options to go to swamp, grasslands, spawn
    bold = '\033[1m'
    end = '\033[0m'
    
def ocean(status):
    abyssal_echo = status['mob']
    # options to go to rockylands, swamp, spawn
    bold = '\033[1m'
    end = '\033[0m'
    if abyssal_echo['hp'] > 0:
        print("abyssal echo is alive")
    turn = random.choice([playerTurn, monsterTurn])
    while monster_stats["hp"] > 0:
        if turn == playerTurn:
            player_stats, monster_stats = playerTurn(player_stats,abyssal_echo)
            turn = monsterTurn
        elif turn == monsterTurn:
            monsterTurn(player_stats,abyssal_echo)
            turn = playerTurn

        if player_stats["hp"] <= 0:
            print(f"{player_stats['name']} was killed. The Abyssal Echo swallowed you whole.")
            break

    if monster_stats["hp"] <= 0:
        print(f"{player_stats['name']} emerged victorious in a gruesome battle against the Abyssal Echo!")


location_funcs = {
    Locations.SPAWN: spawn,
    Locations.GRASSLANDS: grasslands,
    Locations.DECIDUOUS_FOREST: deciduousForest,
    Locations.SWAMP: swamp,
    Locations.GRAVEYARD: graveyard,
    Locations.DESERT: desert,
    Locations.ROCKYLANDS: rockylands,
    Locations.STALAGMITE_TERRAIN: stalagmiteTerrain,
    Locations.OCEAN: ocean
}

main()