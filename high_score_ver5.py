elif option == "2": # shows the highest scores of the play by taking the option "2" 
        print("\nPresenting the Leaderboard......")

        player_profile = {  # dictionary created for getting the highest scores throgh total wins.
                        "Player Name":player_name,
                        "Total Win":total_wins if total_wins is not None else 0,      
                        }
                        
        player_data.update({player_name:player_profile})    # updating the dictionary with player's name and it's profile
        
        

        for player_name, player_profile in player_data.items():    # for loop for getting the player name and its profile details stored in player data dictonary
            total_wins = player_profile.get("Total Win",0)    # getting the value from player_profile dictionary for Total wins.
            
            if total_wins >= most_wins:      # comparing total_wins with most_wins
                most_wins = total_wins      # most_wins will be the highest total wins
                top_players.append(player_name)  # top_players will be the player_name[s] who scored max total wins. Before adding [] each letter was considered player_name in this code

            elif total_wins == most_wins:   # comparing if total_wins are tied with most_wins meaning a tie between multiple players
                top_players.append(player_name) # appending players tied with most_wins to top_players list

        if len(top_players) > 1 :  # Checking if top_players list is longer than one player
            print(f"\nWe have mutiple winners/Ties with {most_wins} wins :")
            for player in top_players:
               print('\033[92m'+player+'\033[0m')
        
        elif most_wins == 0:   # check if the length of the top_player list is blank / zero or most_wins =0
            for player in top_players:  
                print(f"\n\033[92m{player}\033[0m has not won any games yet...") 
       
        else:       # If top_players list length is 1, message for one sole winner is displayed
            for player in top_players:  
                print(f"\033[92m{player} \033[0m showed some incredible skill with amazing {most_wins} wins today!") #For looping top_players list and displaying highest scoring player(s)            
    
        
        print("\nPress any key to continue")
        input()