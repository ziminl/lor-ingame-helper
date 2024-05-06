import requests
import time

def get_current_game_state(player_puuid):
    url = f"https://asia.api.riotgames.com/lor/active/v1/active-games/by-puuid/{player_puuid}"
    api_key = "YOUR_RIOT_API_KEY"
    headers = {"X-Riot-Token": api_key}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        game_state = response.json()
        return game_state
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

def print_opponent_name_if_game_starts(player_puuid):
    while True:
        game_state = get_current_game_state(player_puuid)
        if game_state:
            if "GameState" in game_state:
                if game_state["GameState"] == "InProgress":
                    for participant in game_state["Players"]:
                        if participant["PUUID"] != player_puuid:
                            print("Opponent's name:", participant["Name"])
                            return
            else:
                print("No active game found.")
                return
        time.sleep(5)

if __name__ == "__main__":
    player_puuid = "YOUR_PLAYER_PUUID"
    print_opponent_name_if_game_starts(player_puuid)
