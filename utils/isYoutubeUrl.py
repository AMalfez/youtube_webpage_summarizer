from urllib.parse import urlparse

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