
import json
import urllib.request

with urllib.request.urlopen("https://ddragon.leagueoflegends.com/realms/na.json") as url:
    version = json.loads(url.read().decode())["n"]["champion"]


def get_champ(champion_id, version):
    with urllib.request.urlopen("http://ddragon.leagueoflegends.com/cdn/" + version + "/data/en_US/champion.json") as url:
        champs = json.loads(url.read().decode())["data"]

        for champ in champs.values():
            if champ["key"] == str(champion_id):
                return champ["id"]

"""
def get_tips_against(champion):
    with urllib.request.urlopen(
            "http://ddragon.leagueoflegends.com/cdn/" + version + "/data/en_US/champion/" + champion + ".json") as url:
        data = json.loads(url.read().decode())

        print("Tips when playing against " + champion)
        for count, tips in enumerate(data["data"][champion]["enemytips"]):
            print(str(count + 1) + ". " + tips)
"""

api_key = "RGAPI-2781b50d-7a9a-4350-a38e-3bf19f6b61e1"

summoner = input("Your summoner name: ")

with urllib.request.urlopen(
        "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner + "?api_key=" + api_key) as url:
    userID = json.loads(url.read().decode())["id"]

with urllib.request.urlopen(
        "https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + userID + "?api_key=" + api_key) as url:
    for count, player in enumerate(json.loads(url.read().decode())["participants"]):
        if count == 0:
            print("\nTeam 1:")
        elif count == 5:
            print("\nTeam 2:")
        print(player["summonerName"] + " (" + get_champ(player["championId"], version) + ")" + " Lvl:" )
       ## get_tips_against(get_champ(player["championId"], version))
