import random

def play():
    print "Being a computer is pretty boring..."
    choice = raw_input("would you like to play a game with me?  y/n ")

    if choice == "y":
        print "Yeah!"
        guess()

    if choice == "n":
        print ""
        print "OK... I don't understand why you'd rather have an unremarkable day.."
        print "..not playing with a sexy computer...but I wish you well."
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
        print "Ahh, you should give it a go, good things can happen!"
        guess()

    elif choice != "y"+"n":
        choice = raw_input("Please choose either y or n. y/n ")
        

def begin():
    from random import randint
    
    randomNumber = randint(1,10)
    guess = raw_input("OK, I have my number...please guess now: 1-10 ?  ")

    if guess == str(randomNumber):
        print "You got it! The number was " + str(randomNumber)
        choice = raw_input("Want to play again? y/n ")

        if choice == "y":
            print ""
            print "Woohoo!"
            begin()

        if choice == "n":
            print ""
            print "Thanks for playing...try one more time, you got this!"
            begin()

        elif choice != "y"+"n":
            choice = raw_input("Please choose either y or n. y/n ")
            

    if guess != randomNumber:
        print "Nope, that wasn't it, the number was " + str(randomNumber)
        choice = raw_input("Want to play again? y/n ")

        if choice == "y":
            print ""
            print "Woohoo!"
            begin()

        if choice == "n":
            print ""
            print "You're the best, here we go again!!!"
            begin()

        elif choice != "y"+"n":
            choice = raw_input("Please choose either y or n. y/n ")        

play()
