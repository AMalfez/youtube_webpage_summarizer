from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    model="moonshotai/kimi-k2-instruct-0905",
)