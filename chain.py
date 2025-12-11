from langchain_unstructured import UnstructuredLoader
from langchain_community.document_loaders import YoutubeLoader
from llm import llm
from prompt import prompt
from groq import APIStatusError

chain = prompt | llm

def summarize(url: str) -> str:
    try:
        if "youtube.com" or "youtu.be" in url:
            loader = YoutubeLoader.from_youtube_url(
                url, 
                # add_video_info=True
            )
        else:
            loader = UnstructuredLoader(web_url=url)

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
    web_url="https://youtu.be/Pmd6knanPKw?si=sfLUl3iyq-96fyLd"
    print(summarize(web_url))