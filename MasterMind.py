

import random

print("WELCOME TO MASTERMIND, PLAY AT YOUR OWN EXPENSE")
print('\n')

#Randomly chosen colours, which are the answers
def randomcolour():
    colours = ['y','b','r','t','g','w']
    colour1 = random.choice(colours)
    colour2 = random.choice(colours)
    colour3 = random.choice(colours)
    colour4 = random.choice(colours)
    allcolours = (colour1, colour2, colour3, colour4)
    return allcolours

#Main Function which holds users answers, and how many attempts they took (large information contained in this function)
def discolours(colour1, colour2, colour3, colour4):
    print('The colours are: (y)ellow, (b)lue, (r)ed, (t)eal, (g)reen and (w)hite.') # showing the user the different colours to choose from
    print('\n')

#ALLOWING USER TO CHOOOSE THE 4 COLOURS

    #First Colour user chooses
    f = True
    while f == True:
        choice1 = input('Choose your first colour:').lower()
        if choice1 != 'y' and choice1 != 'b' and choice1 != 'r'  and choice1 != 't' and choice1 != 'g' and choice1 != 'w': 
            print('Invalid Input, Please enter the first letter of the available colours')
            print('\n')
        else:
            f = False
            print('\n')

    #Second Colour uses chooses        
    f = True
    while f == True:
        choice2 = input('Choose your second colour: ').lower()
        if choice2 != 'y' and choice2 != 'b' and choice2 != 'r' and choice2 != 't' and choice2 != 'g' and choice2 != 'w':
            print('Invalid Input, Please enter the first letter of the available colours')
            print('\n')
        else:
            f = False
            print('\n')

    #Third Colour user chooses        
    f = True
    while f == True:
        choice3 = input('Choose your third colour: ').lower()
        if choice3 != 'y' and choice3 != 'b' and choice3 != 'r' and choice3 != 't' and choice3 != 'g' and choice3 != 'w':
            print('Invalid Input, Please enter the first letter of the available colours')
            print('\n')
        else:
            f = False
            print('\n')
            
    #Fourth Colour user chooses 
    f = True
    while f == True:
        choice4 = input('Choose your fourth and final colour: ').lower()
        if choice4 != 'y' and choice4 != 'b' and choice4 != 'r' and choice4 != 't' and choice4 != 'g' and choice4 != 'w':
            print('Invalid Input, Please enter the first letter of the available colours')
            print('\n')
        else:
            f = False
            print('\n')

    #Accounting for how many colours user chosen in the correct place, or correct colours but in the wrong place
    correct = 0
    wrongplace = 0
    if colour1 == choice1:
        correct += 1
    elif colour1 == choice2 or colour1 == choice3 or colour1 == choice4:
        wrongplace += 1
    if colour2 == choice2:
        correct += 1
    elif colour2 == choice1 or colour2 == choice3 or colour2 == choice4:
        wrongplace += 1
    if colour3 == choice3:
        correct += 1
    elif colour3 == choice2 or colour3 == choice1 or colour3 == choice4:
        wrongplace += 1
    if colour4 == choice4:
        correct += 1
    elif colour4 == choice1 or colour4 == choice2 or colour4 == choice3:
        wrongplace += 1

    print('Correct colour in the correct place:',correct)        #Telling user how many are in correct place, and incorrect place
    print('Correct colour but in the wrong place:',wrongplace)
    print('\n')
    
    rightwrong = [correct, wrongplace]
    return rightwrong

#Calculating whether user has entered correct colours in the correct places, and if so ending the game with a display showing how many guesses they took
(colour1, colour2, colour3, colour4) = randomcolour()
score = 0
play = True
while play == True:
    (correct ,wrongplace) = discolours(colour1, colour2, colour3, colour4)
    score += 1
    if correct == 4:
        play = False
        print('WINNER, YOU DID IT!')
        print('You took',score,'guesses')  


        
                
