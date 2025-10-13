from gaming_tools import *

def attaque(character:str, creature:str):
    """manage the combat part

        parameter
        ------------------
        character: the character that attack (str)
        creature: the crature that is attack (str)

        note
        -----------------
        the creature and the character must exist

    """


    if(not is_there_a_creature()):
        print('there is no creature to attack')
        return
    
    if(not character_exists(character)):
        print('there is no charachter names %s' %(character))
        return
    
    if(not creature_exists(creature)):
        print('there is not creature names %s' %creature)
        return

    creature_reach = get_creature_reach(creature)
    character_reach = get_character_reach(character)
        
    if(creature_reach == 'long' and character_reach == 'short'):
        print("%s can't reach the creatur" %s %(character,creature))

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
            set_character_life(character, 0)
            print("%s is dead" %character)
            #remove character from list
