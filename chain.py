from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import YoutubeLoader
from llm import llm
from prompt import prompt
from groq import APIStatusError
import validators
from utils.isYoutubeUrl import is_youtube_url

chain = prompt | llm

def summarize(url: str) -> str:
    try:
        validation = validators.url(url)
        if not validation:
            raise Exception("Invalid URL")
        
        if is_youtube_url(url):
            loader = YoutubeLoader.from_youtube_url(url.strip())
        else:
            loader = WebBaseLoader(url.strip())

        docs = loader.load()

        text = ""
        for doc in docs:
            text += doc.page_content + "\n"

        res = chain.invoke({"content":text})
        return res.content
    except APIStatusError as e:
        raise Exception(f"{e.message}")
    except Exception as e:
        raise Exception(f"{str(e)}")

if __name__ == "__main__":    
    web_url="https://www.geeksforgeeks.org/dsa/binary-tree-data-structure/"
    print(summarize(web_url))