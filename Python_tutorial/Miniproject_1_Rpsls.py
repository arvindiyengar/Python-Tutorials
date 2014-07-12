# Rock-paper-scissors-lizard-Spock 
import math
import random


# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors



def name_to_number(name):
   
    if(name=="rock"):
        return 0
    elif(name=="Spock"):
        return 1
    elif(name=="paper"):
        return 2
    elif(name=="lizard"):
        return 3
    else:
        return 4


def number_to_name(number):
   
    if(number==0):
        return "rock"
    elif(number==1):
        return "Spock"
    elif(number==2):
        return "paper"
    elif(number==3):
        return "lizard"
    else:
        return "scissors"
   

def rpsls(player_choice): 
   
    print "Player choose ",player_choice
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    comp_choice=number_to_name(comp_number)
    print "Computer choose ",comp_choice
    compute=(comp_number-player_number)%5
    if(compute==1 or compute==2):
        print "Computer Wins!"
    elif compute==0:
        print "Computer and player tie!"
    else:
        print "Player Wins!"    
     
    print 
    
   
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


