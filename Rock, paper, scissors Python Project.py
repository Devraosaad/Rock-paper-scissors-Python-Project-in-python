import random 
print("Welcome to rock , paper ,  scissors  Game!")
choice_1 = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choice_1)
while True:
    player_choice = input("Your turn: ").lower()
        
    if player_choice not in choice_1:
            print("Invalid input! Please enter 'rock', 'paper', or 'scissors'.")
            continue
    
        
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}\n")
    if choice_1 == computer_choice:

      print("the match is tie ")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
    else:
            print("Computer wins!")
        
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
            break
    
    print("\nThanks for playing!")

  