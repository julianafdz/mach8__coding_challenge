import unittest

import requests

from .methods import search_algorithm, data_sorting


class TestMyLogarithm(unittest.TestCase):

    API_URL = "https://mach-eight.uc.r.appspot.com/"

    try:
        json_data = requests.get(API_URL)
        players_data = json_data.json()["values"]

    except:
        raise RuntimeError

    sorted_data = data_sorting(players_data)

    def test_search_algorithm(self):
        for test_input in range(300):
            player_pairs = search_algorithm(self.sorted_data, test_input)

            if player_pairs:
                # If pairs are finded check if the sum of both is correct and that there are not duplicates in the pair
                for player_pair in player_pairs:
                    self.assertEqual(int(player_pair[0]["h_in"]) + int(player_pair[1]["h_in"]), test_input)
                    self.assertNotEqual(player_pair[0], player_pair[1])

            else:
                # else if pairs are not finded check if there are endeed not sum of heights wich result is equal to test_input
                all_heights = self.sorted_data.keys()
                for height in all_heights:
                    heights = list(all_heights)
                    substract = test_input - height

                    if substract == height and len(self.sorted_data[height]) < 2:
                        heights.remove(height)

                    self.assertNotIn(substract, heights)


if __name__ == "__main__":
    unittest.main()