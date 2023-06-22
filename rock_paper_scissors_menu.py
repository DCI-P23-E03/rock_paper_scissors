from os import system as x
import random

# assigning the black value to the variables 
player_name = ""
player_age = ""
total_wins = 0
total_loses = 0
total_draw = 0
player_profile = ""
player_score = ""
choice1 = ""
count = 0
player_data ={}


# the program will goes on on till the wanted to exit.
while True:
    print('''
    [0] - Final Exit
    [1] - Play
    [2] - High Scorer Player
    [3] - Scoreboard/Dashboard
    [4] - Instructions how to play
    ''')


    option = input("Select an option: ")
    
    if option == "1": # Begining the play by taking the option "1"
        total_wins = 0  # value "0" so that with every new player, variables are initialized or set as default.
        total_loses = 0
        total_draw = 0
            
        print("\nYuhuuu!!! Your game begins now......:")
        player_name = input("\nEnter Your Name: ") 
        #while (player_name.isalpha() != True):  
        #    print("Please enter the name using valid string..")
            
        player_age = input("\nEnter Your Age: ")
        #while (player_age.isnumeric() != True):
        #    print("Please enter your age using valid numbers..")
        
        input()
        x("clear")
        print('''
        Let's begin.......
        Enter your choice from Rock , Paper , Scissors
        
        ''')

        while True:
            choice1 = [
                "Rock",
                "Paper",
                "Scissors",
            ] # option for random choice.
            computer_choice1 = random.choice(choice1) # random module choice method is called so that every time computer shows a random option.
            player_choice =  input("Enter your choice: ").capitalize()
            print("Computer Choice: ",computer_choice1)
            
            # comparing the player_choice and computer_choice so as show the win, lose, draw.
            if ((player_choice == "Rock" and computer_choice1 == "Scissors") or (player_choice == "Scissors" and computer_choice1 =="Paper") or (player_choice == "Paper" and computer_choice1 =="Rock")):
                print("\nYipppiee..... You WON!!!!")
                total_wins +=1
            elif ((computer_choice1 == "Rock" and player_choice == "Scissors") or (computer_choice1 == "Scissors" and player_choice == "Paper") or (computer_choice1== "Paper" and player_choice == "Rock")):
                print("\nSORRY!!!! You Lose.... Play again to Win")
                total_loses +=1
            elif (computer_choice1 == player_choice):
                print("\nIt's a draw..... Play again to Win!!!!")
                total_draw +=1
            else:    
                print("\nError........................Warning...................")        


            # to check from user if he/she want to continue the game.
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
        
        continue
        
        
    elif option == "2": # shows the highest scores of the play by taking the option "2" 
        print("\nTodays highest scoring player is......\n")
        
        player_profile = {  # dictionary created for getting the highest scores through total wins.
                        "Player Name":player_name,
                        "Total Games":total_wins+total_loses+total_draw,
                        "Total Win":total_wins,        
                        }
        player_data.update({player_name:player_profile}) # updating the dictionary with player's name and it's profile

        most_wins = 0
        top_player = ""

        for player_name1, player_profile1 in player_data.items(): # for loop for getting the player name and its profile details stored in player data dictonary
            total_wins = player_profile.get("Total Win") # getting the value from player_profile dictionary for Total wins.
            print(total_wins)
            if total_wins > most_wins:   # comparing total_wins with most_wins
                most_wins = total_wins   # most_wins will be the highest total wins
                top_player = player_name1 # top_player will the player_name who scored max total wins

            print(f"{top_player} with amazing {most_wins} wins today!\n")
            print("Press any key to continue")
            input()
        
    elif option == "3": # shows the scoreboard of the play by taking the option "3"
        print("\nHere you goes....The Scoreboard of the Game:.........: \n")
        print("\n{:<15}{:<15}{:<15}{:<15}{:<15}".format("Player", "Total Games", "Total Wins", "Total Loses", "Total Draws")) # formatting and presentation of Scoreboard
        print("-" * 73) # formatting and presentation of Scoreboard
      
        player_data[player_name] = { # dictionary created with player name and its profile
            "Total Games": total_wins + total_loses + total_draw, # total games played is summation of total wins, total loses, total draws.
            "Total Wins": total_wins,
            "Total Loses": total_loses,
            "Total Draws": total_draw
        }
        for player_name, player_profile in player_data.items(): #loop for getting the values player_data for each player
            total_games = player_profile["Total Games"]
            total_wins = player_profile["Total Wins"]
            total_loses = player_profile["Total Loses"]
            total_draw = player_profile["Total Draws"]
            print("{:<15}{:<15}{:<15}{:<15}{:<15}".format(player_name, total_games, total_wins, total_loses,total_draw)) # formatting and presentation of Scoreboard along with values

        '''player_profile = { # sub dictionary of profile_data dictionary
                        "Total Games":count,
                        "Total Wins":total_wins,
                        "Total Loses":total_loses,
                        "Total Draws":total_draw
                        }
        
        
        player_data.update({player_name:player_profile}) # updating the values in nested dictionary.
        #print("\nPlayer details on Scoreboard:   \n", player_data)
        
        #loop for each element of player_profile in player_data to be presented.
        for playerprofile, value in player_data.items(): 
                print(f"{playerprofile} : Total Games: {value['Total Games']}")
                print(f"Total Wins: {value['Total Wins']}")
                print(f"Total Loses: {value['Total Loses']}")
                print(f"Total Draws: {value['Total Draws']}")'''
        
    elif option == "4":
        print(""" 
        Rock, Paper, Scissors is an easy, fast game that everyone probably already knows.
        But if you are new into this, down below you can find basic instructions on how to play it. 

        In rock-paper-scissors, two players will each randomly choose one of three  signs: rock, paper, scissors
        Here are the rules that determine which sign beats another:

        -Rock wins over scissors (because rock smashes scissors)
        -Scissors wins over paper (because scissors cut paper)
        -Paper wins over rock (because paper covers rock)

        If both players show the same sign, it’s a tie.

        Good luck and enjoy your game game!

        """)

    elif option == "0":
        print("Exiting......")
        break
    else: # if wish to completly close/exit the game.
        print("Exiting.......")    
        break