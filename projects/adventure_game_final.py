# KK 2nd, Text Based Adventure Game Final // Project

import random
import time
from enum import Enum, auto

class Locations(Enum):
    SPAWN = 1
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

def main():

def player_turn():

def monster_turn():

def spawn():

def grasslands():

def deciduous_forest():

def swamp():

def graveyard():

def desert():

def rockylands():

def stalagmite_terrain():

def ocean():

location_funcs = {
    Locations.SPAWN: spawn,
    Locations.GRASSLANDS: grasslands,
    Locations.DECIDUOUS_FOREST: deciduous_forest,
    Locations.SWAMP: swamp,
    Locations.GRAVEYARD: graveyard,
    Locations.DESERT: desert,
    Locations.ROCKYLANDS: rockylands,
    Locations.STALAGMITE_TERRAIN: stalagmite_terrain,
    Locations.OCEAN: ocean}
