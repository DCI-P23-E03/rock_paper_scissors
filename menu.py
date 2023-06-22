from os import system as x
import random
import time

player_data = {}

while True:
    print('''
    [0] - Exit
    [1] - Play Game
    [2] - Leaderboard
    [3] - Scoreboard
    [4] - How to Play
    ''')

    option = input("Select an option: ")

    if option == "1":
        total_wins = 0
        total_loses = 0
        total_draw = 0

        print("\nGame Starts:")
        player_name = input("\nEnter Your Name: ")
        player_age = input("\nEnter Your Age: ")

        input()
        x("clear")
        print('''
        Let's begin!
        Enter your choice >>> Rock, Paper, Scissors
        ''')

        while True:
            choice1 = [
                "Rock",
                "Paper",
                "Scissors",
            ]
            computer_choice1 = random.choice(choice1)
            player_choice = input("Enter your choice: ").capitalize()
            print("Computer Choice: ", computer_choice1)

            if (
                (player_choice == "Rock" and computer_choice1 == "Scissors")
                or (player_choice == "Scissors" and computer_choice1 == "Paper")
                or (player_choice == "Paper" and computer_choice1 == "Rock")
            ):
                print("\nYOU WIN!")
                total_wins += 1
            elif (
                (computer_choice1 == "Rock" and player_choice == "Scissors")
                or (computer_choice1 == "Scissors" and player_choice == "Paper")
                or (computer_choice1 == "Paper" and player_choice == "Rock")
            ):
                print("\nYou lose, Try again?")
                total_loses += 1
            elif computer_choice1 == player_choice:
                print("\nIt's a draw! Try again?")
                total_draw += 1
            else:
                print("\n...................Invalid Input...................")

            yes_no = input("\nDo you wish to continue: y/n  : ").lower()
            if yes_no == "n":
                print("\nSee You Later!")
                x("clear")
                break
            else:
                print("\nLet's GO!")
                input()
                print("\nNext Round")
                x("clear")

        player_data[player_name] = {
            "Total Game": total_wins + total_loses + total_draw,
            "Total Win": total_wins,
            "Total Loses": total_loses,
            "Total Draw": total_draw
        }

        continue

    elif option == "2":
        print("\nThe Highest scores of Player......\n")
        player_list = [player_name, player_profile]
        player_profile = [total_wins, total_loses, total_draw]
        for player_name in player_list:
            player_list.append(player_list)
            count = total_wins + total_loses + total_draw
            break

    elif option == "3":
        print("\nHere you go....The Scoreboard: ")
        print("\n{:<15}{:<15}{:<15}{:<15}".format("Player", "Total Games", "Total Wins", "Total Loses"))
        print("-" * 60)
        for player_name, player_profile in player_data.items():
            total_games = player_profile["Total Game"]
            total_wins = player_profile["Total Win"]
            total_loses = player_profile["Total Loses"]
            print("{:<15}{:<15}{:<15}{:<15}".format(player_name, total_games, total_wins, total_loses))

    elif option == "4":
        instruction_text = '''
        Rock, Paper, Scissors is an easy, fast game that everyone probably already knows.
        But if you are new to this, down below you can find basic instructions on how to play it. 

        In rock-paper-scissors, two players will each randomly choose one of three signs: rock, paper, scissors.
        Here are the rules that determine which sign beats another:

        - Rock wins over scissors (because rock smashes scissors)
        - Scissors wins over paper (because scissors cut paper)
        - Paper wins over rock (because paper covers rock)

        If both players show the same sign, it's a tie.

        Good luck and enjoy your game!
        '''

        # Iterate over each character in the instruction text and print it gradually
        for char in instruction_text:
            print(char, end='', flush=True)  # Print the character without a new line
            time.sleep(0.01)  # Delay for 0.01 seconds


    else:
        print("Exiting.......")
        break
