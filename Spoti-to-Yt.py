from time import sleep
import time
import spotipy
import json
from pathlib import Path
from dataclasses import dataclass

from pytube import Search
from pytube.contrib.search import logger

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# https://dev.to/yogeshwaran01/from-spotify-to-youtube-how-i-built-a-python-script-to-convert-playlists-2h89 do dokonczenia info

logger.disabled = True

client_id, redirect_uri, api_key, credentials = None, None, None, None

class YoutubeClient:
    def __init__(self) -> None:
        flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])

        creds = flow.run_local_server()

        self.youtube = build('youtube', 'v3', credentials=creds)

    def create_playlist(self, title, description):
        playlist = self.youtube.playlists().insert(
            part='snippet',
            body=dict(
                snippet=dict(
                    title=title,
                    description=description
                )
            )
        ).execute()

        return playlist
    
    def add_song_playlist(self, playlist_id: str, video_id: str):
        request = (
                self.youtube.playlistItems()
                .insert(
                    part="snippet",
                    body={
                        "snippet": {
                            "playlistId": playlist_id,
                            "resourceId": {"kind": "youtube#video", "videoId": video_id},
                        }
                    },
                )
            )
        playlist_item = request.execute()
        return playlist_item

    def search_video(self, query: str):
        return Search(query).results[0].video_id


def load_config():
    global client_id
    global client_secret
    global redirect_uri

    if Path('config.json').exists():
        with open('config.json', 'r') as file:
            config = json.load(file)
            client_id = config['client_id']
            client_secret = config['client_secret']
            redirect_uri = config['redirect_uri']
    else:
        print('Config file not found')
        client_id = input('Enter client_id: ')
        client_secret = input('Enter client_secret: ')
        redirect_uri = input('Enter redirect_uri: ')

        with open('config.json', 'w') as file:
            config = {
                'client_id': client_id,
                'client_secret': client_secret,
                'redirect_uri': redirect_uri,
            }
            json.dump(config, file)


def listener():
    today_date = time.strftime("%d/%m/%Y")
    youtube_playlist_id = youtube.create_playlist(f'Spotify to Youtube {today_date}', 'Playlist created by Spoti-to-Yt.py')['id']
    while True:
        wait_for_active_device()
        track_name, artist = current_song()
        query = f'{track_name} {artist} lyrics'
        video_id = youtube.search_video(query)
        if video_id not in yt_playlist:
            youtube.add_song_playlist(youtube_playlist_id, video_id)
            yt_playlist.append(video_id)
            print(f'Added {track_name} by {artist} to playlist')
        else:
            print('Song already in playlist')
        take_break(track_name, artist)

def wait():
    global wait_time
    wait_time += 1
    sleep(wait_time)
    pass


def wait_for_active_device():
    global wait_time
    if sp.devices()['devices'][0]['is_active']:
        wait_time = 0
        
    else:
        wait()
        wait_for_active_device()


def current_song():
    current_track = sp.current_user_playing_track()
    if current_track is not None:
        track_name = current_track['item']['name']
        artist_name = current_track['item']['artists'][0]['name']
        return track_name, artist_name
    else:
        print("No song is currently playing.")


def take_break(track_name, artist):
    param = track_name, artist
    while param == current_song():
        sleep(5)


@dataclass
class Playlist:
    name: str
    description: str
    tracks: list


yt_playlist = []
wait_time = 0
break_time = 15


load_config()

youtube = YoutubeClient()

scope = 'playlist-read-private user-modify-playback-state playlist-modify-public playlist-modify-private user-top-read user-read-playback-state'
sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

listener()
