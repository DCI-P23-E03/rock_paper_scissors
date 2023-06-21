from os import system as x
import random

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

while True:
    print('''
    [0] - Final Exit
    [1] - Play
    [2] - High Scorer Player
    [3] - Scorboard/Dashboard
    ''')


    option = input("Select an option: ")

    if option == "1":
        total_wins = 0
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
            ]
            computer_choice1 = random.choice(choice1)
            player_choice =  input("Enter your choice: ").capitalize()
            print("Computer Choice: ",computer_choice1)
            
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
        
        
    elif option == "2":
        print("\nTodays highest score is......\n")
        
        player_profile = {
                        "Player Name":player_name,
                        "Total Win":total_wins,        
                        }
        player_data.update({player_name:player_profile})

        most_wins = 0
        top_players = []

        for player_name, player_profile in player_data.items():
            total_wins = player_profile.get("Total Win")
            if total_wins > most_wins:
                most_wins = total_wins
                top_players = player_name
            elif total_wins == most_wins:
                top_players.append(player_name)

        print(f"Incredible skills from {top_players} with amazing {most_wins} wins today!\n")
        print("Press any key to continue")
        input()

    elif option == "3":
        print("\nHere you goes....The Scoreboard of the same:.........: ")

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
        player_profile = {
                        "Total Game":count,
                        "Total Win":total_wins,
                        "Total Loses":total_loses,
                        "Total Draw":total_draw
                        }
        
        #player_name = {"Player Name":player_name}
        player_data.update({player_name:player_profile})
        #print("\nPlayer details on Scoreboard:   \n", player_data)

        for playername, playerprofile in player_data.items():
            #print("\nPlayer Name : ", playername)
            for playerprofile, value in player_data.items(): 
                print(f"{playerprofile} : {value}")
            
                


      
      
        
        

    else:
        print("Exiting.......")    
        break
    