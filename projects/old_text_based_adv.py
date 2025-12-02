# uvu prep crusty text based adventure game

import time
import random

from enum import Enum, auto
from colorama import Fore, Back, Style

# https://www.geeksforgeeks.org/python/print-colors-python-terminal/
# https://www.geeksforgeeks.org/python/enum-auto-in-python/
class Rooms(Enum):
  LOBBY = auto()
  LAVA_CHAMBER = auto()
  ABANDONED_BUNKER = auto()
  BATHROOM = auto()
  REDROOM = auto()
  WARPED_ROOM = auto()
  WARPED_ROOM_CONTINUATION = auto()
  SPIDER_NEST = auto()
  EGG_ROOM = auto()
  TIGHT_CAVE = auto()
  QUEUE = auto()
  FINAL_BOSS_ROOM = auto()

room_names = {
    Rooms.LOBBY: "Lobby",
    Rooms.LAVA_CHAMBER: "Lava Chamber",
    Rooms.ABANDONED_BUNKER: "Abandoned Bunker",
    Rooms.BATHROOM: "Mystery Room",
    Rooms.REDROOM: "Red Room",
    Rooms.WARPED_ROOM: "Warped Room",
    Rooms.WARPED_ROOM_CONTINUATION: "Other Warped Room",
    Rooms.SPIDER_NEST: "Spider Nest",
    Rooms.EGG_ROOM: "Egg",
    Rooms.TIGHT_CAVE: "Tight Cave",
    Rooms.QUEUE: "Queue",
    Rooms.FINAL_BOSS_ROOM: "Finale",
}

# win/lose function
def win():
  return " "

# combat function
bold = '\033[1m'
end = '\033[0m'
def combat(player, enemy):
  turn = player
  other = enemy
  last = ' '

  while player['hp'] > 0 and enemy['hp'] > 0:
    if turn == player:
      move = input("\nDo you want to attack or defend?\n").strip().lower()
    else:
      moves = ["attack", "defense"]
      move = random.choice(moves)

    if move == "attack":
      damage = turn['dmg']
      if last == "defend":
        damage -= enemy['dmg']
        if damage < 0:
          damage = 0
      other['hp'] -= damage
      print(
          f"{bold}{turn['name']}{end} attacked {other['name']}. {other['name']} has {other['hp']} HP."
      )
    elif move == "defend":
      print("\nYou defended!")

    last = move
    if turn == player:
      turn = enemy
      other = player
    else:
      turn = player
      other = enemy
  if player['hp'] < 1:
    print(f"{bold}{player['name']}{end} has been slain by {enemy['name']}.")
  else:
    print(f"{bold}{player['name']}{end} has defeated {enemy['name']}.")

  return player, enemy


# each room is a function
def lobby(state):

  time.sleep(1)
  # get starter items
  # display starting stats
  # try to get out, explain how to win
  bold = '\033[1m'
  end = '\033[0m'
  # ask where do you want to go
  print(f"\n{bold}Where do you want to go?{end} (Enter the number)")
  options = [
      # connected to abandoned bunker, nest, lava chamber, and tight cave
      Rooms.ABANDONED_BUNKER,
      Rooms.SPIDER_NEST,
      Rooms.LAVA_CHAMBER,
      Rooms.TIGHT_CAVE,
  ]
  for i, x in enumerate(options):
    print(f'{i}. {room_names[x]}')
  while True:
    try:
      room_no = int(input('\n?: ').strip())
      state['current_room'] = options[room_no]
    except ValueError and IndexError:
      print("Invalid entry! Try again.")


def spider_nest(state):
  player = state['player']
  # asks abc format questions, else, the player takes damage

  bold = '\033[1m'
  end = '\033[0m'

  # answer - c
  questions1 = f"\n    {bold}Which of these statements about spider silk is FALSE?{end}\nA) It is stronger than steel of the same diameter.\nB) It can stretch up to five times its length.\nC) All spiders use silk only for making webs.\nD) Some spiders use silk to balloon and travel by air.\n"

  # answer - c
  questions2 = f"\n    {bold}In some ecosystems, removing spiders can lead to which of the following consequences?{end}\nA) Increase in crop yields due to fewer pests\nB) Decrease in insect populations\nC) Increase in insects that damage plants\nD) Increased pollination by bees\n"

  # answer - a
  questions3 = f"\n    {bold}The venom of which spider is known for causing necrotic wounds in humans?{end}\nA) Brown recluse\nB) Wolf spider\nC) Black widow\nD) Garden orb-weaver\n"

  # answer - b
  questions4 = f"\n    {bold}Spiders belong to which class of animals?{end}\nA) Insecta\nB) Arachnida\nC) Reptilia\nD) Mollusca\n"

  # answer - d
  questions5 = f"\n    {bold}Which of these body parts is missing in spiders but present in insects?\n{end}A) Thorax\nB) Abdomen\nC) Legs\nD) Antennae"

  questions = [
      (questions1, "c"),
      (questions2, "c"),
      (questions3, "a"),
      (questions4, "b"),
      (questions5, "d"),
  ]

  question, answer = random.choice(questions)
  print(question)
  playerInput = input("Is your answer A, B, C, or D?\n").lower().strip()
  if playerInput == answer:
    print("\nCorrect, you got 15 HP.")
    player['hp'] += 15
  else:
    print("\nError! Wrong answer, you lost 7 HP")
    player['hp'] -= 7

  print(f"Health:{player['hp']}")

  print(f"\n{bold}Where do you want to go?{end} (Enter the number)")
  # connected to lobby and egg
  options = [Rooms.LOBBY, Rooms.EGG_ROOM]
  for i, x in enumerate(options):
    print(f'{i}. {room_names[x]}')
  room_no = int(input('\n?: ').lower().strip())
  state['current_room'] = options[room_no]


def tight_cave(state):
  # connected to queue and lobby
  print('Falling through dozens of rocks...')
  time.sleep(3.5)
  state['current_room'] = Rooms.QUEUE

def queue(state):
  player = state['player']
  # requires 5 keys to fight boss
  if state['keys'] >= 5:
    userQ = input("Would you like to fight the final boss?\n")
    if userQ == "yes":
      state['current_room'] = Rooms.FINAL_BOSS_ROOM
    print(
        f"\n{bold}PLAYER STATS{end}\nHealth: {player['hp']}\nYou can deal {player['dmg']} damage.\nInventory: {player['inventory']}\nKeys Collected: {state['keys']}"
    )
  else:
    print("Nope, you have to prepare more! Go away.")
    time.sleep(2)
    state['current_room'] = Rooms.LOBBY
# connected to bossfight and tight cave


def abandoned_bunker(state):
  bold = '\033[1m'
  end = '\033[0m'
  print(
      f"\nAll you see are remains of furniture.You also spot a door with the letter {bold}'R'{end} on it. Maybe the room has something useful?"
  )

  # connected to lobby and bathroom

  print(f"\n{bold}Where do you want to go?{end} (Enter the number)")
  options = [Rooms.BATHROOM, Rooms.LOBBY]
  for i, x in enumerate(options):
    print(f'{i}. {room_names[x]}')
  room_no = int(input('\n?: ').strip())
  state['current_room'] = options[room_no]

  return " "


def egg_room(state):
  player = state['player']
  print(
      "\nYou sneak past all of the spiders into the sticky, cobweb-filled cave of eggs; you start to feel dizzy.."
  )
  time.sleep(2)
  QNA = input(
      "\n¿ON ɹO SƎ⅄ ¿┴ƎƎℲ ɹIƎH┴ H┴IM Ǝ┴S∀┴ SɹƎpIԀS Op\n").lower().strip()
  if QNA == "yes":
    state['keys'] += 1
    player['dmg'] += 10

    print("\n┴ SI ɹƎ┴┴Ǝ˥ ┴ƎɹƆƎS ɹƎH┴O ƎH┴\n")
    time.sleep(7)
    state['current_room'] = Rooms.LOBBY
    print(
        f"You eventually found a small, secret tunnel back to the lobby; as well as gaining some strength and finding a key. While sneaking through the dark tunnel, you see a faint letter {bold}'A'{end} on the wall."
    )
    time.sleep(7)
    print(
        f"\n{bold}PLAYER STATS{end}\nHealth: {player['hp']}\nYou can deal {player['dmg']} damage.\nInventory: {player['inventory']}\nKeys Collected: {state['keys']}"
    )
    time.sleep(7)
  else:
    player['dmg'] -= 2
    state['keys'] += 1
    print(
        "\nYou fell asleep and later climbed back to the lobby, which took some of your strength.\n"
    )
    time.sleep(7)
    state['current_room'] = Rooms.LOBBY
    print(
        f"{bold}PLAYER STATS{end}\nHealth: {player['hp']}\nYou can deal {player['dmg']} damage.\nInventory: {player['inventory']}\nKeys Collected: {state['keys']}"
    )

  # make scrambled lettered questions (confusion)
  # player finds letter to code

  return " "


def bathroom(state):
  player = state['player']
  bold = '\033[1m'
  end = '\033[0m'
  # player takes damage and gets key
  print(
      "\nThe bathroom? Agh! There are so many germs! That's when it strikes you that you're a germaphobe.. You took 5 points of damage.\n"
  )
  time.sleep(5)
  player["hp"] -= 5
  state["keys"] += 1
  print(
      f"{bold}PLAYER STATS{end}\nHealth: {player['hp']}\nYou can deal {player['dmg']} damage.\nInventory: {player['inventory']}\nKeys Collected: {state['keys']}"
  )

  # connected to bunker
  time.sleep(6)
  state['current_room'] = Rooms.ABANDONED_BUNKER


def final_boss_room(state):
  player = state['player']
  boss = state['boss']

  bold = '\033[1m'
  end = '\033[0m'
  # jeering jeely fight
  print(
      "\nYou slowly walk into the echoey, gloomy, and ginormous cave where the Jeering Jeely lived. Maybe it still lives there.."
  )
  time.sleep(7)
  if boss['hp'] > 0:
    print(
        f"\nThe {boss['name']} appears out of a giant crevice in the wall; a terrifying, giant, mutated bat! Things have gotten serious."
    )
  player, boss = combat(player, boss)

  if player['hp'] <= 0:
    print(Fore.BLUE, f"You were conquered by the {boss['name']}")
    time.sleep(2)
    AGAIN = input("Will you play again?\n").lower().strip()
    if AGAIN == "yes":
      return main()
  else:
    print(
        Fore.BLUE,
        f"\nYou defeated the {boss['name']} in an extraordinary battle and emerged victorious!"
    )
    print(f"Remaining Health : {player['hp']}")
    time.sleep(2)
    AGAIN = input("Will you play again?\n").lower().strip()
    if AGAIN == "yes":
      return main()


def lava_chamber(state):
  player = state['player']
  snake = state['snake']

  bold = '\033[1m'
  end = '\033[0m'
  # snake fight, add key
  print(
      "\nEntering the lava cave, you're struck with an intense wave of heat. The lava chamber is no joke."
  )
  time.sleep(2)
  if snake['hp'] > 0:
    print(
        f"{snake['name']} is seen slithering out of the magma, attacking out of the blue! While barely escaping Fellisio's bite, you see a letter {bold}'S'{end} on its back!"
    )
    player, snake = combat(player, snake)

    if player['hp'] <= 0:
      print(Fore.GREEN, f"You were conquered by {snake['name']}")
      time.sleep(2)
      AGAIN = input("Will you play again?\n").lower().strip()
      if AGAIN == "yes":
        return main()
    else:
      print(Fore.GREEN, "\nYou vanquished the snake and found a key!\n")
      state['keys'] += 1
      time.sleep(5)
      print(
          Fore.WHITE,
          f"{bold}PLAYER STATS{end}\nHealth: {player['hp']}\nYou can deal {player['dmg']} damage.\nInventory: {player['inventory']}\nKeys Collected: {state['keys']}"
      )
      time.sleep(6.5)
  else:
    print(f"The smoldering remains of {snake['name']} lay on the ground.")
    time.sleep(2)
    print(f"\n{bold}Where do you want to go?{end} (Enter the number)")
    options = [Rooms.LOBBY, Rooms.REDROOM, Rooms.WARPED_ROOM]
    for i, x in enumerate(options):
      print(f'{i}. {room_names[x]}')
    room_no = int(input('\n?: ').strip().lower())
    state['current_room'] = options[room_no]

  # connected to lobby, warped room, and redroom


def redroom(state):
  bold = '\033[1m'
  end = '\033[0m'
  # bold letters + key if player answers question about neon element
  redQ = input(
      Fore.RED +
      f"{bold}\nWhat is the atomic number of NEON on the periodic table of elements?{end}\n"
  )
  if redQ == "10":
    state['keys'] += 1
    print("\nYAYAYAYYA! Good job, you earned another key.")
    time.sleep(5)
    state['current_room'] = Rooms.LAVA_CHAMBER
  else:
    print("Oh.. Okay")
    state['current_room'] = Rooms.LAVA_CHAMBER
  # connected to chamber


def warped_room(state):
  player = state['player']
  bold = '\033[1m'
  end = '\033[0m'
  # enter code, if code correct +1 key
  code = input(
      "\nPlease enter the deciphered 4 letter code:\n").strip().lower()
  if code == "rats":
    print(
        f"Congrats! You guessed the code..! You've been awarded 1 key and a {bold}Rusty Fork{end} dealing 15 damage"
    )
    state['keys'] += 1
    player['dmg'] += 15
    player['inventory'].append("Rusty Fork")
    time.sleep(7)
    state['current_room'] = Rooms.LAVA_CHAMBER

  else:
    print("Err.. That's not it! Come back next time?")
    time.sleep(2)
    state['current_room'] = Rooms.LAVA_CHAMBER

    # connected to lava chamber

    pass


room_functions = {
    Rooms.LOBBY: lobby,
    Rooms.LAVA_CHAMBER: lava_chamber,
    Rooms.ABANDONED_BUNKER: abandoned_bunker,
    Rooms.BATHROOM: bathroom,
    Rooms.REDROOM: redroom,
    Rooms.WARPED_ROOM: warped_room,
    #Rooms.WARPED_ROOM_CONTINUATION: warped_room_continuation,
    Rooms.SPIDER_NEST: spider_nest,
    Rooms.EGG_ROOM: egg_room,
    Rooms.TIGHT_CAVE: tight_cave,
    Rooms.QUEUE: queue,
    Rooms.FINAL_BOSS_ROOM: final_boss_room,
}


def main():
  # write an introduction
  bold = '\033[1m'
  end = '\033[0m'
  story = "\nYou go on a hike with your 2 friends, and they dare you to go first through a small tunnel; as you take a few steps into the dark abyss, you feel the ground under your feet disappear. As you open your eyes, you find yourself in a dimly lit cave, sitting in a pool of water.\n \nAfter looking around and acknowledging the fact that you're stuck here, you find 4 different paths to cross."

  instructions = f"Collect keys and survive.\n{bold}HINT:{end} Keep track of letters."
  # make variables for tools/player stats

  player = {
      "name": input("What's your name?\n").capitalize().strip(),
      "hp": 225,
      "dmg": 20,
      "inventory": []
  }
  boss = {"name": f"{bold}Jeering Jeely{end}", "hp": 600, "dmg": 25}
  snake = {
      "name": f"{bold}Fellisio the Snake{end}",
      "hp": 160,
      "dmg": 22,
  }
  current_room = Rooms.LOBBY

  state = {
      'player': player,
      'boss': boss,
      'current_room': current_room,
      'snake': snake,
      'keys': 0
  }

  print(f"{story}\n")
  time.sleep(3)
  print(f"{instructions}\n")
  time.sleep(3)
  (print(
      f"{bold}PLAYER STATS{end}\nHealth: {player['hp']}\nYou can deal {player['dmg']} damage.\nInventory: {player['inventory']}"
  ))

  while True:
    room = state['current_room']
    print(f"You're in the {room_names[room]}")
    time.sleep(1)
    room_function = room_functions[room]
    room_function(state)
main()