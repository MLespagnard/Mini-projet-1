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
    print('The new character have been added and your name is: ', character, '\n Your variety is: ', variety, '\n Your reach is:', reach, '\n Your strength is:', strength, '\n Your life is:', life )

def create_new_creature():

    """Adds a creature. 
    Creature name is randomized.
    Creature reach is chosen between short or long.
    Creature strength is set between 1 and 10 * 1+number of defeated creatures.
    Creature life is set between 1 and 10 * 1+number of defeated creatures.
    """
  
    if not is_there_a_creature():
        creature_name=get_random_creature_name()
        creature_reach=random.choice(["short","long"])
        creature_strength=random.randint(1,10)*(1+get_nb_defeated())
        creature_life=random.randint(1,10)*(1+get_nb_defeated())
        add_creature(creature_name,creature_reach,creature_strength,creature_life)
        print("A creature has been added (Name:%s Reach:%s Strength:%d Life:%d)"%(creature_name,creature_reach,creature_strength,creature_life))
        return(creature_name,creature_reach,creature_strength,creature_life)
    else:
        print("A creature already exists")

def character_alive(character):
    """Checks if the character is alive
    Parameter
    __________
    character: the name of the character (str)
    
    Return
    __________
    result: True if the character is alive ,False otherwise (bool)
    """
    if get_character_life(character)>0:
        return True
    
    else:
        return False

def attack(character:str, creature:str):
    """Manage the combat part

        Parameters
        ------------------
        character: the character that attack (str)
        creature: the creature that is attack (str)

        Note
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
            set_nb_defeated(get_nb_defeated()+1)
            money_win = 40 +(10 * get_nb_defeated())
            set_team_money(get_team_money() + money_win)
            print('the team defeated %s and win %d money' %(creature, money_win))
            return

    if(character_reach == 'long' and creature_reach == 'short'):
        print('%s can\'t reach %S' %(creature, character))

    else:
        life_of_character = get_character_strength(character)
        strength_of_creature = get_creature_strength(creature)

        if(life_of_character > strength_of_creature):
            set_character_life(character, life_of_character - strength_of_creature)
            print('%s attack and %s losse %d hp' %(creature, character, strength_of_creature) )

        else:
            set_character_life(character, -1)
            print("%s is dead" %character)
            
def use_special_power(character,target):
    """Let the character use the special power.
    
    Parameter
    __________
    character : the name of the given character (str)
    target: the name of the target (str)
    
    """
    #First ckeck if the character exists
    
    if character_exists(character):
        #check if the character is alive
        
        type = get_character_variety(character)
        
        if character_alive(character) : 
            
            #check the variety of the character  
            
            if type=='necromancer':
                necromancer_power(target)
            
            elif type =='wizard':
                wizard_power(target)
            
            elif type =='healer':
                healer_power(target)
            else:
                print('The character does not have a special power')
        else:
            print('The character is dead. Can not use special power.')   
    
    else:
        print('The character does not exist.')

def necromancer_power(character):
    """Let the necromancer revive the target with 10 points of live for 75 pieces of gold.

    Parameter
    ________
    character : the name of the character we want to revive (str)
    
    """
    
    # Checks if the target exist
    if character_exists(character):
        
        # Checks if the team has enough money (75 gold)
        if get_team_money()>=75:
            
            # Checks if the target is dead
            if character_alive(character)==False :
            
                set_character_life(character,10)
            
                # it cost 75 pieces of gold to use the power
                set_team_money(get_team_money()-75)
            else:
            
                print('The character is not dead. No need to revive.')
        
        else:
            print('Not enough money.')

    else:
        print('The character does not exist.')

def wizard_power(creature):
    """Let the wizard reduce the live of the creature  by half for 20 pieces of gold
     
     Parameter
     ___________
     target: the name of the creature (str)
     """
     
     #check if the creature exists
    if creature_exists(creature):
        
        # check if the team has enough money.(20 gold)
        if get_team_money()>=20:

            set_creature_life(creature,get_creature_life(creature)//2)
            #it cost 20 pieces of gold
            set_team_money(get_team_money()-20)
        else:

            print('Not enough money.')
    else:

        print('The creature does not exist.')  

def healer_power(character):
    """Lets the healer heal a character in the team for 10 pieces of gold
    
    Parameter
    __________
    target : the name of the character we heal
    """  
    # Checks if the target exists 
    if character_exists(character):

        #check if the team has enough money (5 gold)
        if get_team_money()>=5:

            #Check if the target is alive
            if character_alive(character):

                set_character_life(character,get_character_life(character)+10)
                #it costs 5 pieces of gold

                set_team_money(get_team_money()-5)
                print("The life of this character is now: ", get_character_life(target))
            
            else:

                print('The character is dead. Can not heal.')
       
        # Checks if the target is dead
        else:

            print('Not enough money.')
    else: 
        print('The character does not exist.')

def lvl_up(character:str):
    """Handles the evolution of a given character. (Strength and life bonuses)

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



