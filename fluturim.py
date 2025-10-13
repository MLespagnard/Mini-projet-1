from gaming_tools import * 

reset_game()
def new_character(character, variety):
    """Create a new player to the game and set team money to 50 for the team
    
    Parameters
    ----------
    character (str): name of the new character 
    type (str): the type of the player who can be 'dwarf', 'elf', 'healer', 'wizard' nor 'necromancer'
    
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

new_character('Test1','elf')
