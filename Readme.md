# AI Chatbot Agent with LangGraph & LangChain

This project allows you to create and interact with AI agents built using **LangChain**, **Groq**, and **Tavily** search tools. You can define your agent's behavior, query different models (Groq, OpenAI), and interact with the agent via a simple web interface powered by **Streamlit**.

## Features
- **Create AI Chatbots** with custom system prompts.
- **Search functionality** using the Tavily API.
- **Model support** for **Groq** and **OpenAI**.
- **Web interface** built with **Streamlit** for interacting with the AI agents.

## Requirements

Before you start, ensure you have the following dependencies installed:

- **Python 3.7+**
- **poetry** (for managing dependencies)
- **Groq API Key** (for Groq Model)
- **Tavily API Key** (for Tavily search)
- **LangChain** (for LLM integration)
- **Streamlit** (for the web interface)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/langgraph-agent.git
   cd langgraph-agent
2. Set up the environment using Poetry:
```bash 
    poetry install

```
3. Create a .env file in the root directory and add your API keys:
```bash
    GROQ_API_KEY=your_groq_api_key
    TAVILY_API_KEY=your_tavily_api_key

```

