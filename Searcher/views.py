import requests

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .methods import search_algorithm, data_sorting


API_URL = "https://mach-eight.uc.r.appspot.com/"

@csrf_exempt
def index(request):

    if request.method == "GET":
        return render(request, "Searcher/index.html")

    if request.method == "POST":
        user_input = int(request.POST["user_input"])

        try:
            json_data = requests.get(API_URL)
            players_data = json_data.json()["values"]

        except:
            return render(request, "Searcher/index.html", {"error": "Fetch from API failed"})

        # Sort the data in a dict by height
        sorted_data = data_sorting(players_data)

        # Run the algorithm to find the pairs
        player_pairs = search_algorithm(sorted_data, user_input)

        return render(request, "Searcher/index.html", {"result": player_pairs if player_pairs else 0})
