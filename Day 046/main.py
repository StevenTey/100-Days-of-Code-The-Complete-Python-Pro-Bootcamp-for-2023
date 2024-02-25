import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import pprint as pp
import json

while True:
    date = input("Which Year do you want to travel to? Please enter a date in YYYY-MM-DD format: ")
    if len(date) != 10 or date[4] != "-" or date[7] != "-":
        print("Invalid date format. Please try again.")
    else:
        break

url = f"https://www.billboard.com/charts/hot-100/{date}"
# url = f"https://www.billboard.com/charts/hot-100/2023-08-11"

response = requests.get(url)  
billboard_html = response.text    
    
def scrape_data(billboard_html):
    soup = BeautifulSoup(billboard_html, 'html.parser')
    songs = soup.find_all("h3", id = "title-of-a-story", class_ = "a-no-trucate")
    songs_list = []
    for song in songs:
        songs_list.append(song.text.strip())
    return songs_list

songs_list = scrape_data(billboard_html)

YOUR_APP_CLIENT_ID = "26880cabb2fc425e9cf65f0b195d1cff"
YOUR_APP_CLIENT_SECRET = "8e73349e9e2f41a996ffcbd423647e56"
YOUR_APP_REDIRECT_URI = "http://example.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=YOUR_APP_CLIENT_ID,
                                               client_secret=YOUR_APP_CLIENT_SECRET,
                                               redirect_uri=YOUR_APP_REDIRECT_URI,
                                               scope="playlist-modify-private"))


# search song and retrive uri from spotify
def search_song(song, year=date[0:4]):
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        return uri
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        return None

# create a playlist if no exist
def create_playlist():
    user_id = sp.current_user()["id"]
    playlist_name = f"{date} Billboard 100"
    playlists = sp.user_playlists(user_id)
    # for playlist in playlists["items"]:
    #     if playlist["name"] == playlist_name:
    #         print(f"{playlist_name} already exists.")
    #         return playlist["id"]
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
    print(f"{playlist_name} created.")
    return playlist["id"]

def add_song_to_playlist():
    playlist_id = create_playlist()
    uris = [search_song(song) for song in songs_list]
    uris = [uri for uri in uris if uri is not None]  # remove None values
    sp.playlist_add_items(playlist_id, uris)
    print(f"{len(uris)} songs added to the playlist.")

add_song_to_playlist()