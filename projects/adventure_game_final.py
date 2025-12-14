# KK 2nd, Text Based Adventure Game Final // Project

import random
import time
import sys
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

# scroll questions  
easymath1 = "Evaluate; 2^3 + 12 / 3 = ?"
easymath2 = "Simplify; 3(2x+5) - 4x"
easymath3 = "What's 3/4 of 20?"

rockylands_easymath_Qs_and_As = [
    (easymath1, "12"),
    (easymath2, "2x+15"),
    (easymath1, "15"),
]

analogy1 = "Leaf : Tree :: Petal : ?"
analogy2 = "Black : White :: Hot : ?"
analogy3 = "Puppy : Dog :: Kitten : ?"

desert_analogy_Qs_and_As = [
    (analogy1, "flower"),
    (analogy2, "cold"),
    (analogy3, "cat"),
]

name_list1 = "Nova\nLeo\nViper\nWillow\nAstra\nIvy\nMaya\nSkipper\nWilson\nAce\nWolfgang\nNova\nYuni\nGinger\nSascha"
name_list2 = "Asper\nVincent\nAmbrose\nAugust\nOphelia\nWilfred\nBlanche\nVinny\nAmbrose\nVivian\nOllie\nAlexandra\nSupernova"
name_list3 = "Dmitri\nWinni\nSadie\nCamille\nLizzie\nVexley\nWillow\nIvy\nConnor\nWinter\nDakota\nAsper\nBracia\nWllow\nLizzie"

graveyard_name_list_As = [
    (name_list1, "nova"),
    (name_list2, "ambrose"),
    (name_list3, "lizzie"),
]

poison_animal1 = ""
poison_animal2 = ""
poison_animal3 = ""

swamp_poison_animal_As = [
    (),
    (),
    (),
]

riddle1 = ""
riddle2 = ""
riddle3 = ""

dec_forest_riddles = [
    (),
    (),
    (),
]

unscramble1 = "LPAEP"
unscramble2 = "TUERUF"
unscramble3 = "DRBAO"

grasslands_unscrambling = [
    (unscramble1, "apple"),
    (unscramble2, "future"),
    (unscramble3, "board"),
]

# different biome dialogue

# grasslands

# dec forest

# swamp

# graveyard

# desert

# rockylands

# ocean

def winLose():
    bold = '\033[1m'
    end = '\033[0m'
    while True:
        queue = input(f"\n{bold}Yes/No - Would you like to play again?:{end}\n")
        if queue == "no":
            sys.exit()
            break
        elif queue == "yes":
            print(" ")
            main()
        else:
            print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")

def main():
    bold = '\033[1m'
    end = '\033[0m'
    playername = input("Welcome to the Retreat Island! First off we need to get to know you. Enter your name:\n").capitalize().strip()
    intro = "\nYou get knocked out by what seemed to be a human in a black mask--at least that's what you saw from the corner of your eye.\nAfter an unknown period of time passes, your eyes don't decieve you--you find yourself laying next to a red portal, sluggishly getting the ability to move your muscles and limbs.\nA fellow townsperson runs up to you in fear.\n\n'Save our island!'\n\nThe little boy runs away as your fuzzy brain gains awareness. You spot wooden posts nailed to trees with biome names; maybe they can be your guide...\n"
    directions = f"{bold} - - DIRECTIONS - -{end}\nCollect scrolls from each biome to find the code word. Keep track of clues and line up the number to the letter.\nDon't let your sanity deplete too far.\nScariness may be useful in combat..\nUse your brain.\nPerhaps don't be stupid.\n\n{bold} - - IMPORTANT NOTE - -{end}\nBe careful when reading details! They will help you find the CODE!\n"
    item_lookup = {
        # healing items
        "Orange Blossom": {
            "type": "healing"},
        "Healing Herb": {
            "type": "healing"},
        "Cherry Pierogi": {
            "type": "healing"},
        "Sweet Goop": {
            "type": "healing"},
        # ranged weapons
        "Acorn": {
            "type": "ranged"},
        "Sand Bag": {
            "type": "ranged"},
        "Berry": {
            "type": "ranged"},
        "Rock": {
            "type": "ranged"},
        "Mushroom": {
            "type": "ranged"},
    }
    weapon_damages = {
        "Sharpened Stick": 5, # in grasslands
        "Bone Shard": 10, # desert
        "Kelp Rope": 8, # ocean
        "Spear": 16, # crafted in rockylands
        "Obsidian Shard": 6, # graveyard
    }

    # CHANGE
    shadow_guardian = {
        "name": "Shadow Guardian",
        "hp": 300,
        "defense": 10,
        "passive_dialogue": {
            "1": "Hm.",
            "2": "Oh..",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
        },
        "aggressive_dialogue": {
            "1": "You're actually pathetic!",
            "2": "Has no one ever taught you how to properly use a weapon or what?",
            "3": "Wild, curious..almost disgusting creatures, you are. Can't leave the poor shadows alone",
            "4": "",
            "5": "",
            "6": "",
        },
        "scared_dialogue":{
            "1": "Hhhhhhh...k- keep those claws away from me!",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
        }
    }
    # CHANGE
    abyssal_echo = {
        "name": "Abyssal Echo",
        "hp": 180,
        "defense": 8,
        "passive_dialogue": {
            "1": "Hm.",
            "2": "Oh..",},
        "aggressive_dialogue": {
            "1": "You're actually pathetic!",},
        "scared_dialogue":{
            "1": "I-i.."
    }}
    player = {
        "name": playername,
        "hp": 150,
        "attacking_damage": 20, # print ~20 + weapon
        "defense": 8,
        "sanity": 100,
        "scariness": 1,
        "inventory": ["Stick"]
    }

    current_loc = Locations.SPAWN

    status = {
        "player": player,
        "boss": shadow_guardian,
        "mob": abyssal_echo,
        "current_loc": current_loc,
        "current_enemy": None,
        "weapon": None,
        "item_lookup": item_lookup,
        "weapon_lookup": weapon_damages,
    }

    display_stats = f"{bold} - - PLAYER STATISTICS - - {end}\nUser: {bold}{player['name']}\n{end}Health: {bold}{player['hp']}{end}\nAttacking Damage: {bold}16-26{end}\nDefense: {bold}{player['defense']}{end}\nSanity: {bold}{player['sanity']}{end}\nScariness: {bold}{player['scariness']}{end}"

    print(intro)
    time.sleep(1) #7
    print(directions)
    time.sleep(1) #7
    print(f"{display_stats}")
    time.sleep(1) #5
    while True:
        location = status["current_loc"]
        print(Fore.BLACK + f"\n{bold}Current Location: {location_names[location]}{end}")
        time.sleep(1)

        location_function = location_funcs[location] # if location is the class value, location function becomes the object (ex. spawn funct) from the location functions dictionary
        new_location = location_function(status) 

        if new_location in Locations:
            status['current_loc'] = new_location

def playerTurn(status, combat_status):
    weapon_name = status["weapon"]
    weapon_dmg = status["weapon_lookup"].get(weapon_name, 0)
    item_lookup = status['item_lookup']
    player_stats = status['player']
    monster_stats = status['current_enemy']
    avail_choices = ["1","2","3","4","5","6"]
    bold = '\033[1m'
    end = '\033[0m'
    inventory = status['player']['inventory']

    if player_stats['hp'] <= 0:
        return status

    while True:
        combat_choice = input(f"\nIt's your turn to attack! What will you choose to do?\n\n#1: {bold}Normal Attack{end} - Attack with base damage\n#2: {bold}Wild Card{end} - Deal double damage to enemy but you also take damage\n#3: {bold}Stun{end} - Single use; normal attack damage, alonside giving yourself another turn {bold}if the stun ability is unlocked{end}\n#4: {bold}Healing{end} - Gain 15 health if you collected healing resources\n#5: {bold}Ranged Attack{end} - Wrist Rocket needed. Throw rocks, berries, sand bags, acorns, or mushrooms at enemy if you collected said resources, recieve another turn; low damage and 4 uses\n#6: {bold}Flee{end} - Abyssal Echo only, 50/50 chance of losing health or exiting the combat sequence.\n\nEnter your choice as a number:\n")
        if combat_choice in avail_choices:
            break
        else:
            print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
            time.sleep(2)
    player_dmg = random.randint(16,26) + weapon_dmg
    # 1 normal attack
    if combat_choice == "1":
        calculated_dmg = max(0, player_dmg - monster_stats["defense"])
        monster_stats["hp"] -= calculated_dmg
        print(f"Your inital attack is {player_dmg}...You dealt {calculated_dmg} damage after the monster's defense.")

    # 2 wild card
    elif combat_choice == "2":
        double = player_dmg * 2
        calculated_dmg = max(0, double - monster_stats["defense"])
        monster_stats["hp"] -= calculated_dmg
        player_stats["hp"] -= 20  #penalty
        print(f"You dealt {calculated_dmg} damage to the {monster_stats['name']} but.. lost 20 HP.")
        time.sleep(2)
            
    # 3 stun (if unlocked)
    elif combat_choice == "3":
        if player_stats['scariness'] == 3:
            if combat_status['stun_counter'] < 1:
                calculated_dmg = max(0, player_dmg - monster_stats["defense"])
                monster_stats["hp"] -= calculated_dmg
                print(f"Your inital attack is {player_dmg}...You dealt {calculated_dmg} damage after the monster's defense.\nSTUN ability used up! The enemy is stunned--you have time to land another hit on it!")
                combat_status['stun_counter'] += 1
                time.sleep(4)
                return "added_turn"
            else:
                print("You already used this combat strategy in this fight! Turn skipped..")
        else:
            print("Your scariness stat is below 3! Turn skipped..")
    # # 4 healing
    elif combat_choice == "4":
        healing_items = [item for item in inventory if item in item_lookup and item_lookup[item]["type"] == "healing"]
        if not healing_items:
            print("You have no healing items! Turn skipped..")
            return "end"
        used_item = random.choice(healing_items)
        player_stats["hp"] = min(player_stats["hp"] + 15, 150)
        inventory.remove(used_item)
        print(f"You used {used_item} and gained 15 HP! (IF you weren't already at 150..)")
    # 5 ranged attack
    elif combat_choice == "5":
        ranged_items = [item for item in inventory if item in item_lookup and item_lookup[item]["type"] == "ranged"]
        if not ranged_items:
            print("You have no projectiles to throw.. Turn skipped.")
            return "end"
        used_item = random.choice(ranged_items)
        combat_status["ranged_atk_counter"] += 1
        dmg = random.randint(8,14)
        monster_stats["hp"] -= dmg
        print(f"You throw a {used_item} for {dmg} damage and stun your enemy!")
        print(Fore.BLUE + f"\n{monster_stats['name']}: {monster_stats["hp"]} HP")
        print(Fore.BLUE + f"{player_stats["name"]}: {player_stats["hp"]} HP")
        return "added_turn"

    # 6 flee
    elif combat_choice == "6":
        if monster_stats['name'] == "Abyssal Echo":
            running_decider = ["run","die"]
            chosen = random.choice(running_decider)
            if chosen == "run":
                print("You successfully escaped to the mysterious red portal at spawn--for now. The Abyssal Echo awaits your return.")
                time.sleep(3)
                status['current_loc'] = Locations.SPAWN
                status['current_enemy'] = None
                return status
            if chosen == "die":
                print("The Abyssal Echo yanks your legs down with its tail..you fail to flee and break your toe; -12 damage")
                player_stats["hp"] -= 12
        else:
            print("It's too late to run, my friend. Turn lost..")
    else:
        print(Fore.RED + "\nERROR /// INVALID CHOICE /// TURN LOST.")

    print(Fore.BLUE + f"\n{monster_stats['name']}: {monster_stats["hp"]} HP")
    print(Fore.BLUE + f"{player_stats["name"]}: {player_stats["hp"]} HP")
    time.sleep(3)
    return "end"

def monsterTurn(status):
    player_stats = status['player']
    monster_stats = status['current_enemy']
    bold = '\033[1m'
    end = '\033[0m'

    if monster_stats['hp'] <= 0:
        return status
    else:
        monster_dmg = random.randint(18,26)
        calculated = max(0, monster_dmg - player_stats['defense'])
        player_stats['hp'] -= calculated
        print(f"\nIts inital attack is {monster_dmg}...The {monster_stats['name']} dealt {calculated} damage after your defense.")
        time.sleep(3)
        print(Fore.BLUE + f"\n{monster_stats['name']}: {monster_stats["hp"]} HP")
        print(Fore.BLUE + f"{player_stats["name"]}: {player_stats["hp"]} HP")
        time.sleep(3)
    return status
  
def spawn(status):
    player = status['player']
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","view"]

    print("\nAt your spawnpoint, the aura from the red portal makes you shiver when looking where to go next.\nErr- why does it have an eyeball attached to the top of it?.. Hahah. Hah. Hahahahahahha....?")
    time.sleep(2)
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
    player_stats = status['player']
    # options to go to spawn, stalagmite terrain, desert
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","search","scavenge","unscramble"]
    print("\nThe grasslands are bare, but..who doesn't like soft, bright green grass? You spot friendly rabbits who run away as you inch closer to them.")
    time.sleep(5)
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
        print("\nSoft grass under your toes turns into hardened mud, you approach several boards nailed to rows of trees.")
        time.sleep(2)
        print("\nType 'exit' to go back to action list.\n")
        time.sleep(2)
        while True:
            question, answer = random.choice(grasslands_unscrambling)
            print(question)
            guess = input("Unscramble the word:\n").lower().strip()
            if guess == "exit":
                break
            if guess == answer:
                print("\nJackpot! Papers flutter down as the last puzzle piece you placed unhooked the wooden board. Trying to pick one up, you exactly the scroll you needed")
                print(f"-,-^~`_`*.{bold}5Y{end}")
                time.sleep(5)
                break
            else:
                print("You were caught doing 'magic.' Just because of easy math. Better luck next time--be sneaky alright??\n-5 Health")
                player_stats['hp'] -= 5
                break
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
    print("\nThe deciduous forest features bright orange trees and dried mud. What a lovely place for trees.")
    time.sleep(4)
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
        print("\nFull of oddities, this island is. Just an hour of wandering you see a raccoon with a pattern on its back that looked like '7S'\nWait..?--")
        time.sleep(3)
    else:
        print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")

def swamp(status):
    weapon_name = status["weapon"]
    weapon_dmg = status["weapon_lookup"].get(weapon_name, 0)
    attacking_dmg = 20 + weapon_dmg
    player = status['player']
    # options to go to spawn, ocean, stalagmite terrain
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","search","socialize","view"]
    print("\nMucky dirt puddles reek of animal manure. A mosquito lands on you--followed by a few more flies as you swat them. Lit up houses are spotted from afar.\nGrass and weeds build up on your legs every time you take a step.")
    time.sleep(9)
    while True:
        action_choice = input(f"\nWhat would you like to do?\n - {bold}Walk{end} to another location\n - {bold}Search{end} for a scroll\n - {bold}Socialize{end} with townspeople for resources and help\n - {bold}View{end} your inventory and statistics\n\nEnter the bolded word for your action:\n").strip().lower()
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
        print(f"\nA fellow villager, though dirty in mud and raspberry jam--which looks incredibly appetizing--hands you a recipe book for future reference\nThat is, if you make it out of this place alive. One page mentions {bold}{Fore.BLACK}'R6'{end}{Fore.RESET} for.. no reason? Or maybe uhm..who knows..")
        time.sleep(7)
    elif action_choice == "socialize":
        print("placeholder")
    elif action_choice == "view":
        print("\nYou find a swirly rock amidst an ant hill. It's a pretty rock, really--though trying to extract it from the muck, all your items fly out from your pockets\nEverything floats in front of you to observe.\n")
        time.sleep(4)
        print(f"{bold} - - - PLAYER STATISTICS - - - {end}\nUser: {bold}{player['name']}\n{end}Health: {bold}{player['hp']}{end}\nAttacking Damage: {bold}~{attacking_dmg}{end}\nDefense: {bold}{player['defense']}{end}\nSanity: {bold}{player['sanity']}{end}\nScariness: {bold}{player['scariness']}{end}")
        print(f"\n{bold}EQUIPPED WEAPON:{end} {status['weapon']}\n")
        time.sleep(4)
        print(f"{bold} - - - Inventory - - - {end}")
        item_counts = {}
        for item in player["inventory"]:
            item_counts[item] = item_counts.get(item, 0) + 1
        for item, count in item_counts.items():
            print(f"{count}x {item}")
        time.sleep(3)
        print("\nExiting to the main menu in a moment..")
        time.sleep(8)
    else:
        print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
    
def graveyard(status):
    player_stats = status['player']
    # options to go to deciduous forest, rockylands, spawn
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","search","dig"]
    print("\nYou feel the presence of spirits as you walk by each grave. The graveyard feels uncomfortable and bare.\nAlthough, perhaps it's more interesting at a second glance. We don't judge books by their covers here.")
    time.sleep(5)
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
        print("\nVenturing deeper into the graveyard, you feel nauseous..maybe you remember the way you came from? Jus--t--find..\nfi..nd similar.. names----")
        time.sleep(3)
        print("\nType 'exit' to go back to action list.\n")
        time.sleep(2)
        while True:
            question, answer = random.choice(graveyard_name_list_As)
            print(question)
            guess = input("\nWhat name appears twice?:\n").lower().strip()
            if guess == "exit":
                break
            if guess == answer:
                print("\nA piece of paper sticks to your foot--")
                print(f"`-_`*~~_`/{bold}E2{end}")
                time.sleep(5)
                break
            else:
                print("Felt like a spirit bit your ankle for not paying attention. Oh well, maybe 5 health or so")
                player_stats['hp'] -= 5
                break
    elif action_choice == "build":
        print("placeholder")
    elif action_choice == "mine":
        print("placeholder")
    elif action_choice == "dig":
        print("placeholder")
    else:
        print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")

def desert(status):
    player_stats = status['player']
    # options to go to forest, spawn, grasslands
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","search","seek"]
    print("\nTemples, wells, and mounds of sand make up a scorching desert. Cacti and sticks in the ground seem useless.\nYour bare feet warm up as you explore the dry land.")
    time.sleep(5)
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
        print("\nYou dig through piles upon piles of hot sand with thorns and debris until something sticks out of the ground..")
        time.sleep(2)
        print("\nType 'exit' to go back to action list.\n")
        time.sleep(2)
        while True:
            question, answer = random.choice(desert_analogy_Qs_and_As)
            print(question)
            guess = input("'Complete the analogy to decipher the message' states the wooden board.\n").lower().strip()
            if guess == "exit":
                break
            if guess == answer:
                print(f"\nAfter painful thinking and sitting in the sand until the day got cold, you\nfinally swipe away some sand and find the letter you needed..{bold}{Fore.YELLOW}4H{end}{Fore.RESET}")
                time.sleep(5)
                break
            else:
                print("Yikes, you lost 5 health stubbing your toe. Be more focused on writing next time")
                player_stats['hp'] -= 5
                time.sleep(2)
                break
    elif action_choice == "seek":
        print("placeholder")
    else:
        print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")

def rockylands(status):
    player_stats = status['player']
    inventory = player_stats['inventory']
    # options to go to ocean, spawn, graveyard
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","search","build","mine"]
    print("\nMountains of boulders, gems, and small rocks make up the lovely rockylands.")
    time.sleep(5)
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
        print("\nAs you avoid sharp objects on the rocky ground, continuing the 'hike', you lift your head to reveal a small cave--stopping in your tracks. Fascinating.")
        time.sleep(2)
        print("\nType 'exit' to go back to action list.\n")
        time.sleep(2)
        while True:
            question, answer = random.choice(rockylands_easymath_Qs_and_As)
            print(question)
            guess = input("Answer with no spaces and capitals:\n").lower().strip()
            if guess == "exit":
                break
            if guess == answer:
                print("\nNot sure who read what you wrote--in return, a scroll falls from a nearby edge")
                print(f"~_--`{bold}Z1{end}")
                time.sleep(5)
                break
            else:
                print("You were caught doing 'magic.' Just because of easy math. Better luck next time--be sneaky alright??")
                player_stats['hp'] -= 5
                break
    elif action_choice == "build":
        print("\nSpotting a wooden block from afar, on approach you notice that it has a 3x3 grid. A fascinating, magic crafter!\nUpon touching it, several objects are yoinked from your hands and pockets\nYou need 2 rocks and a stick to make a spear. Might be useful in combat if you have the resources")
        time.sleep(6)
        while True:
            choice = input("\nYes/No - Do you wish to proceed in crafting?:\n").strip().lower()
            if choice == "no":
                print("\nYou chose to stray from giving the crafter your precious items.")
                break
            elif choice == "yes":
                print("\nChecking for necessary items...")
                time.sleep(2)
                rocks = inventory.count("Rock")
                sticks = inventory.count("Stick")
                if rocks >= 2 and sticks >= 1:
                    inventory.remove("Rock")
                    inventory.remove("Rock")
                    inventory.remove("Stick")
                    print("\nYou have the resources required! The crafter wobbles as a spear comes together.")
                    if status['weapon'] is not None:
                        replace = input(f"\nYes/No - You're currently wielding a {status['weapon']}. Would you like to replace it?:\n").lower().strip()
                        if replace == "yes":
                            player_stats["weapon"] = "Spear"
                            print("\nSpear equipped.")
                        else:
                            print("\nYou decide to keep your weapon. The spear vanishes into thin air. Odd, but alrighty then.")
                    else:
                        status['weapon'] = "Spear"
                        print("\nSince your pockets are empty of weapons, you grab the spear to your advantage.\nYou grant +16 base attacking damage")
                        time.sleep(4)
                else:
                    print("\nYou don't have enough materials, silly. The crafter rejects your peace offering. Well, not really a peace offering but--\nanyway. Whilst leaving, you stub your toe. Youch! -1 Health.")
                    player_stats['hp'] -= 1
                    time.sleep(3.5)
                break
            else:
                print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
    elif action_choice == "mine":
        while True:
            print("\nYou pick up the pickaxe laying amongst the boulders. Swing in the correct direction using WASD.")
            times = random.randint(7,10)
            directions = {
                "up": "w",
                "down": "s",
                "left": "a",
                "right": "d"}
            for i in range(times):
                direction = random.choice(list(directions.keys()))
                correct_key = directions[direction]
                print(f"\nStrike {direction.upper()}!")
                key_choice = input().lower().strip()
                if key_choice == correct_key:
                    print(f"\n{bold}*CRACK*{end}")
                else:
                    print("Your foot slipped! You struggle getting up for a bit...")
                    time.sleep(3)
            print("\nThe boulder cracks apart! You pick up a decent rock and gain 0.2 scariness.")
            time.sleep(1.5)
            inventory.append("Rock")
            player_stats['scariness'] += min(player_stats['scariness'] + .2,3)
            again = input("\nYes/No - Mine again?:").lower().strip()
            if again == "yes":
                print("\nYou walk over to another rock.")
            elif again == "no":
                break
            else:
                print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
    else:
        print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")

def stalagmiteTerrain(status):
    monster_stats = status['boss']
    player_stats = status['player']
    status['current_enemy'] = status['boss']
    combat_status = {
        "stun_counter": 0,
        "ranged_atk_counter": 0
    }
    # options to go to swamp, grasslands, spawn
    bold = '\033[1m'
    end = '\033[0m'
    print("\nWater drips from the stalagtites above your head--which are sharp as a spear. Your foot bumps into som- piles of human skeletons? Really?\nEugh....Better be careful. The echoes of bats' wings invade your perception of hearing as another raspy voice enters your ear canal. Yikes.")
    time.sleep(6)
    code = input(Fore.MAGENTA + f"\nEnter the 7-letter code:\n" + Fore.RESET).lower().strip()
    if code == "zephyrs":
        print(f"\nSlowly but surely you reach the deepest section of the cave picking up trinkets and a torch along the pathway; stalagmites connecting with stalagtites, broken shards of glass and rock\nsurround cracked pillars of dark, mossy stone. At last, an enormous shadow dims the flame of your torch; {bold}{Fore.MAGENTA}The Shadow Guardian{end}{Fore.RESET}.. This is the only way to save the island residents. Prevent their poor souls from being taken over by fury.")
        time.sleep(9)
        turn = random.choice([playerTurn, monsterTurn])
        while monster_stats["hp"] > 0:
            if player_stats["hp"] <= 0:
                print(f"{bold}YOU DIED!{end} Engulfed by the Shadow Guardian. Your body lays there whilst finishing decomposing.")
                winLose()
                break
            if status['current_enemy'] == None:
                break
            if status['current_loc'] != Locations.STALAGMITE_TERRAIN:
                break
            if status['current_enemy']['hp'] <= 0:
                winLose()
                break
            if turn == "player":
                calc = playerTurn(status, combat_status)
                if calc != "added_turn":
                    turn = "monster"
            else:
                monsterTurn(status)
                turn = "player"
    else:
        print(Fore.RED + "\nERROR /// WRONG CODE /// RUN. GET OUT. RUN. COME BACK WITH THE CORRECT CODE. DID YOU FOLLOW THE INSTRUCTIONS?")
        time.sleep(5)
        print(f"\n{bold}ǝɹǝɥʍ do ⅄On ʇuɐʍ to oƃ?{end}")
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
    
def ocean(status):
    monster_stats = status['mob']
    player_stats = status['player']
    status['current_enemy'] = status['mob']
    combat_status = {
        "stun_counter": 0,
        "ranged_atk_counter": 0
    }
    # options to go to rockylands, swamp, spawn
    avail_actions = ["walk","fish"]
    bold = '\033[1m'
    end = '\033[0m'
    print("\nThe ocean lurks with fish, bones covered in seaweed, algae, sharp rocks and--is that something in the water..?")
    time.sleep(4)
    if monster_stats['hp'] > 0:
        print(f"AHHHH! That THING in the water was NOT harmless!! {bold}{Fore.GREEN}The Abyssal Echo{end}{Fore.RESET} slithers under your feet and flings you into the air. You barely land back into the water whole.")
        time.sleep(5)
    turn = random.choice([playerTurn, monsterTurn])
    while monster_stats["hp"] > 0:
        if player_stats["hp"] <= 0:
            print(f"{bold}YOU DIED!{end} The Abyssal Echo swallowed you whole.")
            winLose()
            break
        if status['current_enemy'] == None:
            break
        if status['current_loc'] != Locations.OCEAN:
            break
        if monster_stats['hp'] <= 0:
            break
        if turn == "player":
            calc = playerTurn(status, combat_status)
            if calc != "added_turn":
                turn = "monster"
        else:
            monsterTurn(status)
            turn = "player"
    else:
        print("\nIt's alright, the shore doesn't seem too scary..")
        time.sleep(2)
        print("\nYour eye catches an engraved stone near the seashells: 3P\nUhh well alright then.")
        time.sleep(3)
        while True:
            action_choice = input(f"\nWhat would you like to do?\n - {bold}Walk{end} to another location\n - {bold}Fish{end} for health and weapons\n\nEnter the bolded word for your action:\n").strip().lower()
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
        elif action_choice == "fish":
            print("placeholder")
        else:
            print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
        
    #     if player_stats["hp"] <= 0:
    #         print(f"{player_stats['name']} was killed. The Abyssal Echo swallowed you whole.")
    #         break

    # if monster_stats["hp"] <= 0:
    #     print(f"{player_stats['name']} emerged victorious in a gruesome battle against the Abyssal Echo!")

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