from youtube_client import YoutubeClient
from spotify_client import SpotifyClient

if __name__ == '__main__':
    # # Create a Youtube API client to download list of liked videos
    # yt_client = YoutubeClient()
    # yt_client.get_liked_videos()
    # yt_client.print_liked_videos()

    # Create a Spotify account handle to create a new playlist
    # containing the songs in the liked YouTube videos list
    spotify_client = SpotifyClient()
    spotify_client.create_playlist()
