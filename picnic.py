# CS161 - HW4: The Picnic Game
# Connor Williams 2021

# Program tells user whether they are bringing the
# correct item to a picnic based on first letter of their name.

# User input is assigned to start_game.
start_game = input("Welcome to the Picnic Game! Press Enter to begin.")

# while loop checks whether user presses 'Enter' to continue the game.
while True:

    # if/else statement requires user to press 'Enter' in order to
    # break the while loop. Otherwise, the user must try again and
    # start_game is re-assigned.
    if start_game == "":
        print("\n")
        break
    else:
        start_game = input("Oops! Press Enter to begin.")

# An empty list is assigned to names.
names = []

# User integer input is assigned to num_of_players.
num_of_players = int(input("How many players? "))

# while loop adds user's input to the 'names' list until
# the num_of_players is reached.
while True:

    # Length of the names list plus 1, assigned to player_number.
    player_number = len(names) + 1

    # if/else statement checks that the length of the names list is
    # less than num_of_players. If true, user input is assigned to
    # add_names and appended to names. Otherwise, the loop breaks.
    if len(names) < num_of_players:

        # player_number is displayed in fstring to indicate which
        # player number the user is naming.
        add_names = input(f"What is the name of Player {player_number}? ")

        # current add_names is added to the names list.
        names.append(add_names)
    else:
        print("Great! That's everyone! Let's play!\n")
        break

# Function allows user to find out whether they can come to the
# picnic based on the item they want to bring.
def picnic_game():

    # for loop traverses the names index in the range of
    # number of players, to be matched with user input.
    for n in range(num_of_players):

        # Current index of names displays in fstring and user input
        # is assigned to picnic_item.
        picnic_item = input(f"{names[n]}, what item will you bring? ")

        # Current index of names is assigned to players.
        players = names[n]

        # if/else statement checks whether the first letter of the
        # picnic_item is equal to the first letter of players.
        if picnic_item[0].lower() == players[0].lower():
            print("You can come!\n")
        else:
            print("Sorry, you can't come.\n")

    # Function is called to check whether user wants to play again.
    play_again()

# Function allows user to input whether they want to play again.
def play_again():

    # 'Yes' or 'No' input assigned to start_over.
    start_over = input("Play again? Yes (y) or No (n): ")

    # while loop checks whether user inputs 'Yes', 'No', nothing
    # or something else and breaks or loops again depending on
    # user input.
    while True:

        # if/elif/else statement breaks the while loop if user enters
        # 'Yes', 'No', or nothing. If 'Yes', the function
        # picnic_game() is called. If 'No' or nothing, the game ends.
        # Otherwise it loops again and start_over is re-assigned.
        if start_over.lower() == "yes" or start_over.lower() == "y":
            print("Great! Let's play!\n")
            picnic_game()
            break
        elif start_over.lower() == "no" or start_over.lower() == "n":
            print("Exiting game. Goodbye.\n")
            break
        elif start_over == "":
            print("Exiting game. Goodbye.\n")
            break
        else:
            print("I'm sorry, try that again.\n")
            start_over = input("Was that a Yes (y) or No (n)? ")

# Calling function at bottom allows user to play the game over and over.
picnic_game()