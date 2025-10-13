from gaming_tools import *
import random

def lvl_up(character):

    money = get_team_money()

    if money < 4:
        print("You have not enough money")
    else:
        set_team_money(money - 4)

        if (random.randint(1,4) == 1):
            strength = get_character_strength(character)
            set_character_strength(character, strength + 4)
            print(f"You win a strength bonus of 4, you now have {strength + 4}")
        else:
            Print("You didn't win")
        
        if (random.randint(1,2) == 1):
            life = get_character_life(character)
            set_character_life(character, life + 2)
            print(f"You win a life bonus of 2, you now have {life + 2}")
        else:
            print("You didn't win a life bonus")
