def search_algorithm(sorted_data, user_input):
    player_pairs = []
    already_checked = []

    for h_in in sorted_data:
        substract = user_input - h_in

        if sorted_data.get(substract) and h_in not in already_checked:
            for player_1 in sorted_data[h_in]:
                for player_2 in sorted_data[substract]:
                    if player_1 != player_2:
                        player_pairs.append((player_1, player_2))
                        if h_in == substract:
                            sorted_data[substract].remove(player_2)

            already_checked.append(substract)

    return player_pairs

def data_sorting(data):
    sorted_data = {}

    for player in data:
        player_h_in = int(player["h_in"])
        if player_h_in not in sorted_data:
            sorted_data[player_h_in] = []

        sorted_data[player_h_in].append(player)

    return sorted_data
