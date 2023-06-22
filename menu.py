import time
from os import system as x
import random

# ASCII graphics
graphics = [
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    '''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''',
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

# Display graphics with delay
for graphic in graphics:
    for line in graphic.splitlines():
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.01)
        print()
    time.sleep(1)
    x("clear")
    
welcome_text = "WELCOME TO THE GAME OF ROCK PAPER SCISSORS"
for char in welcome_text:
    print(char, end='', flush=True)
    time.sleep(0.01)
print()

# Blink 3 times
for _ in range(3):
    time.sleep(0.5)
    x("clear")
    time.sleep(0.5)
    print(welcome_text)
    time.sleep(0.05)

# Assigning the blank values to the variables
player_name = ""
player_age = ""
total_wins = 0
total_loses = 0
total_draw = 0
player_profile = ""
player_score = ""
choice1 = ""
count = 0
player_data = {}

# The program will continue until the user wants to exit.
while True:
    print('''
    [0] - Exit
    [1] - Play
    [2] - Leaderboard
    [3] - Scoreboard
    [4] - How to Play
    ''')

    option = input("Select an option: ")

    if option == "1":  # Begin the play by choosing option "1"
        total_wins = 0  # Value "0" so that with every new player, variables are initialized or set as default.
        total_loses = 0
        total_draw = 0

        print("\nGame Begins!:")
        player_name = input("\nEnter Your Name: ")
        player_age = input("\nEnter Your Age: ")

        input()
        x("clear")
        print('''
        Game On!
        Enter your choice from Rock, Paper, Scissors

        ''')

        while True:
            choice1 = [
                "Rock",
                "Paper",
                "Scissors",
            ]  # Option for random choice.
            computer_choice1 = random.choice(choice1)  # Randomly select an option for the computer
            player_choice = input("Enter your choice: ").capitalize()
            print("Computer Choice: ", computer_choice1)

            # Comparing the player_choice and computer_choice to determine the outcome (win, lose, or draw).
            if (
                (player_choice == "Rock" and computer_choice1 == "Scissors")
                or (player_choice == "Scissors" and computer_choice1 == "Paper")
                or (player_choice == "Paper" and computer_choice1 == "Rock")
            ):
                print("\nYou Win!")
                total_wins += 1
            elif (
                (computer_choice1 == "Rock" and player_choice == "Scissors")
                or (computer_choice1 == "Scissors" and player_choice == "Paper")
                or (computer_choice1 == "Paper" and player_choice == "Rock")
            ):
                print("\nComputer Wins.")
                total_loses += 1
            elif computer_choice1 == player_choice:
                print("\nIt's a Draw!")
                total_draw += 1
            else:
                print("\n........................Invalid Input........................")

            # Check if the player wants to continue the game.
            yes_no = input("\nDo you wish to continue: y/n  : ").lower()
            if yes_no == "n":
                print("\nSee You another Time!")
                x("clear")
                break
            else:
                print("\nFeeling lucky?")
                input()
                print("\nGame On!")
                x("clear")

        continue

    elif option == "2":  # Display the highest scoring player by choosing option "2", also some fucked up shit i don't fully understand but it works.
        print("\nAnd the Winner is...\n")

        player_profile = {
            "Player Name": player_name,
            "Total Games": total_wins + total_loses + total_draw,
            "Total Win": total_wins,
        }
        player_data.update({player_name: player_profile})

        most_wins = 0
        top_player = ""

        most_wins = -1
        top_player = ""  # initiate most_wins with a negative value so any positive value encountered in the loop update most_wins

        for player_name1, player_profile1 in player_data.items():
            total_wins = player_profile1.get("Total Win", 0)
            if total_wins > most_wins:
                most_wins = total_wins
                top_player = player_name1

        if most_wins == -1:
            print("No player has won any games yet.")
        else:
            print(f"{top_player} with amazing {most_wins} wins today!\n")

        print("Press any key to continue")
        input()

    elif option == "3":  # Display the scoreboard by choosing option "3"
        print("\n...................... The Scoreboard of the Game: ...................... \n")
        print("{:<15}{:<15}{:<15}{:<15}{:<15}".format("Player", "Total Games", "Total Wins", "Total Loses", "Total Draws"))
        print("-" * 73)

        player_data[player_name] = {
            "Total Games": total_wins + total_loses + total_draw,
            "Total Wins": total_wins,
            "Total Loses": total_loses,
            "Total Draws": total_draw,
        }
        for player_name, player_profile in player_data.items():
            total_games = player_profile["Total Games"]
            total_wins = player_profile["Total Wins"]
            total_loses = player_profile["Total Loses"]
            total_draw = player_profile["Total Draws"]
            print("{:<15}{:<15}{:<15}{:<15}{:<15}".format(player_name, total_games, total_wins, total_loses, total_draw))

    elif option == "4":  # Display the instructions by choosing option "4"
        instructions = '''\nRock, Paper, Scissors is an easy, fast game that everyone probably already knows.
        But if you are new into this, down below you can find basic instructions on how to play it. 

        In rock-paper-scissors, two players will each randomly choose one of three signs: rock, paper, scissors
        Here are the rules that determine which sign beats another:

        - Rock wins over scissors (because rock smashes scissors)
        - Scissors wins over paper (because scissors cut paper)
        - Paper wins over rock (because paper covers rock)

        If both players show the same sign, it's a tie.

        Good luck and enjoy your game!'''

        # Display text gradually using time.sleep()
        for char in instructions:
            print(char, end="", flush=True)
            time.sleep(0.01)

    elif option == "0":
        print("Exiting......")
        break
    else:
        print("Exiting.......")
        break
