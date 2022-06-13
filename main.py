import random

# Asks user for their name
username = input("What's your name? ").title()

print(f"Hi there, {username}! Let's get right into the game!")

game = True

# Loop for the game
while game == True:

    options = ['R', 'P', 'S']

    # Asks user to choose their option
    user = input("Make a move (R, P or S): ")

    # The CPU chooses a random option
    computer = random.choice(options)

    # Validates the user's input
    if user == "R":
        pass

    elif user == "P":
        pass

    elif user == "S":
        pass

    else:
        print("That's invalid, try again...")
        continue

    # Prints the user and computer's move
    print(f"Player ({user}) : CPU ({computer}).")

    # Compares the moves to determine if it's a tie and restarts the game
    if user == computer:
        print("It's a tie!")
        pass

    # Compares the moves to find a winner
    elif user == "R":
        if computer == "S":
            print(f"{username} wins!")
            break
        else:
            print("CPU wins!")
            break

    elif user == "P":
        if computer == "R":
            print(f"{username} wins!")
            break
        else:
            print("CPU wins!")
            break

    elif user == "S":
        if computer == "P":
            print(f"{username} wins!")
            break
        else:
            print("CPU wins!")
            break

print("Thanks for playing!")
