# Snake Water Gun Game

import random

def gameWin(comp, you):  # This is a function with name : gameWin
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

# At starting the score is 0.
player_score = 0
computer_score = 0

while True:
    print("\nComputer's Turn: Snake(s) Water(w) or Gun(g)?")
    randomNo = random.randint(1, 3)  # isme 1, 2, 3 mai se randomly ayega bar bar 
    if randomNo == 1:
        comp = "s"
    elif randomNo == 2:
        comp = "w"
    else:
        comp = "g"

    you = input("Player's Turn: Snake(s) Water(w) or Gun(g)? : ")  # Choose g, w, s to play the game
    while you not in ['s', 'w', 'g']:
        you = input("Invalid choice. Please enter Snake(s), Water(w), or Gun(g): ")

    a = gameWin(comp, you)

    print(f"You chose {you}")
    print(f"Computer chose {comp}")

    if a == None:  # it gives output on behave of backend 
        print("The game is a tie!")
    elif a:
        print("You Won!")
        player_score += 1
    else:
        print("You Lose!")
        computer_score += 1

    print(f"Scores: You - {player_score}, Computer - {computer_score}")

    play_again = input("Do you want to play another round? (y/n): ")
    if play_again.lower() != 'y':
        break

print("Game Over!")
print(f"Final Scores: You - {player_score}, Computer - {computer_score}")
 
