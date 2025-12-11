from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate(
    [
        ("system", "You are a helpful assistant that summarizes YouTube video transcripts or webpage content."),
        ("user", "Summarize the following content: {content}"),
    ]
)