    
import random

# Initialize scores for both players
player1_score = 0
player2_score = 0
rounds = 0

# Game continues until one player wins 2 rounds or they decide to stop
while rounds < 3:
    rounds += 1
    print(f"\nRound {rounds}:")
    
    # Players roll the dice
    player1_roll = random.randint(1, 6)
    player2_roll = random.randint(1, 6)
    
    print(f"Player 1 rolls: {player1_roll}")
    print(f"Player 2 rolls: {player2_roll}")
    
    # Compare rolls and determine the winner of the round
    if player1_roll > player2_roll:
        print("Player 1 wins the round!")
        player1_score += 1
    elif player2_roll > player1_roll:
        print("Player 2 wins the round!")
        player2_score += 1
    else:
        print("It's a tie, rerolling this round!")
        rounds -= 1  # Decrease the round counter so it doesn't count towards the best of 3
    
    # Display the current scores after each round
    print(f"Current scores - Player 1: {player1_score}, Player 2: {player2_score}")
    
    # Ask if players want to continue or quit after each round
    continue_game = input("Do you want to continue to the next round? (Y/N): ").strip().lower()
    if continue_game != 'y':
        print("Game has been exited.")
        break  # Exit the game if the player does not want to continue

# Determine the overall winner
if player1_score > player2_score:
    print("\nPlayer 1 wins the game!")
elif player2_score > player1_score:
    print("\nPlayer 2 wins the game!")
else:
    print("\nIt's a tie game!")
    