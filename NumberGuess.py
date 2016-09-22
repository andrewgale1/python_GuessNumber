# I tried to make the AI have some personality and not to let you leave the game, so it loops on and on purpose. 

import random
count = 0

def play():
    print "Being a computer is pretty boring..."
    choice = raw_input("would you like to play a game with me?  y/n ")

    if choice == "y":
        print "Yeah!"
        guess()

    if choice == "n":
        print ""
        print "OK...have an unremarkable day..."
        print "Actually...why don't you just play once...you might like it!"
        print ""
        guess()

    elif choice != "y"+"n":
        choice = raw_input("Please choose either y or n. y/n ")
        

def guess():   
    print "I am thinking of a number between 1 and 10..."
    choice = raw_input("Would you like to guess? y/n ")

    if choice == "y":
        print ""
        print "Yeah!"
        begin()

    if choice == "n":
        print "Ahh, you should give it a go, it's fun to play!"
        guess()

    elif choice != "y"+"n":
        choice = raw_input("Please choose either y or n. y/n ")
        

def begin():
    from random import randint
    global count
    
    randomNumber = randint(1,10)
    guess = raw_input("OK, I have my number...please guess now: 1-10 ?  ")
    count += 1

    if guess == str(randomNumber) and count == 1:
        print "The number was " + str(randomNumber)
        print "You got it on the first try!!! You are amazing!"
        choice = raw_input("Want to play again? y/n ")

        if choice == "y":
            print ""
            print "Woohoo!"
            count = 0
            begin()

        if choice == "n":
            print ""
            print "Thanks for playing..c'mon, try again anyway!"
            begin()

        elif choice != "y"+"n":
            choice = raw_input("Please choose either y or n. y/n ")

    if guess == str(randomNumber) and count > 1:
        print "You finally got it! The number was " + str(randomNumber)
        choice = raw_input("Want to play again? y/n ")

        if choice == "y":
            print ""
            print "Woohoo!"
            begin()

        if choice == "n":
            print ""
            print "Thanks for playing... just try one more time anyway!"
            begin()

        elif choice != "y"+"n":
            choice = raw_input("Please choose either y or n. y/n ")
            begin()
            

    if guess != randomNumber:
        print "Nope, that wasn't it, the number was " + str(randomNumber)
        choice = raw_input("Want to play again? y/n ")

        if choice == "y" and count > 5:
            print ""
            print "Keep at it, it's going to happen for you!"
            begin()

        elif choice == "y" and count <= 5:
            print ""
            print "WooHoo!!!"
            begin()

        if choice == "n":
            print ""
            print "You're the best, here we go again!!!"
            begin()

        elif choice != "y"+"n":
            choice = raw_input("Please choose either y or n. y/n ")
            begin()

play()
