from youtube_client import YoutubeClient
from spotify_client import SpotifyClient

if __name__ == '__main__':
    # # Create a Youtube API client to download list of liked videos
    # yt_client = YoutubeClient()
    # liked_videos_lst = yt_client.get_liked_videos()

    # Test values for SpotifyClient class 
    artists = ['JPEGMAFIA', 'Liturgy', 'JPEGMAFIA', 'Madvillain', 'KGHNDSF',]
    songs = ['SUPER TUESDAY!', 'HAJJ', 'BALD!', 'Figaro', 'ASDFASDF']
    liked_videos_lst = [artists, songs]

    # Create a Spotify account handle to create a new playlist
    # containing the songs in the liked YouTube videos list
    spotify_client = SpotifyClient()
    spotify_songs_lst = spotify_client.get_spotify_songs(liked_videos_lst)
    http_reponse = spotify_client.add_song_to_playlist(spotify_songs_lst)
