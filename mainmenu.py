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
    
while True:
    print('''
    [0] - Final Exit
    [1] - Play
    [2] - Scorboard/Dashboard
    [3] - High Scorer Player
    ''')


    option = input("Select an option: ")

    if option == "1":
        print("\nYuhuuu!!! Your game begins now......:")
        player_name = input("\nEnter Your Name: ")
        player_age = input("\nEnter Your Age: ")
        input()
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
                print("\nError........................Waring...................")        


            yes_no = input("\nDo you wish to continue: y/n  :").lower()
            if yes_no == "n":
                print("\nOh!!! No Problem you play later......")
                break
            
            else:
                print("\nGlad you are continuing.......")
                input()
                print("\nNext game...... ")
        
        continue
        
       
    elif option == "2":
        print("\nHere you goes....The Scoreboard of the same:.........: ")
        player_list = [player_name, player_profile]
        player_profile =[total_wins,total_loses,total_draw]
        for player_name in player_list:
            player_list.append(player_list)
            count = total_wins+total_loses+total_draw
            
            print(f"\nPlayer details on Scoreboard:   \n", 
            "\nPlayer_Name: ", player_name,
            "\nTotal Games played: ", count,
            "\nTotal Wins: ", total_wins,
            "\nTotal Loses: ", total_loses,
            "\nTotal Draw: ",total_draw
            )
            break


    elif option == "3":
        print("\nThe Highest scores of Player......\n")      
        player_name_profile = {"\nName":player_name, "\nPlayer_Profile":player_profile}

       
        player_profile = {
            #"Name":player_name,
            "\nTotal_Wins":total_wins,
            "\nTotal_Loses":total_loses,
            "\nTotal_Draw":total_draw  
        }
        player_name_profile.update({"\nName":player_name,"\nPlayer_Profile":player_profile})
        player_profile.update({
            #"Name":player_name,
            "\nTotal_Wins":total_wins,
            "\nTotal_Loses":total_loses,
            "\nTotal_Draw":total_draw})
        
        print("\nScoreboard of High Score Player......", player_name_profile)

    else:
        print("Exiting.......")    
        break
    