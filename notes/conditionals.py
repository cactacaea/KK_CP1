# KK 2nd Conditional Notes

import random
monster_hp = 30
dmg_modifier = 2
atck_bonus = 3
player_hp = 25

# num = float(input("Enter a number: "))

# if num > 0: # if the condition is TRUE
#     print(f"{num} is positive!")
# elif num < 0: # if condition above is FALSE
#     print(f"{num} is negative!")
# else: # if conditions above are ALL FALSE
#     print(f"The number {num} is zero.")

roll = random.randint(1,20)

if roll == 20:
    print("You rolled a crit! That doubles your damage.")
    attack = random.randint(1,8) + random.randint(1,8) + dmg_modifier
    monster_hp -= attack
    print(f"You did {attack} damage to the monster.")
elif roll+atck_bonus > 10:
    print("You hit!")
    attack = random.randint(1,8) + dmg_modifier
    monster_hp -= attack
    print(F"You did {attack} damage to the monster.")
elif roll <= 10:
    if roll == 1:
        print("You rolled a critical failure.. The monster gets a free attack!")
        damage = random.randint(1,10) + 2
        player_hp -= damage
        print(f"You took {damage} damage. You have {player_hp} health.")
    else:
        print("You missed...")
else:
    print("That shouldn't be possible")
print("Your turn is over")

if monster_hp > 0:
    print("It's the monster's turn")
else: print("The monster is dead")