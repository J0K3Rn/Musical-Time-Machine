# Musical-Time-Machine
 
Gets the top 100 songs of a particular date and creates a Spotify playlist

Features:
- Uses Beautiful Soup to web-scrape Billboard and get the top 100 songs of a particular date
- Uses Spotify API (spotipy) to create a playlist
- User input validation

How to run:
- Download repository
- Open downloaded repository with a command line interface
- Create an account on [Spotify](https://www.spotify.com/)
- Go to the [Developer Dashboard](https://developer.spotify.com/dashboard), create an app set `Redirect URIs` to 
`http://localhost:3000/callback/`
- Get your `Client ID`, and `Client secret` from your newly created Spotify App
- Update `main.py` with your `Client ID`, and `Client secret` hashes
- run `pip install bs4`
- run `pip install spotipy`
- run `python main.py`
- Program will start and ask you for a date to get. Songs not found will be outputted by the program

Program Running Example:

![alt text](https://github.com/J0K3Rn/Musical-Time-Machine/blob/main/screenshots/program.png?raw=true) 

Billboard Top 100:

![alt text](https://github.com/J0K3Rn/Musical-Time-Machine/blob/main/screenshots/top_100.png?raw=true) 

Generated Spotify Playlist:

![alt text](https://github.com/J0K3Rn/Musical-Time-Machine/blob/main/screenshots/spotify_playlist.png?raw=true) 

