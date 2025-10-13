from gaming_tools import *

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



def necromancer_power(target):
    """Let the necromancer revive the target with 10 points of live for 75 pieces of gold.

    Parameter
    ________
    target : the name of the character we want to revive (str)
    
    """
    
    # Checks if the target exist
    if character_exists(target):
        
        # Checks if the team has enough money (75 gold)
        if get_team_money()>=75:
            
            # Checks if the target is dead
            if character_alive(target)==False :
            
                set_character_life(target,10)
            
                # it cost 75 pieces of gold to use the power
                set_team_money(get_team_money()-75)
            else:
            
                print('The character is not dead. No need to revive.')
        
        else:
            print('Not enough money.')

    else:
        print('The character does not exist.')



def wizard_power(target):
    """Let the wizard reduce the live of the creature  by half for 20 pieces of gold
     
     Parameter
     ___________
     target: the name of the creature (str)
     """
     
     #check if the creature exists
    if creature_exists(target):
        
        # check if the team has enough money.(20 gold)
        if get_team_money()>=20:

            set_creature_life(target,get_creature_life(target)//2)
            #it cost 20 pieces of gold
            set_team_money(get_team_money()-20)
        else:

            print('Not enough money.')
    else:

        print('The creature does not exist.')  



def healer_power(target):
    """Lets the healer heal a character in the team for 10 pieces of gold
    
    Parameter
    __________
    target : the name of the character we heal
    """  
    # Checks if the target exists 
    if character_exists(target):

        #check if the team has enough money (5 gold)
        if get_team_money()>=5:

            #Check if the target is alive
            if character_alive(target):

                set_character_life(target,get_character_life(target)+10)
                #it costs 5 pieces of gold

                set_team_money(get_team_money()-5)
            
            
            else:

                print('The character is dead. Can not heal.')
       
        # Checks if the target is dead
        else:

            print('Not enough money.')
    else: 
        print('The character does not exist.')

