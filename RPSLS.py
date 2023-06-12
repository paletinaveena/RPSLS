import random

choices = ["rock", "spock", "paper", "lizard", "scissors"]

def determine_winner(player_choice, computer_choice):
    difference = (choices.index(computer_choice) - choices.index(player_choice.lower())) % 5
    if difference == 0:
        return "tie"
    elif difference in [1, 2]:
        return "computer"
    else:
        return "player"

def play_game(num_turns):
    player_score = 0
    computer_score = 0

    for _ in range(num_turns):
        player_choice = input("Enter your choice (rock, spock, paper, lizard, scissors): ")
        computer_choice = random.choice(choices)

        print("=> Player chooses", player_choice)
        print("=> Computer chooses", computer_choice)

        winner = determine_winner(player_choice, computer_choice)

        if winner == "tie":
            player_score += 1
            computer_score += 1
            print("*** It's a tie! ***")
        elif winner == "computer":
            computer_score += 1
            print("*** Computer wins! ***")
        else:
            player_score += 1
            print("*** Player wins! ***")

        print()

    print("********* Score Board *********")
    print("Number of Games Played:", num_turns)
    print("Player Score:", player_score)
    print("Computer Score:", computer_score)

    if computer_score > player_score:
        print("Computer wins the game over", num_turns, "turns")
    elif player_score > computer_score:
        print("Player wins the game over", num_turns, "turns")
    else:
        print("The game is a tie over", num_turns, "turns")

# Game Starts Here!!
num_turns = int(input("Enter number of turns: "))
print()

play_game(num_turns)
