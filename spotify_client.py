import json
import requests

from exceptions import ResponseException

class SpotifyClient:

    def  __init__(self):
        # Access Spotify API credentials in secret JSON file
        client_secrets_file = "./spotify_secret.json"
        with open( client_secrets_file ) as f:
            client_auth_dict = json.load(f)

        self.oauth_token = client_auth_dict["oauth_token"]
        self.user_id = client_auth_dict["user_id"]

    # Creates a public Spotify playlist called "YouTube Liked Videos" and 
    # returns the playlist ID 
    def create_playlist(self):
        # TODO Do not create playlist if it already exists
        """Create A New Playlist"""
        request_body = json.dumps({
            "name": "Youtube Liked Videos",
            "description": "All Liked Youtube Videos",
            "public": "True"
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            self.user_id)
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.oauth_token)
            }
        )

        # TODO Handle 400, 401, 403 response codes
        # Returning playlist ID
        response_json = response.json()        
        return response_json["id"]

    # Sends list of song and artist names to Spotiy API, and returns the 
    # received list of song URIs
    def get_spotify_songs(self, songs_lst):
        """Convert artist and song list into list of Spotify songs URIs"""
        uri_lst = []

    # [ y[1] for y in temp_sum_period_lst ]

        # for x in songs_lst:
        songs_list_range = range( len(songs_lst[0]) )
        for x in songs_list_range:
            artist = songs_lst[0][x]
            song = songs_lst[1][x]
            uri = self.find_song_uri(song, artist)

            # Skip invalid URIs
            if uri == '':
                continue

            uri_lst.append(uri)
        
        return uri_lst

    # Requests a song URI from the Spotify API using the song and artist name.
    # Returns empty string if song and artist do not find any results
    def find_song_uri(self, song_name, artist):
        """Search For the Song"""
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.oauth_token)
            }
        )
        response_json = response.json()
        songs = response_json["tracks"]["items"]

        # TODO Handle IndexError exception case when songs[][] is empty or not
        # found
        # If no songs URIs were found for the artist and song, return empty string
        if len(songs) == 0:
            return ''

        # Only use the first song found in the search
        uri = songs[0]["uri"]
        return uri

    # Takes all Spotify song URIs in songs_lst and adds them to our
    # previously created playlist
    def add_song_to_playlist(self, songs_lst):
        """Add all liked songs into a new Spotify playlist"""
        # # collect all of uri
        # uris = [info["spotify_uri"]
        #         for song, info in self.all_song_info.items()]

        # Create a new playlist
        playlist_id = self.create_playlist()

        # Add all songs into new playlist
        request_data = json.dumps(songs_lst)

        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            playlist_id)

        response = requests.post(
            query,
            data=request_data,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.oauth_token)
            }
        )

        # TODO Create HTTP response handler 
        # check for valid response status
        if response.status_code != 200 | response.status_code != 201:
            raise ResponseException(response.status_code)

        response_json = response.json()
        return response_json
