import random

flag1 = True
while flag1 == True:
    print("----------------------------------------------------------")
    print("-----Welcome to the game of Rock, Paper and Scissors!-----")
    print("----------------------------------------------------------")
    print("----------------Choose 1 to start new game----------------")
    print("-------------Choose 2 to view high score lists------------")
    print("--------------------Choose 3 to exit----------------------")
    print("----------------------------------------------------------")
    menu = input("Your choice? ")

    if menu == "1":
        print("Game starts")

        while True:
            choices = ["rock", "paper", "scissors"]
            player_choice = input("Choose your move (rock, paper, scissors): ").lower()
            computer_choice = random.choice(choices)

            print("Player chooses:", player_choice)
            print("Computer chooses:", computer_choice)

            if player_choice == computer_choice:
                print("It's a tie!")
            elif (
                (player_choice == "rock" and computer_choice == "scissors")
                or (player_choice == "paper" and computer_choice == "rock")
                or (player_choice == "scissors" and computer_choice == "paper")
            ):
                print("Player wins!")
            else:
                print("Computer wins!")

            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                break

        continue

    elif menu == "2":
        flag2 = True
        while flag2 == True:
            print("----------------------------------------------------------")
            print("-----------------Choose 1 for winners list----------------")
            print("------------------Choose 2 for games list-----------------")
            print("------------------Choose 3 for draws list-----------------")
            print("------------------Choose 4 for losers list----------------")
            print("-------------------Choose 5 for main menu-----------------")
            print("----------------------------------------------------------")
            highscore = input("Your choice? ")

            if highscore == "1":
                print("List of players sorted with most wins")
                list1 = input(
                    "Return to main menu with (m) or return to high score lists by pressing any key >>>"
                )
                if list1 == "m":
                    flag2 = False

            elif highscore == "2":
                print("List of players sorted with most games")
                list2 = input(
                    "Return to main menu with (m) or return to high score lists by pressing any key"
                )
                if list2 == "m":
                    flag2 = False

            elif highscore == "3":
                print("List of players sorted with most draws")
                list3 = input(
                    "Return to main menu with (m) or return to high score lists by pressing any key"
                )
                if list3 == "m":
                    flag2 = False

            elif highscore == "4":
                print("List of players sorted with most loses")
                list4 = input(
                    "Return to main menu with (m) or return to high score lists by pressing any key"
                )
                if list4 == "m":
                    flag2 = False

            else:
                flag2 = False

    elif menu == "3":
        print("Thanks for playing, see you later!")
        flag1 = False

    else:
        print("Wrong input please try again")
        flag1 = True
