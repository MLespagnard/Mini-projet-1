from gaming_tools import *
import random

def lvl_up(character):
    """Gère l'évolution pour un personnage donné.

    D'abors, la fonction vérifie si l'équipe possède assez d'argent, si oui, 
    on retire 4 d'or à l'équipe et génère aléatoirement avec un pourcentage de
    victoire des gains, 25% de chances d'obtenir 

    Args:
        character (_type_): _description_
    """

    money = get_team_money()

    if money < 4:
        print("You have not enough money")
    else:
        set_team_money(money - 4)

        if (random.randint(1,4) == 1):
            try:
                strength = get_character_strength(character)
            except ValueError as e:
                print(e)
            try:
                set_character_strength(character, strength + 4)
                print(f"You win a strength bonus of 4, you now have {strength + 4}")
            except ValueError as e:
                print(e)

        else:
            print("You didn't win a strength bonus")
            
        if (random.randint(1,2) == 1): 
            try:
                life = get_character_life(character)
            except ValueError as e:
                print(e)
            try:
                set_character_life(character, life + 2)
            except ValueError as e:
                print(e)
            print(f"You win a life bonus of 2, you now have {life + 2}")
        else:
            print("You didn't win a life bonus")

reset_game()
add_new_character("max", "dwarf", "short", 20, 20)
set_character_strength("max", 20)
set_character_strength("max", 10)
set_team_money(50)
lvl_up("max")
