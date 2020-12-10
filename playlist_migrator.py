from youtube_client import YoutubeClient

if __name__ == '__main__':
    yt_client = YoutubeClient()
    yt_client.get_liked_videos()
    yt_client.print_liked_videos()
