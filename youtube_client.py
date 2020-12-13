import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import os
import requests
import youtube_dl

from exceptions import ResponseException

class YoutubeClient:

    def  __init__(self):
        self.get_client()

    # Log in to YouTube
    def get_client(self):
        """ Log Into Youtube, Copied from Youtube Data API """
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "client_secret.json"

        # Get credentials and create an API client
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()

        # from the Youtube DATA API
        self.api_client = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

    def get_liked_videos(self):
        """Grab Our Liked Videos & Create A Dictionary Of Important Song Information"""
        liked_videos_lst = [[],[]]
        
        request = self.api_client.videos().list(
            part="snippet,contentDetails,statistics",
            myRating="like"
        )
        response = request.execute()

        # collect each video and get important information
        for item in response["items"]:
            # video_title = item["snippet"]["title"]
            youtube_url = "https://www.youtube.com/watch?v={}".format(
                item["id"])

            # use youtube_dl to collect the song name & artist name
            video = youtube_dl.YoutubeDL({}).extract_info(
                youtube_url, download=False)
            liked_videos_lst[0].append(video["artist"])
            liked_videos_lst[1].append(video["track"])

        return liked_videos_lst
