elif option == "2":     # shows the highest scores of the play by taking the option "2" 
        print("\nTodays highest score is......\n")
        
        player_profile = {  # dictionary created for getting the highest scores throgh total wins.
                        "Player Name":player_name,
                        "Total Win":total_wins,        
                        }
        player_data.update({player_name:player_profile})    # updating the dictionary with player's name and it's profile

        most_wins = 0
        top_players = []

        for player_name, player_profile in player_data.items():    # for loop for getting the player name and its profile details stored in player data dictonary
            total_wins = player_profile.get("Total Win")    # getting the value from player_profile dictionary for Total wins.
            if total_wins > most_wins:      # comparing total_wins with most_wins
                most_wins = total_wins      # most_wins will be the highest total wins
                top_players = [player_name]   # top_players will be the player_name[s] who scored max total wins. Before adding [] each letter was considered player_name in Ver2 code
            elif total_wins == most_wins:   # comparing if max total wins are tied with multiple players
                top_players.append(player_name) # appending tied players with most wins to top_players list

        for player in top_players:
            print(f"{player} showed some incredible skill with amazing {most_wins} wins today!\n") #For looping top_players list and displaying highest scoring player(s)
        print("Press any key to continue")
        input()