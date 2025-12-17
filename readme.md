# AI Summarizer

An intelligent content summarization tool that automatically generates concise summaries of YouTube videos and web pages using AI. Built with LangChain, FastAPI, and React.

## 🌟 Features

- **YouTube Video Summarization**: Extract and summarize video transcripts from YouTube URLs
- **Web Page Summarization**: Summarize content from any public web page
- **RESTful API**: Easy-to-use API endpoints for integration with other applications
- **React Chat Interface**: User-friendly chat-based interface for submitting URLs and viewing summaries
- **AI-Powered**: Leverages the Moonshotai Kimi K2 Instruct model via Groq for intelligent summarization
- **Proxy Support**: Built-in proxy configuration for YouTube transcript fetching

## 🛠️ Tech Stack

### Backend
- **FastAPI**: High-performance web framework for building APIs
- **LangChain**: Framework for developing LLM-powered applications
- **Groq**: API for accessing LLM models
- **BeautifulSoup4**: Web scraping and HTML parsing
- **YouTube Transcript API**: Fetch video transcripts

### Frontend
- **React**: Modern JavaScript library for building user interfaces

### AI Model
- **Moonshotai Kimi K2 Instruct**: Advanced language model for content summarization

## 📋 Prerequisites

- Python 3.8+
- Node.js and npm (for frontend)
- Groq API key
- Webshare proxy credentials (for YouTube transcripts)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-summarizer.git
cd ai-summarizer
```

### 2. Backend Setup

#### Install Python Dependencies

```bash
pip install -r requirements.txt
```

#### Configure Environment Variables

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit the `.env` file with your credentials:

```env
GROQ_API_KEY="your-groq-api-key"
FRONTEND_URL="http://localhost:5173"
ENV="dev"
PROXY_USERNAME="your-proxy-username"
PROXY_PASSWORD="your-proxy-password"
```

### 3. Frontend Setup

*(Note: Frontend setup instructions should be added based on your React application structure)*

```bash
cd frontend
npm install
```

## 🎯 Usage

### Starting the Backend Server

Run the FastAPI server:

```bash
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

### Starting the Frontend

```bash
cd frontend
npm run dev
```

The interface will be available at `http://localhost:5173`

### API Endpoints

#### Root Endpoint
```http
GET /
```
Returns a simple greeting message.

**Response:**
```json
{
  "Hello": "World"
}
```

#### Summarize Endpoint
```http
POST /summary
```

**Request Body:**
```json
{
  "url": "https://www.youtube.com/watch?v=example"
}
```

**Response (Success):**
```json
{
  "summary": "This is the AI-generated summary of the content..."
}
```

**Response (Error):**
```json
{
  "error": "Error message"
}
```

### Testing the API

You can test the summarization functionality directly:

```bash
python chain.py
```

This will run the example URLs defined in the `__main__` block.

## 📁 Project Structure

```
ai-summarizer/
├── app.py                 # FastAPI application and API routes
├── chain.py              # Core summarization logic
├── llm.py                # LLM configuration
├── prompt.py             # Prompt templates for AI
├── requirements.txt      # Python dependencies
├── .env.example          # Example environment variables
├── .gitignore           # Git ignore rules
├── utils/
│   └── YoutubeUrl.py    # YouTube URL handling and transcript extraction
└── frontend/            # React frontend application
```

## 🔧 Core Components

### `app.py`
FastAPI application with CORS middleware and API endpoints for content summarization.

### `chain.py`
Contains the main `summarize()` function that:
- Validates input URLs
- Determines if URL is YouTube or web page
- Fetches content (transcript or webpage)
- Generates AI summary using LangChain

### `llm.py`
Configures the LLM using ChatGroq with the Moonshotai Kimi K2 Instruct model.

### `prompt.py`
Defines the chat prompt template for the AI assistant.

### `utils/YoutubeUrl.py`
Utility functions for:
- Detecting YouTube URLs
- Extracting video IDs
- Fetching transcripts with proxy support

## 🔒 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Your Groq API key for accessing the LLM | Yes |
| `FRONTEND_URL` | URL of your frontend application | Yes |
| `ENV` | Environment (dev/prod) | Yes |
| `PROXY_USERNAME` | Webshare proxy username for YouTube | Yes |
| `PROXY_PASSWORD` | Webshare proxy password for YouTube | Yes |

## 🧪 Example Usage

### Summarizing a YouTube Video

```python
from chain import summarize

youtube_url = "https://www.youtube.com/watch?v=example"
summary = summarize(youtube_url)
print(summary)
```

### Summarizing a Web Page

```python
from chain import summarize

web_url = "https://www.example.com/article"
summary = summarize(web_url)
print(summary)
```

## 🐛 Error Handling

The application handles various error scenarios:
- Invalid URLs
- API rate limits
- Missing transcripts
- Network errors
- Invalid proxy configurations

All errors are returned with descriptive messages to help with debugging.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- LangChain for the powerful LLM framework
- Groq for providing access to advanced AI models
- FastAPI for the excellent web framework
- The open-source community for various tools and libraries

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Note**: Remember to keep your API keys and proxy credentials secure. Never commit the `.env` file to version control.