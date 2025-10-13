from gaming_tools import *
def addc():
    """Adds a creature
    Creature name is randomized
    Creature reach is chosen between short or long
    Creature strength is set between 1 and 10 * 1+number of defeated creatures
    Creature life is set between 1 and 10 * 1+number of defeated creatures"""
    if not is_there_a_creature():
        cname=get_random_creature_name()
        creach=random.choice(["short","long"])
        cstrength=random.randint(1,10)*(1+get_nb_defeated())
        clife=random.randint(1,10)*(1+get_nb_defeated())
        add_creature(cname,creach,cstrength,clife)
        print("A creature has been added (Name:%s Reach:%s Strength:%d Life:%d)"%(cname,creach,cstrength,clife))
        return(cname,creach,cstrength,clife)
    else:
        print("A creature already exists")


addc()
reset_game()
