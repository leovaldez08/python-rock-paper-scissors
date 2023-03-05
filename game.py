import random

print("Let's play Rock, Paper, Scissors!")
print("Enter your choice: R for Rock, P for Paper, and S for Scissors.")

choices = ["R", "P", "S"]

player_wins = 0
computer_wins = 0

for round in range(1, 6):
    print(f"\nRound {round}:")

    while True:
        player_choice = input("Your choice: ").upper()
        if player_choice in choices:
            break
        print("Invalid choice. Please try again.")

    computer_choice = random.choice(choices)
    print(f"Computer's choice: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (
        (player_choice == "R" and computer_choice == "S")
        or (player_choice == "P" and computer_choice == "R")
        or (player_choice == "S" and computer_choice == "P")
    ):
        print("You win!")
        player_wins += 1
    else:
        print("Computer wins!")
        computer_wins += 1

    print(f"Score: You {player_wins} - {computer_wins} Computer")

print("\nGame over!")
if player_wins == computer_wins:
    print("It's a tie!")
elif player_wins > computer_wins:
    print("Congratulations, you win the game!")
else:
    print("Sorry, the computer wins the game.")
