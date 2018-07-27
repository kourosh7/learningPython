import random

def isSevenElleven(point):
    dice = die1 + die2
    if dice == 7 or dice == 11:
        return True
    else: 
        return False

def isComeOutCrappedOut(point):
    dice = die1 + die2
    if dice == 3 or dice == 12 or dice == 2:
        return True
    else: 
        return False

def rollDie():
    return random.randint(1,6)

#main
die1 = rollDie()
die2 = rollDie()
point = die1 + die2
print ("First roll was a", point)

if isSevenElleven(point):
    print ("Winner! You rolled a", point)
    #ask to start new game or quit
elif isComeOutCrappedOut(point):
        print ("Loser! You crapped out with", point)
        #ask to start new game or quit
else:
    while True:
        print ("Rolling again!")
        newRoll = rollDie() + rollDie()
        if newRoll == 7:
            print ("Loser! You crapped out with a 7")
            break
        else:
            if newRoll == point:
                print ("Winner! You matched the point", point)
                break