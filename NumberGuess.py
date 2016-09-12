import random

def start():
    print "I am thinking of a number between 1 and 10..."
    choice = raw_input("Would you like to guess? y/n ")

    if choice == "y":
        print "Yeah!"
        begin()

    if choice == "n":
        print "Bummer...bye then."

    elif choice != "y"+"n":
        choice = raw_input("Please choose either y or n. y/n ") 

def begin():
    from random import randint
    
    randomNumber = randint(1,10)
    guess = raw_input("OK, I have my number, please guess now: 1-10 ")

    if guess == str(randomNumber):
        print "You got it! The number was " + str(randomNumber)
        choice = raw_input("Want to play again? y/n ")

        if choice == "y":
            print "Woohoo!"
            begin()

        if choice == "n":
            print "Thanks for playing."
            exit()

        elif choice != "y"+"n":
            choice = raw_input("Please choose either y or n. y/n ")
            

    if guess != randomNumber:
        print "Nope, that wasn't it, the number was " + str(randomNumber)
        choice = raw_input("Want to play again? y/n ")

        if choice == "y":
            print "Woohoo!"
            begin()

        if choice == "n":
            print "Thanks for playing."
            exit()

        elif choice != "y"+"n":
            choice = raw_input("Please choose either y or n. y/n ")        

start()
