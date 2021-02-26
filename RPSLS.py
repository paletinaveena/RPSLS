# Rock-paper-Scissors-lizard-Spock_game
import random
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
    
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    else:
        return 4
    
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"        
    else:
        return "scissors"


def rpsls(player_choice):
    print()
    print("=>Player choose", player_choice)

    player_number = name_to_number(player_choice)

    comp_number = random.randrange(5)

    comp_choice = number_to_name(comp_number)

    print("=>Computer choose", comp_choice)

    difference = (comp_number - player_number) % 5

    if difference == 0:
        print("***Player and computer tie!***")
    elif (difference == 1) or (difference == 2):
        print("***Computer wins!***")
    else:
        print("***Player wins!***")
        
     
    
# Game Starts Here!!
test = input("Enter object:")
rpsls(test)
