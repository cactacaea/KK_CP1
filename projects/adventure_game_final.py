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
    (easymath3, "15"),
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

# lore dialogue

# graveyard

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
    intro = "\nYou get knocked out by what seemed to be a human in a black mask--at least that's what you saw from the corner of your eye.\nAfter an unknown period of time passes, your eyes don't decieve you--you find yourself laying next to a red portal, sluggishly getting the ability to move your muscles and limbs.\nA fellow townsperson runs up to you in fear.\n\n'Kill tha shadwow monstow to save our island!'\n\nThe little boy runs away as your fuzzy brain gains awareness.\nYou spot wooden posts nailed to trees with biome names; maybe they can be your guide...\n"
    directions = f"{bold} - - DIRECTIONS - -{end}\nCollect scrolls from each biome to find the code word. Keep track of clues and line up the number to the letter.\nDon't let your sanity deplete too far.\nScariness may be useful in combat..\nUse your brain.\nPerhaps don't be stupid.\n\n{bold} - - IMPORTANT NOTE - -{end}\nBe careful when reading details! They will help you find the CODE!\n"
    item_lookup = {
        # healing items
        "Wet Orange Blossom": {
            "type": "healing"},
        "Mandrake": {
            "type": "healing"},
        "Cherry Pierogi": {
            "type": "healing"},
        "Bottle of Orange Soda": {
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
        "Sharpened Stick": 5, # in desert DONE
        "Bone Shard": 10, # desert DONE
        "Kelp Rope": 8, # ocean DONE
        "Spear": 16, # crafted in rockylands DONE
        "Obsidian Shard": 6, # graveyard DONE
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
        "hp": 155,
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
        "hp": 160,
        "attacking_damage": 20, # print ~20 + weapon
        "defense": 8,
        "sanity": 100,
        "scariness": 1,
        "inventory": []
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
        "available_graveyard_trinkets": ["lore",
                                         "Bowl",
                                         "lore",
                                         "Ruby",
                                         "Frazzled Wire",
                                         "Garden Gnome",
                                         "lore",
                                         "Obsidian Shard",
                                         "Ship in a Bottle",
                                         "lore",
                                         "lore",],
        "available_ocean_stuff": ["Kelp Rope",
                                  "Mandrake",
                                  "Bottle of Orange Soda",
                                  "Wet Orange Blossom",
                                  "Cherry Pierogi",
                                  "Tuna",
                                  "Salmon",
                                  "Cod"
        ],
        "available_desert_stuff": ["Sand Bag",
                                   "lore",
                                   "Bone Shard",
                                   "Sand Bag",
                                   "lore",
                                   "lore",
                                   "lore"]
    }

    display_stats = f"{bold} - - PLAYER STATISTICS - - {end}\nUser: {bold}{player['name']}\n{end}Health: {bold}{player['hp']}{end}\nAttacking Damage: {bold}16-26{end}\nDefense: {bold}{player['defense']}{end}\nSanity: {bold}{player['sanity']}{end}\nScariness: {bold}{player['scariness']}{end}"

    print(intro)
    time.sleep(9) #7
    print(directions)
    time.sleep(9) #7
    print(f"{display_stats}")
    time.sleep(6) #5
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
        combat_choice = input(f"\nIt's your turn to attack! What will you choose to do?\n\n#1: {bold}Normal Attack{end} - Attack with base damage\n#2: {bold}Wild Card{end} - Deal double damage to enemy but you also take damage\n#3: {bold}Stun{end} - Single use; normal attack damage, alonside giving yourself another turn {Fore.LIGHTRED_EX}{bold}if the stun ability is unlocked at 3 Scariness{end}{Fore.RESET}\n#4: {bold}Healing{end} - Gain 10 health if you collected healing resources and give yourself another turn\n#5: {bold}Ranged Attack{end} - Throw rocks, berries, sand bags, acorns, or mushrooms at enemy if you collected said resources, recieve another turn; low damage and 4 uses\n#6: {bold}Flee{end} - Abyssal Echo only, 50/50 chance of losing health or exiting the combat sequence.\n\nEnter your choice as a number:\n")
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
        player_stats["hp"] = min(player_stats["hp"] + 10, 150)
        inventory.remove(used_item)
        print(f"You used {used_item} and gained 10 HP! (IF you weren't already at 150..)")
        return "added_turn"
    # 5 ranged attack
    elif combat_choice == "5":
        
        ranged_items = [item for item in inventory if item in item_lookup and item_lookup[item]["type"] == "ranged"]
        if not ranged_items:
            print("You have no projectiles to throw.. Turn skipped.")
            return "end"
        if combat_status['ranged_atk_counter'] > 4:
            print("\nAlready used your ranged attacks!")
        else:
            used_item = random.choice(ranged_items)
            combat_status["ranged_atk_counter"] += 1
            dmg = random.randint(8,14)
            monster_stats["hp"] -= dmg
            inventory.remove(used_item)
            print(f"You throw a {used_item} for {dmg} damage and stun your enemy!")
            print(Fore.BLUE + f"\n{monster_stats['name']}: {monster_stats["hp"]} HP")
            print(Fore.BLUE + f"{player_stats["name"]}: {player_stats["hp"]} HP")
            time.sleep(2)
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
    avail_actions = ["walk","search"]
    print("\nThe grasslands are bare, but..who doesn't like soft, bright green grass? You spot friendly rabbits who run away as you inch closer to them.")
    time.sleep(3.5)
    while True:
        action_choice = input(f"\nWhat would you like to do?\n - {bold}Walk{end} to another location\n - {bold}Search{end} for a scroll\n\nEnter the bolded word for your action:\n").strip().lower()
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
                print("\nJackpot! Papers flutter down as the last puzzle piece you placed unhooked the wooden board. Trying to pick one up, you get exactly the scroll you needed")
                print(f"-,-^~`_`*.{Fore.GREEN}{bold}5Y{end}{Fore.RESET}")
                time.sleep(5)
                break
            else:
                print("A rabbit bites your ankle thinking it's grass--you took too long, bud!\n-5 Health")
                player_stats['hp'] -= 5
                break
    else:
        print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")

def deciduousForest(status):
    # options to go to spawn, graveyard, desert
    player_stats = status['player']
    inventory = player_stats['inventory']
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","chop","pick","search"]
    print("\nThe deciduous forest features bright orange trees and dried mud. What a lovely place for trees.")
    time.sleep(3.5)
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
        print("\nWood might be handy for the villagers. Chop in 2 directions at a time using WASD.")
        while True:
            times = random.randint(5,6)
            directions = {
                "up": "w",
                "down": "s",
                "left": "a",
                "right": "d"}
            for i in range(times):
                direction = random.choice(list(directions.keys()))
                direction2 = random.choice(list(directions.keys()))
                correct_key = directions[direction]+directions[direction2]
                print(f"\nSwing your axe {direction.upper()} and {direction2.upper()}!")
                key_choice = input().lower().strip()
                if key_choice == correct_key:
                    print(f"\n{bold}*CREAK*{end}")
                else:
                    print("\nYou nearly fall back! Getting your composure together...-2 Sanity.")
                    time.sleep(4)
                    player_stats['sanity'] -= 2
            print("\nThe log breaks off! +0.2 scariness.")
            time.sleep(1.5)
            inventory.append("Log")
            player_stats['scariness'] = min(player_stats['scariness'] + .2,3)
            while True:
                again = input("\nYes/No - Chop again?:\n").lower().strip()
                if again == "yes":
                    print("\nYou walk to another log rotting on the ground")
                    break
                elif again == "no":
                    return
                else:
                    print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
    elif action_choice == "pick":
        print("\nWalk and pick mushrooms in the correct direction using WASD.")
        while True:
            times = random.randint(3,4)
            directions = {
                "forward": "w",
                "back": "s",
                "left": "a",
                "right": "d"}
            for i in range(times):
                direction = random.choice(list(directions.keys()))
                correct_key = directions[direction]
                print(f"\nWalk {direction.upper()}!")
                key_choice = input().lower().strip()
                if key_choice == correct_key:
                    print(f"\n{bold}*yoink*{end}")
                else:
                    print("You step on a thorn!... -1 Health")
                    time.sleep(3)
                    player_stats['hp'] -= 1
            print("\nYou pick the best mushroom out of your crusty batch and gain 0.03 scariness.")
            time.sleep(1.5)
            inventory.append("Mushroom")
            player_stats['scariness'] = min(player_stats['scariness'] + 0.03,3)
            while True:
                again = input("\nYes/No - Pick again?:\n").lower().strip()
                if again == "yes":
                    print("\nYou walk over to another batch of mushrooms")
                    break
                elif again == "no":
                    return
                else:
                    print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
    elif action_choice == "search":
        print(f"\nFull of oddities, this island is. Just an hour of wandering you see a raccoon barely chewing a scroll paper,\nit looked as if it said something like {Fore.LIGHTYELLOW_EX}{bold}'7S'{end}{Fore.RESET}\nWait..?--")
        time.sleep(3)
    else:
        print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")

def swamp(status):
    weapon_name = status["weapon"]
    weapon_dmg = status["weapon_lookup"].get(weapon_name, 0)
    attacking_dmg = 20 + weapon_dmg
    player = status['player']
    inventory = player['inventory']
    # options to go to spawn, ocean, stalagmite terrain
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","search","socialize","view"]
    print("\nMucky dirt puddles reek of animal manure. A mosquito lands on you--followed by a few more flies as you swat them. Lit up houses are spotted from afar.\nGrass and weeds build up on your legs every time you take a step.")
    time.sleep(4)
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
        print(f"\nA fellow villager, though dirty in mud and raspberry jam--which looks incredibly appetizing--hands you a recipe book for future reference\nThat is, if you make it out of this place alive. One page mentions {bold}{Fore.CYAN}'R6'{end}{Fore.RESET} for.. no reason? Or maybe uhm..who knows..")
        time.sleep(7)
    elif action_choice == "socialize":
        print("\nMade up of black-brown wood and stone covered in moss, happy citizens of a small town are seen running errands and enjoying their life.\nYou spot two villagers chatting near a dock who you might be interested in talking to.")
        time.sleep(5)
        villager_choice = input(f"\n(Enter their name.)\nWould you like to walk up to..\n- {bold}Gary{end} the wood carver\n- {bold}Wilson{end} the trinket collector\n\n?: ").lower().strip()

        if villager_choice == "gary":
            log_amount = inventory.count("Log")

            print(f"\n{bold}Gary:{end} Aye bud! Do you happen to have any logs? They from theh.. deciduo-whatever forest, you get me?\nI might give yeh.. sum nice in return..?")
            time.sleep(2)
            if log_amount == 0:
                print(f"{bold}Gary:{end} Agh.. shame. Come back if you chop some trees, yeah?")
                time.sleep(4)
                return
            while True:
                give_logs = input(f"\nYes/No - Give Gary your logs? You have {log_amount}.\n?: ").lower().strip()
                if give_logs == "no":
                    print(f"{bold}Gary:{end} Ah shucks. Well, no worries, I mean. Who needs wood?")
                    return
                elif give_logs == "yes":
                    for smth in range(log_amount):
                        inventory.remove("Log")
                    heal_amount = log_amount * 10
                    player["hp"] = min(player["hp"] + heal_amount, 160)
                    print(f"\n{bold}Gary:{end} Oy thank you lad! These are bound to give me more resources to carve useless things..! COUGH. I meant, provide wood for the people!\n{Fore.GREEN}+{heal_amount} Health{Fore.RESET}")
                    time.sleep(4)
                    return
                else:
                    print(f"\n{bold}Gary:{end} Oh c'mon that's not a straight up answer!")

        elif villager_choice == "wilson":
            trinkets = []
            for item in inventory:
                if item == "Garden Gnome" or item == "Ruby" or item == "Frazzled Wire" or item == "Ship in a Bottle" or item == "Bowl":
                    trinkets.append(item)

            print(f"\n{bold}Wilson:{end} Ooooh. You look like someone who digs graves.")
            time.sleep(2)
            if not trinkets:
                print(f"{bold}Wilson:{end} Aye!! No trinkets?? Come back when you finished searching for ghosts.")
                time.sleep(4)
                return
            while True:
                give_trinkets = input(f"\nYes/No - Give Wilson your trinkets? You have {len(trinkets)}.\n?: ").lower().strip()
                if give_trinkets == "no":
                    print(f"{bold}Wilson:{end} That's not nice. But I'll wait.")
                    return
                elif give_trinkets == "yes":
                    for item in trinkets:
                        inventory.remove(item)
                    heal_amount = len(trinkets) * 10
                    player["hp"] = min(player["hp"] + heal_amount, 160)
                    print(f"\n{bold}Wilson:{end} Ehheheheheh! Thanks mate!\n{Fore.GREEN}+{heal_amount} Health{Fore.RESET}")
                    time.sleep(4)
                    return
                else:
                    print(f"\n{bold}Wilson:{end} Oh, give me a straightforward answer.")
        else:
            print(Fore.RED + "\nYou wander off as they fail to notice.")
    elif action_choice == "view":
        print("\nYou find a swirly rock amidst an ant hill. It's a pretty rock, really--though trying to extract it from the muck, all your items fly out from your pockets.\nEverything floats in front of you to observe.\n")
        time.sleep(4)
        print(f"{bold} - - - PLAYER STATISTICS - - - {end}\nUser: {bold}{player['name']}\n{end}Health: {bold}{player['hp']}{end}\nAttacking Damage: {bold}~{attacking_dmg}{end}\nDefense: {bold}{player['defense']}{end}\nSanity: {bold}{player['sanity']}{end}\nScariness: {bold}{player['scariness']:.2f}{end}")
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
    inventory = player_stats['inventory']
    # options to go to deciduous forest, rockylands, spawn
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","search","dig"]
    avail_trinkets = status["available_graveyard_trinkets"]
    graveyard_lore = {
        "1": "They're all.. unconscious",
        "2": "That name is scratched out again, and again, and again, and again, and--who can hate a person that much?",
        "3": "The loot senses are tingling",
        "4": "Do the dead REALLY remember more than the living?",
        "5": "Why's there just a big 'W' etched in it"
    }
    print("\nYou feel the presence of spirits as you walk by each grave. The graveyard feels uncomfortable and bare.\nAlthough, perhaps it's more interesting at a second glance. We don't judge books by their covers here.")
    time.sleep(4)
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
                print(f"`-_`*~~_`/{Fore.BLACK}{bold}E2{end}{Fore.BLACK}")
                time.sleep(5)
                break
            else:
                print("Felt like a spirit bit your ankle for not paying attention. Oh well, maybe -5 health or so")
                player_stats['hp'] -= 5
                break
    elif action_choice == "dig":
        print("\nYou grab a rusty shovel laying to the side. Dig in the correct direction using WASD.")
        while True:
            if not avail_trinkets:
                print("\nYou already dug up all of the graves and find nothing.")
                return
            random_trinket = random.choice(avail_trinkets)
            directions = {
                "up": "w",
                "down": "s",
                "left": "a",
                "right": "d"}
            for i in range(5):
                direction = random.choice(list(directions.keys()))
                direction2 = random.choice(list(directions.keys()))
                direction3 = random.choice(list(directions.keys()))
                direction4 = random.choice(list(directions.keys()))
                correct_key = directions[direction] + directions[direction2] + directions[direction3] + directions[direction4]
                print(f"\nSwing your shovel {direction.upper()}, {direction2.upper()}, {direction3.upper()}, {direction4.upper()}!")
                key_choice = input().lower().strip()
                if key_choice == correct_key:
                    print(f"\n{bold}*SCHCK*{end}")
                else:
                    print("Your shovel got stuck! You struggle yanking it from the dirt... -4 Health")
                    time.sleep(3)
                    player_stats['hp'] -= 4

            if random_trinket == "lore":
                lore_key, lore_text_value = random.choice(list(graveyard_lore.items()))
                print(f"\nYou dig up.. something? Uhhh:\n'{lore_text_value}'")
                graveyard_lore.pop(lore_key)
                avail_trinkets.remove("lore") 

            elif random_trinket == "Obsidian Shard":
                print("\nYou dug up a weapon! OBSIDIAN SHARD: +6 Attacking Damage")
                if status['weapon'] is not None:
                        replace = input(f"\nYes/No - You're currently wielding: {status['weapon']}. Would you like to replace it?:\n").lower().strip()
                        if replace == "yes":
                            player_stats["weapon"] = "Obsidian Shard"
                            print("\nObsidian Shard equipped. +6 Attacking Damage given.")
                            avail_trinkets.remove("Obsidian Shard")
                        else:
                            print("\nYou keep your weapon and chuck the sharp slice of obsidian back into the dirt. Oh well.")
                else:
                    status['weapon'] = "Obsidian Shard"
                    print("\nYou didn't find any weapons so far, so.. you grab the obsidian shard to your advantage!\nYou grant +6 base attacking damage")
                    avail_trinkets.remove(random_trinket)
                    time.sleep(3)
            else:
                print(f"\nYou find: a {bold}{random_trinket}{end}! Might be handy to give to someone..")
                inventory.append(random_trinket)
                avail_trinkets.remove(random_trinket)
                time.sleep(1.5)
                player_stats['scariness'] = min(player_stats['scariness'] + 0.2,3)
            while True:
                    again = input("\nYes/No - Continue digging?:\n").lower().strip()
                    if again == "yes":
                        print("\nYou walk over to another grave.")
                        break
                    elif again == "no":
                        return
                    else:
                        print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")           
    else:
        print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")

def desert(status):
    avail_trinkets = status['available_desert_stuff']
    desert_lore = {
        "1": "How does anything grow in this climate!",
        "2": "Endless sand, endless possibilty.",
        "3": "You're watched. But by time. Not eyes. Just uhh. Keep that in mind, 'kay?",
        "4": "Hey so. There might be a shadow behind you for a moment every now and then if you're going insane. Just for a moment though. That's long enough."
    }
    player_stats = status['player']
    inventory = player_stats['inventory']
    # options to go to forest, spawn, grasslands
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","search","seek","dig","forge"]
    print("\nTemples, wells, and mounds of sand make up a scorching desert. Cacti and sticks in the ground seem useless.\nYour bare feet warm up as you explore the dry land.")
    time.sleep(4)
    while True:
        action_choice = input(f"\nWhat would you like to do?\n - {bold}Walk{end} to another location\n - {bold}Search{end} for a scroll\n - {bold}Seek{end} for weapons and lore fragments in the sand\n - {bold}Dig{end} for semi unbroken and useful sticks\n - {bold}Forge{end} collected sticks\n\nEnter the bolded word for your action:\n").strip().lower()
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
                print(f"\nAfter painful thinking and sitting in the sand until the day got cold, you\nfinally swipe away some sand and find the letter you needed..\nThe board opens up and gives you a scroll; {bold}{Fore.YELLOW}4H{end}{Fore.RESET}")
                time.sleep(7)
                break
            else:
                print("\nYikes, you stubbed your toe getting up to leave, disappointed. Be more focused on writing next time\n-5 Health")
                player_stats['hp'] -= 5
                time.sleep(2)
                break
    elif action_choice == "seek":
        print("\nFinding a decent mount of sand, you wonder if it's not a bad idea to jump and dig around in it. You jump.\nWeeeeeh! Dig in the correct direction using WASD.")
        while True:
            if not avail_trinkets:
                print("\nThere doesn't look to be anything in the sand")
                return
            random_trinket = random.choice(avail_trinkets)
            directions = {
                "up": "w",
                "down": "s",
                "left": "a",
                "right": "d"}
            for i in range(3):
                direction = random.choice(list(directions.keys()))
                direction2 = random.choice(list(directions.keys()))
                direction3 = random.choice(list(directions.keys()))
                direction4 = random.choice(list(directions.keys()))
                correct_key = directions[direction] + directions[direction2] + directions[direction3] + directions[direction4]
                print(f"\nMove {direction.upper()}, {direction2.upper()}, {direction3.upper()}, {direction4.upper()}!")
                key_choice = input().lower().strip()
                if key_choice == correct_key:
                    print(f"\n{bold}*sand noises*{end}")
                else:
                    print("Is that a spider?! You struggle trying to smack it.. The guts soak into the sand. Eugh!... -5 Health")
                    time.sleep(3)
                    player_stats['hp'] -= 5

            if random_trinket == "lore":
                lore_key, lore_text_value = random.choice(list(desert_lore.items()))
                print(f"\nYou find a piece of paper:\n'{lore_text_value}'")
                desert_lore.pop(lore_key)
                avail_trinkets.remove("lore") 

            elif random_trinket == "Bone Shard":
                print("\nYou dug up a weapon! BONE SHARD: +10 Attacking Damage")
                if status['weapon'] is not None:
                        replace = input(f"\nYes/No - You're currently wielding: {status['weapon']}. Would you like to replace it?:\n").lower().strip()
                        if replace == "yes":
                            player_stats["weapon"] = "Bone Shard"
                            print("\nBone Shard equipped. +10 Attacking Damage given.")
                            avail_trinkets.remove("Bone Shard")
                        else:
                            print("\nYou keep your weapon and chuck the bone away. Who cares.")
                else:
                    status['weapon'] = "Bone Shard"
                    print("\nNo weapons. Yikes. Grabbing the bone shard might be an okay idea for now.\nYou grant +10 base attacking damage")
                    avail_trinkets.remove(random_trinket)
                    time.sleep(3)
            else:
                print(f"\nYou find: a {bold}{random_trinket}{end}! Handy in combat?..")
                inventory.append(random_trinket)
                avail_trinkets.remove(random_trinket)
                time.sleep(1.5)
                player_stats['scariness'] = min(player_stats['scariness'] + 0.2,3)
            while True:
                    again = input("\nYes/No - Continue digging?:\n").lower().strip()
                    if again == "yes":
                        print("\nYou look around for more sand mounds.")
                        break
                    elif again == "no":
                        return
                    else:
                        print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
       
    elif action_choice == "dig":
        print("\nUpon seeing a pile of sand and sticks, your silly brain is drawn to collecting them. Dig in 2 directions at a time using WASD.")
        while True:
            times = random.randint(5,6)
            directions = {
                "up": "w",
                "down": "s",
                "left": "a",
                "right": "d"}
            for i in range(times):
                direction = random.choice(list(directions.keys()))
                direction2 = random.choice(list(directions.keys()))
                correct_key = directions[direction]+directions[direction2]
                print(f"\nMove your arms {direction.upper()} and {direction2.upper()}!")
                key_choice = input().lower().strip()
                if key_choice == correct_key:
                    print(f"\n{bold}*HAPPY SAND NOISES*{end}")
                else:
                    print("\nYou step into a hole with rocks on accident! You struggle getting your mind together whilst standing up...-2 Sanity.")
                    time.sleep(4)
                    player_stats['sanity'] -= 2
            print("\nYou finally yank the stick from the heavy sand! +0.2 scariness.")
            time.sleep(1.5)
            inventory.append("Stick")
            player_stats['scariness'] = min(player_stats['scariness'] + .2,3)
            while True:
                again = input("\nYes/No - Dig again?:\n").lower().strip()
                if again == "yes":
                    print("\nYou walk to the bunch of thorns sticking out of the ground")
                    break
                elif again == "no":
                    return
                else:
                    print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
    elif action_choice == "forge":
        print("\nYou find some dry rope in the sand at an attempt to forge the twigs into something better. All you need is 2 sticks")
        time.sleep(6)
        while True:
            choice = input("\nYes/No - Do you wish to proceed in crafting?:\n").strip().lower()
            if choice == "no":
                print("\nYou chose to stray from using your precious items.")
                break
            elif choice == "yes":
                print("\nChecking for necessary items...")
                time.sleep(2)
                sticks = inventory.count("Stick")
                if sticks >= 2:
                    inventory.remove("Stick")
                    inventory.remove("Stick")
                    print("\nYou have the resources required. You tie some rope carefully around the twigs and use the small blade from a while ago to sharpen the end of it.\nSHARPENED STICK: +5 Attacking Damage")
                    if status['weapon'] is not None:
                        replace = input(f"\nYes/No - You're currently wielding: {status['weapon']}. Would you like to replace it?:\n").lower().strip()
                        if replace == "yes":
                            player_stats["weapon"] = "Sharpened Stick"
                            print("\nPointy stick equipped. +5 Attacking Damage given.")
                        else:
                            print("\nYou decide to keep your weapon and snap the twig in pieces")
                    else:
                        status['weapon'] = "Spear"
                        print("\nSince your pockets are empty of weapons, you grab the spear to your advantage.\nYou grant +16 base attacking damage")
                        time.sleep(4)
                else:
                    print("\nYou don't have enough materials, silly. You chuck the rope away in annoyance, alerting a snake in the process\nIt bites your pinky toe. -3 Health.")
                    player_stats['hp'] -= 3
                    time.sleep(3.5)
                break
            else:
                print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
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
    time.sleep(3.5)
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
                print(f"\nA scroll falls from a nearby edge; {Fore.LIGHTBLACK_EX}{bold}Z1{end}{Fore.RESET}")
                time.sleep(5)
                break
            else:
                print("You were caught doing 'magic.' Just because of easy math. Ridiculous. You run away before anything else happens. Better luck next time--be sneaky alright?? -5 Health")
                player_stats['hp'] -= 5
                break
    elif action_choice == "build":
        print("\nSpotting a wooden block from afar, on approach you notice that it has a 3x3 grid. A fascinating, magic crafter!\nUpon touching it, several objects are yoinked from your hands and pockets\nYou need 2 rocks and a stick to make a spear. Might be useful in combat if you have the resources.")
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
                    print("\nYou have the resources required! The crafter wobbles as a spear comes together. SPEAR: +16 Attacking Damage")
                    if status['weapon'] is not None:
                        replace = input(f"\nYes/No - You're currently wielding: {status['weapon']}. Would you like to replace it?:\n").lower().strip()
                        if replace == "yes":
                            player_stats["weapon"] = "Spear"
                            print("\nSpear equipped. +16 Attacking Damage given.")
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
        print("\nYou pick up the pickaxe laying amongst the boulders. Swing in the correct direction using WASD.")
        while True:
            times = random.randint(8,10)
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
                    print("Your foot slipped! You struggle getting up for a bit... -2 Sanity")
                    time.sleep(3)
                    player_stats['sanity'] -= 2
            print("\nThe boulder cracks apart! You pick up a decent rock and gain 0.2 scariness.")
            time.sleep(1.5)
            inventory.append("Rock")
            player_stats['scariness'] = min(player_stats['scariness'] + 0.2,3)
            while True:
                again = input("\nYes/No - Mine again?:\n").lower().strip()
                if again == "yes":
                    print("\nYou walk over to another rock.")
                    break
                elif again == "no":
                    return
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
        if monster_stats['hp'] <= 0:
            print(f"\n{Fore.LIGHTMAGENTA_EX}{bold}CONGRATULATIONS! YOU DEFEATED THE SHADOW GUARDIAN IN A GRUESOME DUEL AND SAVED THE RETREAT ISLAND'S RESIDENTS!{end}{Fore.RESET}")
            winLose()
    else:
        print(Fore.RED + "\nERROR /// WRONG CODE /// RUN. GET OUT. RUN. COME BACK WITH THE CORRECT CODE. DID YOU FOLLOW THE INSTRUCTIONS?")
        time.sleep(5)
        print(f"\n{bold}ǝɹǝɥʍ do ⅄On ʇuɐʍ to oƃ?{end}")
        options = [
            Locations.SPAWN,
            Locations.GRASSLANDS,
            Locations.SWAMP]
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
    avail_trinkets = status["available_ocean_stuff"]
    monster_stats = status['mob']
    player_stats = status['player']
    inventory = player_stats['inventory']
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
    print(f"\nYour eye catches an engraved stone near the seashells ~ {Fore.BLUE}{bold}3P{end}{Fore.RESET}\nUhh well alright then.")
    time.sleep(3)
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
        print("\nA skeleton of a giant snake lays a few meters away at shore---It's alright, the shore doesn't seem too scary..")
        time.sleep(2)
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
                Locations.SWAMP,
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
        elif action_choice == "fish":
            print("\nA fishing pole lays to the side. Swing and move your reel in 2 directions at a time using WASD.")
            while True:
                if not avail_trinkets:
                    print("\nThere's no movement in the water..")
                    return
                random_trinket = random.choice(avail_trinkets)
                directions = {
                    "up": "w",
                    "down": "s",
                    "left": "a",
                    "right": "d"}
                for i in range(4):
                    direction = random.choice(list(directions.keys()))
                    direction2 = random.choice(list(directions.keys()))
                    
                    correct_key = directions[direction] + directions[direction2]
                    print(f"\nMove {direction.upper()} and {direction2.upper()}!")
                    key_choice = input().lower().strip()
                    if key_choice == correct_key:
                        print(f"\n{bold}*YOUR FISHING LINE GETS PULLED*{end}")
                    else:
                        print("\nAgh! You step into the water from the harsh tug of your fishing line...-2 Sanity.")
                        time.sleep(3)
                        player_stats['sanity'] -= 2

                if random_trinket == "Kelp Rope":
                    print("\nYou dug up a weapon! KELP ROPE: +8 Attacking Damage")
                    if status['weapon'] is not None:
                            replace = input(f"\nYes/No - You're currently wielding: {status['weapon']}. Would you like to replace it?:\n").lower().strip()
                            if replace == "yes":
                                player_stats["weapon"] = "Kelp Rope"
                                print("\nKelp Rope equipped. +8 Attacking Damage given.")
                                avail_trinkets.remove(random_trinket)
                            else:
                                print("\nYou keep your weapon and chuck the tied rope of kelp back into the ocean. Useless!")
                    else:
                        status['weapon'] = "Kelp Rope"
                        print("\nYou didn't find any weapons so far, so.. you grab the kelp to your advantage!\nYou're granted +8 base attacking damage")
                        avail_trinkets.remove(random_trinket)
                        time.sleep(3)
                elif random_trinket == "Tuna" or random_trinket == "Cod" or random_trinket == "Salmon":
                    print(f"\nYou find a {bold}{random_trinket}{end}! It's edible, so you eat it cuz why not. +10 Health")
                    player_stats['hp'] += 10
                    avail_trinkets.remove(random_trinket)
                else:
                    print(f"\nYou find: {bold}{random_trinket}{end}! Might be handy to heal in battle with..")
                    inventory.append(random_trinket)
                    avail_trinkets.remove(random_trinket)
                    time.sleep(1.5)
                while True:
                        again = input("\nYes/No - Continue fishing?:\n").lower().strip()
                        if again == "yes":
                            print("\nYou walk over to a different part of shore.")
                            break
                        elif again == "no":
                            return
                        else:
                            print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
            # print("\nA fishing pole lays to the side. Swing and move your reel in 2 directions at a time using WASD.")
            # while True:
            #     times = random.randint(7,10)
            #     directions = {
            #         "up": "w",
            #         "down": "s",
            #         "left": "a",
            #         "right": "d"}
            #     for i in range(times):
            #         direction = random.choice(list(directions.keys()))
            #         direction2 = random.choice(list(directions.keys()))
            #         correct_key = directions[direction]+directions[direction2]
            #         print(f"\nMove your arms {direction.upper()} and {direction2.upper()}!")
            #         key_choice = input().lower().strip()
            #         if key_choice == correct_key:
            #             print(f"\n{bold}*SOMETHING PULLS ON YOUR FISHING LINE*{end}")
            #         else:
            #             print("\nAgh! You step into the water from the harsh tug of your fishing line...-2 Sanity.")
            #             time.sleep(4)
            #             player_stats['sanity'] -= 2
            #     print("\nYou yank the object from the water! +0.05 scariness.")
            #     time.sleep(1.5)
            #     inventory.append("Stick")
            #     player_stats['scariness'] = min(player_stats['scariness'] + .05,3)
            #     while True:
            #         again = input("\nYes/No - Dig again?:\n").lower().strip()
            #         if again == "yes":
            #             print("\nYou walk to the bunch of thorns sticking out of the ground")
            #             break
            #         elif again == "no":
            #             return
            #         else:
            #             print(Fore.RED + "\nERROR /// INVALID CHOICE /// PLEASE TRY AGAIN.")
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