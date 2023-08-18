import random
options = ("rock", "paper", "scissors")
playing = True

while playing:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter Your Choice(rock,paper,scissors): ")

    print("player: "+player)
    print("computer: "+computer)

    if player == computer:
        print("It's a Tie!")
    elif player == "rock" and computer == "scissors":
        print("YOU WIN.")
    elif player == "paper" and computer == "rock":
        print("YOU WIN.")
    elif player == "scissors" and computer == "paper":
        print("YOU WIN.")
    else:
        print("YOU LOST!")

    print("Want to play Again(y/n)?")
    choice = input()
    if not choice == 'y':
        playing = False
print("Thanks for playing.")
