# KK 2nd, Text Based Adventure Game Final // Project

import random
import time
from enum import Enum, auto

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
    current_loc = Locations.SPAWN
    bold = '\033[1m'
    end = '\033[0m'
    playername = input("Welcome to the Retreat Island! First off we need to get to know you. Enter your name or player username:\n").capitalize().strip()
    intro = "\nYou get knocked out by -----. After an unknown period of time passes, your eyes don't decieve you--you find yourself laying next to a red portal, sluggishly getting the ability to move your muscles and limbs. A fellow townsperson runs up to you in fear.\n\n'Save our island!!'\n\nThe little boy runs away as your fuzzy brain gains awareness. You spot wooden posts nailed to trees with biome names; maybe they can be your guide...\n"
    directions = f"{bold} - - DIRECTIONS - -{end}\nCollect scrolls from each biome to find the code word. Keep trap of clues and line up the number to the letter.\nWatch out for nighttime.\nDon't let your sanity deplete too far.\nScariness may be useful in combat.\nUse your brain.\nPerhaps don't be stupid.\n"
    # CHANGE
    shadow_guardian = {
        "hp": 800,
        "dmg": 30,
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
        "dmg": 22,
        "sanity": 100,
        "scariness": 1,
        "inventory": []
    }
    status = {
        "player": player,
        "boss": shadow_guardian,
        "mob": abyssal_echo,
        "current_loc": current_loc
    }
    display_stats = f"{bold} - - PLAYER STATISTICS - - {end}\nUser: {bold}{player['name']}\n{end}Health: {bold}{player['hp']}{end}\nDamage: {bold}{player['dmg']}{end}\nSanity: {bold}{player['sanity']}{end}\nScariness: {bold}{player['scariness']}{end}"

    print(intro)
    time.sleep(2)
    print(directions)
    time.sleep(1)
    print(f"{display_stats}\n")
    time.sleep(1)
    while True:
        location = status["current_loc"]
        print(f"Current Location: {location_names[location]}")
        time.sleep(1)
        location_function = location_funcs[location]
        location_function(status)

def player_turn(status, night, Time):
    bold = '\033[1m'
    end = '\033[0m'
def monster_turn(status, night, Time):
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
        loc_num = input("\n?: ").strip().lower()
        status['current_room'] = options[loc_num]

def grasslands(status, night, Time):
    # options to go to spawn, stalagmite terrain, desert
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","search","scavenge","unscramble"]
    print("The grasslands feature....")
    action_choice = input(f"What would you like to do?\n - {bold}Walk{end} to another location\n - {bold}Search{end} for a scroll\n - {bold}Scavenge{end} for food and mobs\n - {bold}Unscramble{end} words to find weapons or lore\n\nEnter the bolded word for your action:\n")

def deciduous_forest(status, night, Time):
    # options to go to spawn, graveyard, desert
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","chop","pick","search"]
def swamp(status, night, Time):
    # options to go to spawn, ocean, stalagmite terrain
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","search","socialize"]
def graveyard(status, night, Time):
    # options to go to deciduous forest, rockylands, spawn
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","search","dig"]
def desert(status, night, Time):
    # options to go to forest, spawn, grasslands
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk","search","seek"]
def rockylands(status, night, Time):
    # options to go to ocean, spawn, graveyard
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk"]
def stalagmite_terrain(status, night, Time):
    # options to go to swamp, grasslands, spawn
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk"]
def ocean(status, night, Time):
    # options to go to rockylands, swamp, spawn
    bold = '\033[1m'
    end = '\033[0m'
    avail_actions = ["walk"]

location_funcs = {
    Locations.SPAWN: spawn,
    Locations.GRASSLANDS: grasslands,
    Locations.DECIDUOUS_FOREST: deciduous_forest,
    Locations.SWAMP: swamp,
    Locations.GRAVEYARD: graveyard,
    Locations.DESERT: desert,
    Locations.ROCKYLANDS: rockylands,
    Locations.STALAGMITE_TERRAIN: stalagmite_terrain,
    Locations.OCEAN: ocean
}

main()