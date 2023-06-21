from os import system as x
import random

player_name = ""
player_age = ""
player_data = {}

while True:
    print('''
    [0] - Final Exit
    [1] - Play
    [2] - High Scorer Player
    [3] - Scoreboard/Dashboard
    ''')

    option = input("Select an option: ")

    if option == "1":
        total_wins = 0
        total_loses = 0
        total_draw = 0

        print("\nYuhuuu!!! Your game begins now......:")
        player_name = input("\nEnter Your Name: ")
        player_age = input("\nEnter Your Age: ")

        input()
        x("clear")
        print('''
        Let's begin.......
        Enter your choice from Rock, Paper, Scissors
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
                print("\nYipppiee..... You WON!!!!")
                total_wins += 1
            elif (
                (computer_choice1 == "Rock" and player_choice == "Scissors")
                or (computer_choice1 == "Scissors" and player_choice == "Paper")
                or (computer_choice1 == "Paper" and player_choice == "Rock")
            ):
                print("\nSORRY!!!! You Lose.... Play again to Win")
                total_loses += 1
            elif computer_choice1 == player_choice:
                print("\nIt's a draw..... Play again to Win!!!!")
                total_draw += 1
            else:
                print("\nError........................Warning...................")

            yes_no = input("\nDo you wish to continue: y/n  : ").lower()
            if yes_no == "n":
                print("\nOh!!! No Problem you play later......")
                x("clear")
                break
            else:
                print("\nGlad you are continuing.......")
                input()
                print("\nNext game...... ")
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
        print("\n{: <15}{: <15}{: <15}{: <15}".format("Player", "Total Games", "Total Wins", "Total Loses"))
        print("-" * 60)
        for player_name, player_profile in player_data.items():
            total_games = player_profile["Total Game"]
            total_wins = player_profile["Total Win"]
            total_loses = player_profile["Total Loses"]
            print("{: <15}{: <15}{: <15}{: <15}".format(player_name, total_games, total_wins, total_loses))

    else:
        print("Exiting.......")
        break
