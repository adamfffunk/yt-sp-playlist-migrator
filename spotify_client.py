import json
import requests

from exceptions import ResponseException

class SpotifyClient:

    def  __init__(self):
        # Access Spotify API credentials in secret JSON file
        client_secrets_file = "./spotify_secret.json"
        with open( client_secrets_file ) as f:
            temp_client_data_dict = json.load(f)

        self.client_id = temp_client_data_dict["client_id"]
        # self.client_secret = temp_client_data_dict['client_secret']
        self.client_token = temp_client_data_dict["client_token"]

    # Creates a public Spotify playlist called "YouTube Liked Videos" and 
    # returns the playlist URI 
    def create_playlist(self):
        """Create A New Playlist"""
        request_body = json.dumps({
            "name": "Youtube Liked Videos",
            "description": "All Liked Youtube Videos",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            self.client_id)
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.client_token)
            }
        )

        # Returning playlist ID
        response_json = response.json()        
        return response_json["id"]

    # def get_spotify_uri(self, song_name, artist):
    #     """Search For the Song"""
    #     query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
    #         song_name,
    #         artist
    #     )
    #     response = requests.get(
    #         query,
    #         headers={
    #             "Content-Type": "application/json",
    #             "Authorization": "Bearer {}".format(self.client_token)
    #         }
    #     )
    #     response_json = response.json()
    #     songs = response_json["tracks"]["items"]

    #     # only use the first song
    #     uri = songs[0]["uri"]

    #     return uri

    # def add_song_to_playlist(self):
    #     """Add all liked songs into a new Spotify playlist"""
    #     # populate dictionary with our liked songs
    #     self.get_liked_videos()

    #     # collect all of uri
    #     uris = [info["spotify_uri"]
    #             for song, info in self.all_song_info.items()]

    #     # create a new playlist
    #     playlist_id = self.create_playlist()

    #     # add all songs into new playlist
    #     request_data = json.dumps(uris)

    #     query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
    #         playlist_id)

    #     response = requests.post(
    #         query,
    #         data=request_data,
    #         headers={
    #             "Content-Type": "application/json",
    #             "Authorization": "Bearer {}".format(self.client_token)
    #         }
    #     )

    #     # check for valid response status
    #     if response.status_code != 200:
    #         raise ResponseException(response.status_code)

    #     response_json = response.json()
    #     return response_json
