#   Prolog
#   Author: Avity Ngonyani  
#   Email:  avity4585@gmail.com
#   Project:  Rock paper scissors with a computer


import random
print("The Rock Paper Scissors Game")
rock = 1
paper = 2
scissors = 3
userinput = 0
def computerinput(comp_choice):
    if comp_choice == 1:
        print('The computer chooses rock')
    elif comp_choice == 2:
        print('The computer chooses paper')
    elif comp_choice == 3:
        print('The computer chooses scissors')


while userinput != -1:
    comp_choice = random.randint(1, 3)
    userinput = int(input('Please enter 1 for rock, 2 for paper, \n3 for scissors or -1 to quit: '))
    if userinput == 1:
        print('You chose rock')
        computerinput(comp_choice)
        if comp_choice == 1:
            print('The match was a tie!')
        elif comp_choice == 2:
            print('Sorry you lose, try again')
        elif comp_choice == 3:
            print('Congratulations you win!')
    elif userinput == 2:
        print('You chose paper')
        computerinput(comp_choice)
        if comp_choice == 1:
            print('Congratulations you win!')
        elif comp_choice == 2:
            print('The match was a tie!')
        elif comp_choice == 3:
            print('Sorry you lose, try again')
    elif userinput == 3:
        print('You chose scissors')
        computerinput(comp_choice)
        if comp_choice == 1:
            print('Sorry you lose, try again')
        if comp_choice == 2:
            print('Congratulations you win!')
        if comp_choice == 3:
            print('The match was a tie!')
print('Goodbye')