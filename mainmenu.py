from os import system as x
import random

def computer_choice():
    choice1 = [
        "Rock",
        "Paper",
        "Scissors",
    ]
    computer_choice1 = random.choice(choice1)
    print(computer_choice1)

while True:
    print('''
    [0] - Final Exit
    [1] - Play
    [2] - High Scorer Player
    [3] - Scorboard/Dashboard
    ''')
    player_name = ""
    player_age = ""
    total_wins = 0
    total_loses = 0
    total_draw = 0
    player_profile = ""
    player_score = ""

    option = input("Select an option: ")

    if option == "1":
        print("Yuhuuu!!! Your game begins now......:")
        player_name = input("Enter Your Name: ")
        player_age = input("Enter Your Age: ")
        input()
        print('''
        Let's begin.......
        Enter your choice from Rock , Paper , Scissors
        
        ''')

        choice =  input("Enter your choice: \n").capitalize()
        choice1 = print("Computer Choice: ") 
        computer_choice()
        
        if (choice == "Rock" and choice1 == "Scissors") or (choice == "Scissors" and choice1 =="Paper") or (choice == "Paper" and choice1 =="Rock"):
            print("Yipppiee..... You WON!!!!")
            total_wins +=1
            yes_no = input("Do you wish to continue: y/n").lower()
            while yes_no == "y":
                print("Glad you are continuing.......")
                input()
                print("Next game...... ")
                choice =  input("Enter your choice: \n").capitalize()
                choice1 = print("Computer Choice: ") 
                computer_choice()   
            else:
                print("Oh!!! No Problem you play later......")
                break
        elif (choice1 == "Rock" and choice == "Scissors") or (choice1 == "Scissors" and choice == "Paper") or (choice1 == "Paper" and choice == "Rock"):
            print("SORRY!!!!.... Play again to Win")
            total_loses +=1
            yes_no = input("Do you wish to continue: y/n").lower()
            while yes_no == "y":
                print("Glad you are continuing.......")
                input()
                print("Next game...... ")
                choice =  input("Enter your choice: \n").capitalize()
                choice1 = print("Computer Choice: ") 
                computer_choice()       
        else:
            print("It's a draw..... Play again to Win!!!!")
            total_draw +=1
            yes_no = input("Do you wish to continue: y/n").lower()
            while yes_no == "y":
                print("Glad you are continuing.......")
                input()
                print("Next game...... ")
                choice =  input("Enter your choice: \n").capitalize()
                choice1 = print("Computer Choice: ") 
                computer_choice()       

    elif option == "2":
        print('''
        Player Name: XYZ
        Total Games played: 100
        Total Wins: 70
        Total Loses: 20
        Total Draw: 10
        ''')

    elif option == "3":
        print("Here you goes.............: ")
        player_profile = {
            "Name":player_name,
            "Total_Wins":total_wins,
            "Total_Loses":total_loses,
            "Total_Draw":total_draw   
        }
        print("Scoreboard......", player_profile)

    else:
        print("Exiting.......")    
        break
    