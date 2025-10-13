import gaming_tools
import random


def new_character(character, variety):
    """Create a new player to the game and set team money to 50 for the team
    
    Parameters
    ----------
    character (str): name of the new character 
    type (str): the type of the player who can be 'dwarf', 'elf', 'healer', 'wizard' nor 'necromancer'
    
    """
    gaming_tools.set_team_money(50)
    if gaming_tools.character_exists(character) == True:
        print("This character already exist, please try another one")
    
    
    variety = gaming_tools.get_character_variety(character)
    life = gaming_tools.get_character_life(character)
    reach = gaming_tools.get_creature_reach(character)

    if variety and life  == 'dwarf':
        strength = random.randint(10, 15)
        life = random.randint(10, 15)
    elif variety and life == 'elf':
        strength = random.randint(15, 25)
        life = random.randint(15, 25)
    elif variety and life == 'healer' or 'wizard' or'necromancer' :
        strength = random.randint(5, 15)
        life = random.randint(5, 15)



    gaming_tools.set_character_strength(character, strength)
    gaming_tools.set_character_life(character,life)

    gaming_tools.add_new_character(character,variety,reach,strength,life)


new_character('Test1','elf')
