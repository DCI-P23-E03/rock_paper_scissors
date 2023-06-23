from os import system as x
import random
import time

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

# assigning the black value to the variables 
player_name = ""
player_age = ""
total_wins = 0
total_loses = 0
total_draw = 0
player_profile = ""
player_score = ""
choice1 = ""
total_games = 0
player_data ={}


# the program will goes on on till the wanted to exit.
while True:
    print('''
    [0] - Exit
    [1] - Play
    [2] - Leader
    [3] - Scorboard
    [4] - How to play
    ''')


    option = input("Select an option: ")
    
    if option == "1": # Begining the play by taking the option "1"
        total_wins = 0  # value "0" so that with every new player, variables are initialized or set as default.
        total_loses = 0
        total_draw = 0
            
        print("\nGame begins now......:")
        player_name = input("\nEnter Your Name: ") 
        #while (player_name.isalpha() != True):  
        #    print("Please enter the name using valid string..")
            
        
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
                print("\nYou WON!!!!Yipppiee..... ")
                total_wins +=1
            elif ((computer_choice1 == "Rock" and player_choice == "Scissors") or (computer_choice1 == "Scissors" and player_choice == "Paper") or (computer_choice1== "Paper" and player_choice == "Rock")):
                print("\nYou Lose....SORRY!!!! Play again to Win")
                total_loses +=1
            elif (computer_choice1 == player_choice):
                print("\nIt's a draw..... Play again to Win!!!!")
                total_draw +=1
            else:    
                print("\n......................Invalid Input.......................")        


            # to check from user if he/she want to continue the game.
            yes_no = input("\nDo you wish to continue: y/n  : ").lower()
            if yes_no == "n":
                print("\nSee You another Time!......")
                x("clear")
                break
            
            else:
                print("\nGlad you are continuing.......")
                input()
                print("\nGame On!...... ")
                x("clear")
        
        continue
        
        
    elif option == "2": # shows the highest scores of the play by taking the option "2" 
        print("\nPresenting the Leaderboard......")

        player_profile = {  # dictionary created for getting the highest scores throgh total wins.
                        "Player Name":player_name,
                        "Total Win":total_wins if total_wins is not None else 0,      
                        }
                        
        player_data.update({player_name:player_profile})    # updating the dictionary with player's name and it's profile
        
        most_wins = 0
        top_players = []

        for player_name1, player_profile1 in player_data.items():    # for loop for getting the player name and its profile details stored in player data dictonary
            total_wins = player_profile.get("Total Win",0)    # getting the value from player_profile dictionary for Total wins.
            #print("total wins: ",total_wins)            
            if total_wins > most_wins:      # comparing total_wins with most_wins
                most_wins = total_wins      # most_wins will be the highest total wins
                top_players = [player_name1]   # top_players will be the player_name[s] who scored max total wins. Before adding [] each letter was considered player_name in this code

            elif total_wins == most_wins:   # comparing if total_wins are tied with most_wins meaning a tie between multiple players
                #print("Total wins if equals to most wins =", total_wins)
                top_players.append(player_name1) # appending players tied with most_wins to top_players list

        if len(top_players) == 1 and most_wins !=0:   # check if the length of top_player list is "1". 
            #print("Length of the top player if equals to one =",len(top_players) )
            top_player = top_players[0] # add the name of the player
            print(f"\n\033[92m{top_player} \033[0m showed some incredible skill with {most_wins} wins today!..")

        elif most_wins == 0:   # check if the length of the top_player list is blank / zero or most_wins =0
            print(f"\n\033[92m{player_name1}\033[0m has not won any games yet...") 
       
        elif len(top_players) > 1:
            #if any(element in player_data[player_name1].get("Total wins") == most_wins):
                print(f"\nWe have mutiple winners with {most_wins} wins :")
                for player in top_players:
                    print('\033[92m'+player+'\033[0m')

        
        print("\nPress any key to continue")
        input()

        
    elif option == "3": # shows the scoreboard of the play by taking the option "3"
        print("\n...................... The Scoreboard of the Game: ...................... \n")
        print("\n{:<15}{:<15}{:<15}{:<15}{:<15}".format("Player", "Total Games", "Total Wins", "Total Loses", "Total Draws")) # formatting and presentation of Scoreboard
        print("-" * 73) # formatting and presentation of Scoreboard
      
        total_games =total_wins+total_loses+total_draw

        player_data[player_name] = { # dictionary created with player name and its profile
            "Total Games": total_games, # total games played is summation of total wins, total loses, total draws.
            "Total Wins": total_wins,
            "Total Loses": total_loses,
            "Total Draws": total_draw
        }
        for player_name, player_profile in player_data.items(): #loop for getting the values player_data for each player
        
            total_games = player_profile.get("Total Games",0) # Get the value for "Total Games" with a default of 0 if not found
            total_wins = player_profile.get("Total Wins",0)
            total_loses = player_profile.get("Total Loses",0)
            total_draw = player_profile.get("Total Draws",0)
            print("{:<15}{:<15}{:<15}{:<15}{:<15}".format(player_name, total_games, total_wins, total_loses,total_draw)) # formatting and presentation of Scoreboard along with values

        
    elif option == "4":
        instructions = '''\nRock, Paper, Scissors is an easy, fast game that everyone probably already knows.
But if you are new into this, down below you can find basic instructions on how to play it. 

In rock-paper-scissors, two players will each randomly choose one of three  signs: rock, paper, scissors
Here are the rules that determine which sign beats another:

-Rock wins over scissors (because rock smashes scissors)
-Scissors wins over paper (because scissors cut paper)
-Paper wins over rock (because paper covers rock)

If both players show the same sign, it’s a tie/draw.

Good luck and enjoy your game !

'''
        # Display text gradually time.sleep
        for char in instructions:
            print(char, end="", flush=True)
            time.sleep(0.01)


    elif option == "0":
        print("Exiting......")
        break
    else: # if wish to completly close/exit the game.
        print("Exiting.......")    
        break
    