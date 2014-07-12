
 
import simplegui
import math
import random

#Flag is to Select the last range after the game ends
#default flag value is 1 , for Range[0,100]
secret=0
no_of_guess=0
guess_range100=7
guess_range1000=10
flag=1

def new_game():
   
    print "Welcome! Lets Play Guess the Number"
   
    if(flag==1):
        range100()
    else:
        range1000()
        
            
def range100():
    
    global secret,no_of_guess,flag
    flag=1
    print 
    print "Game Range is [0,100]"
    no_of_guess=guess_range100
    print "No of Guess left:",no_of_guess
    secret=random.randrange(0,100)
    
    

def range1000():
    global secret,no_of_guess,flag
    flag=0
    print
    print "Game Range is [0,1000]"
    no_of_guess=guess_range1000
    print "No of Guess Left:",no_of_guess
    secret=random.randrange(0,1000)
   
    
    
def input_guess(guess):
    global no_of_guess
    
    if( no_of_guess >0 ):
        print 
        print"Guess was ",int(guess)
        if(secret<int(guess)):
            print "Lower!"
            no_of_guess=no_of_guess-1
            print "No of Remaining Guesses:",no_of_guess
        elif(secret>int(guess)):
            print "Higher!"
            no_of_guess=no_of_guess-1
            print "No of Remaining Guesses:",no_of_guess
        else:
            print "Correct!"
            print "Selecting the last range!"
            print
            new_game()
    else:
        print
        print "Game Over, no more guesses Left"
        print "Selecting the last Range"
        print
        new_game()


frame=simplegui.create_frame("Guess_the_Number",200,200)
frame.add_button("Range:0-100",range100)
frame.add_button("Range:0-1000",range1000)
frame.add_input("Guess the Number",input_guess,100)


new_game()
frame.start()

