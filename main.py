from bs4 import BeautifulSoup
import requests
import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth


BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"

# Spotify Setup
CLIENT_ID = ""
CLIENT_SECRET = ""
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                                               redirect_uri="http://localhost:3000/callback/", client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET, show_dialog=True, cache_path="token.txt"))

user_id = sp.current_user()["id"]

prompt = "Which year do you want to travel to? Type the date in this format: YYYY-MM-DD\n"
date = input(prompt)

# User input validation for date format
try:
    datetime.datetime.strptime(date, "%Y-%m-%d")
except ValueError:
    print("Incorrect data format, should be YYYY-MM-DD")
    exit(1)

response = requests.get(f"{BILLBOARD_URL}{date}")
top_hits_webpage = response.text
soup = BeautifulSoup(top_hits_webpage, "html.parser")
songs = soup.find_all(name="h3", class_="a-no-trucate")

song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song.getText().strip()} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"Song: {song.getText().strip()} - doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
