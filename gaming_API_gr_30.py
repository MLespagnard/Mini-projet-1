from gaming_tools import *

def new_game():
    """Reset all the game and set money to 50 for the team
    """
    reset_game()
    set_team_money(50)



def new_character(character:str, variety:str):
    """Create a new player to the game and set team money to 50 for the team
    
    Parameters
    ----------
    character (str): name of the new character 
    type (str): the type of the player who can be 'dwarf', 'elf', 'healer', 'wizard' or 'necromancer'

    Note
    ----
    The character can't exist 
    
    """

    set_team_money(50)
    if character_exists(character) == True:
        print("This character already exist, please try another one")
    
    
    if variety  == 'dwarf':
        strength = random.randint(10, 15)
        life = random.randint(10, 15)
    elif variety == 'elf':
        strength = random.randint(15, 25)
        life = random.randint(15, 25)
    elif variety == 'healer' or variety == 'wizard' or variety == 'necromancer' :
        strength = random.randint(5, 15)
        life = random.randint(5, 15)

    if variety == 'dwarf' or variety=='healer' or variety=='necromancer':
        reach = 'short'
    elif variety == 'elf' or variety =='wizard':
        reach = 'long'

    add_new_character(character,variety,reach,strength,life)
    print('The new character have been aded and your name is: ', character, '\n Your variety is: ', variety, '\n Your reach is', reach, '\n Your strengh is:', strength, '\n Your life is:', life )


def attack(character:str, creature:str):
    """manage the combat part

        parameter
        ------------------
        character: the character that attack (str)
        creature: the creature that is attack (str)

        note
        -----------------
        the creature and the character must exist
        and the character must be not dead

    """


    if(not is_there_a_creature()):
        print('there is no creature to attack')
        return
    
    if(not character_exists(character)):
        print('there is no charachter names %s' %(character))
        return
    
    if(get_character_life(character) <= 0):
        print("the character %s is dead" %character)
        return
    
    if(not creature_exists(creature)):
        print('there is not creature names %s' %creature)
        return

    creature_reach = get_creature_reach(creature)
    character_reach = get_character_reach(character)
        
    if(creature_reach == 'long' and character_reach == 'short'):
        print("%s can't reach the creatur %s" %(character,creature))

    else:
        life_of_creature = get_creature_life(creature)
        strength_of_character = get_character_strength(character)

        if(life_of_creature > strength_of_character):
            set_creature_life(creature, life_of_creature - strength_of_character)
            print('%s attack and %s losse %d hp' %(character, creature, strength_of_character) )

        else:
            remove_creature(creature)
            set_nb_defeated(get_nb_defeated+1)
            money_win = 40 +(10 * get_nb_defeated)
            set_team_money(get_team_money + money_win)
            print('the team defeated %s and win %d money' %(creature, money_win))
            return

    if(character_reach == 'long' and creature_reach == 'short'):
        print('%s can\'t reach %S' %(creature, character))

    else:
        life_of_character = get_character_strength(character)
        strength_of_creature = get_creature_strength(creature)

        if(life_of_character > strength_of_creature):
            set_character_life(character, life_of_character - strength_of_creature)
            print('%s attack and %s losse %d hp' %(creature, character, strength_of_character) )

        else:
            set_character_life(character, -1)
            print("%s is dead" %character)


