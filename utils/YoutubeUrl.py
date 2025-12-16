import os
from urllib.parse import urlparse
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig
import os

def is_youtube_url(url: str) -> bool:
    try:
        parsed_url = urlparse(url.strip())
        domain = parsed_url.hostname or ""
        youtube_domains = {
            "youtube.com",
            "www.youtube.com",
            "m.youtube.com",
            "youtu.be"
        }
        return domain in youtube_domains
    except Exception:
        return False
    

def extract_video_id(url: str) -> str:
    try:
        parsed_url = urlparse(url.strip())
        if parsed_url.hostname in ["youtu.be"]:
            return parsed_url.path[1:]
        if parsed_url.hostname in ["www.youtube.com", "youtube.com", "m.youtube.com"]:
            if parsed_url.path == "/watch":
                query_params = parsed_url.query.split("&")
                for param in query_params:
                    key, value = param.split("=")
                    if key == "v":
                        return value
            elif parsed_url.path.startswith("/embed/"):
                return parsed_url.path.split("/")[2]
            elif parsed_url.path.startswith("/v/"):
                return parsed_url.path.split("/")[2]
        return ""
    except Exception:
        return ""
    

def load_transcript(video_id: str):
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript_list = ytt_api.list(video_id)
        transcript = transcript_list.find_transcript(['en'])
        ans = ""
        for entry in transcript.fetch():
            ans += entry.text + " "

        return ans

    except Exception as e:
        raise Exception(f"Could not retrieve transcript: {str(e)}")
    
if __name__ == "__main__":
    test_urls = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://youtu.be/dQw4w9WgXcQ",
        "https://m.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/embed/dQw4w9WgXcQ",
        "https://www.youtube.com/v/dQw4w9WgXcQ",
        "https://www.example.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/watch?v=Op4EMZXWjyE&list=RDvB0V3iCSzQw&index=25"
    ]

    transcript_url = "https://www.youtube.com/watch?v=nMkQUlBtFlk"
    
    for url in test_urls:
        print(f"URL: {url}")
        print(f"Is YouTube URL: {is_youtube_url(url)}")
        print(f"Video ID: {extract_video_id(url)}")
        print("-" * 40)

    if is_youtube_url(transcript_url):
        video_id = extract_video_id(transcript_url)
        print(f"Transcript: {load_transcript(video_id)}")