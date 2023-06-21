    elif option == "2": # shows the highest scores of the play by taking the option "2" 
        print("\nTodays highest scoring player is......\n")
        
        player_profile = {  # dictionary created for getting the highest scores throgh total wins.
                        "Player Name":player_name,
                        "Total Win":total_wins,     
                        }
        player_data.update({player_name:player_profile}) # updating the dictionary with player's name and it's profile

        most_wins = 0
        top_player = ""

        for player_name1, player_profile1 in player_data.items(): # for loop for getting the player name and its profile details stored in player data dictonary
            total_wins = player_profile.get("Total Win") # getting the value from player_profile dictionary for Total wins.
            if total_wins >= most_wins:   # comparing total_wins with most_wins
                most_wins = total_wins   # most_wins will be the highest total wins
                top_player = player_name1 # top_player will the player_name who scored max total wins

        print(f"{top_player} with amazing {most_wins} wins today!\n")
        print("Press any key to continue")
        input()