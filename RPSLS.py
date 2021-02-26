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
    print("=>Player choose", player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(5)
    comp_choice = number_to_name(comp_number)
    print("=>Computer choose", comp_choice)
    difference = (comp_number - player_number) % 5
    return difference      
    
# Game Starts Here!!
player = 0
computer = 0
n = int(input("Enter number of turns:"))
print()
for i in range(n):
    test = input("Enter object:")
    diff = rpsls(test)
    if diff == 0:
        computer = computer + 1
        player = player + 1
        print("***Player and computer tie!***")
        print()
    elif (diff == 1) or (diff == 2):
        computer = computer + 1
        print("***Computer wins!***")
        print()
    else:
        player = player + 1
        print("***Player wins!***")
        print()

print("*********Score Board*********")
print("No of Games Played:",n)
print("Player Score:",player)
print("Computer Score:",computer)

if i == n-1:
    if computer > player:
        print("Computer wins the game over",n,"turns")
    elif player > computer:
        print("Player wins the game over",n,"turns")
    else:
        print("Game is tie over",n,"turns")




