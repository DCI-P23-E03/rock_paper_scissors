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
    [3] - Scorboard/Dashboard
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
        print("\nThe Highest scores of Player......\n")
        
        player_list = [player_name, player_profile]
        player_profile =[total_wins,total_loses,total_draw]
        for player_name in player_list:
            player_list.append(player_list)
            count = total_wins+total_loses+total_draw

            '''print(f"\nPlayer details on Scoreboard:   \n", 
            "\nPlayer_Name: ", player_name,
            "\nTotal Games played: ", count,
            "\nTotal Wins: ", total_wins,
            "\nTotal Loses: ", total_loses,
            "\nTotal Draw: ",total_draw
            )'''
            #print("\nScoreboard of High Score Player......", )
            break


    elif option == "3": # shows the scoreboard of the play by taking the option "3"
        print("\nHere you goes....The Scoreboard of the Game:.........: \n")

        count = total_wins+total_loses+total_draw      
        '''player_name_profile = {"Name":player_name, "Player_Profile":player_profile}    
        player_profile = {
            "Total_Games_Played ": count,
            "nTotal_Wins":total_wins,
            "Total_Loses":total_loses,
            "Total_Draw":total_draw  
        }
        player_name_profile.update({"Name":player_name,"Player_Profile":player_profile})
        player_profile.update({
            "Total Games played ":count,
            "Total_Wins":total_wins,
            "Total_Loses":total_loses,
            "Total_Draw":total_draw})
        '''
        player_profile = { # sub dictionary of profile_data dictionary
                        "Total Games":count,
                        "Total Wins":total_wins,
                        "Total Loses":total_loses,
                        "Total Draws":total_draw
                        }
        
        #player_name = {"Player Name":player_name}
        player_data.update({player_name:player_profile}) # updating the values in nested dictionary.
        #print("\nPlayer details on Scoreboard:   \n", player_data)
        
        #for playername, playerprofile in player_data.items():
            #print("\nPlayer Name : ", playername)
        for playerprofile, value in player_data.items(): 
                print(f'''{playerprofile}
Total Games: {value['Total Games']}''')
                print(f"Total Wins: {value['Total Wins']}")
                print(f"Total Loses: {value['Total Loses']}")
                print(f"Total Draws: {value['Total Draws']}")
    
    else: # if wish to completly close/exit the game.
        print("Exiting.......")    
        break
    