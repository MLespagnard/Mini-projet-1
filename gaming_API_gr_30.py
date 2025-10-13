from gaming_tools import *
import random

def lvl_up(character):
    """Gère l'évolution pour un personnage donné.

    La fonction vérifie si l'équipe possède assez d'argent. Si oui, on retire le montant nécessaire 
    pour effectuer l'action (4 d'or), sinon un message informe que l'équipe ne possède pas assez d'argent.
    On attribue ensuite des bonus sur base de pourcentages :
    - On a 25 % de chances d'obtenir un boost de force (+4)
    - On a 50 % de chances d'obtenir un boost de vie (+2)
    Plusieurs messages apparaissent pour indiquer si les gains ont été atteints.

    Args:
        character (str): nom du personnage ciblé.

    Raises:
        Aucun Raise, la fonction gère elle-même les erreurs qui peuvent avoir lieu.
    """

 # Vérifie que le personnage existe avant de dépenser l'or
    try:

        character_strength = get_character_strength(character)
        character_life = get_character_life(character)
    except ValueError as e:
        print(e)
        return


    money = get_team_money()

# Vérifie si l'équipe est soldable
    if money < 4:
        print("You have not enough money")
    else:
        set_team_money(money - 4)

    # 25%: bonus de force
        if (random.randint(1,4) == 1):
            try:
                set_character_strength(character, character_strength + 4)
                print(f"You win a strength bonus of 4, you now have {character_strength + 4}")
            except ValueError as e:
                print(e)
                return
        else:
            print("You didn't win a strength bonus")
            
    # 50%: bonus de vie
        if (random.randint(1,2) == 1): 
            try:
                set_character_life(character, character_life + 2)
                print(f"You win a life bonus of 2, you now have {character_life + 2}")
            except ValueError as e:
                print(e)
                return
        else:
            print("You didn't win a life bonus")