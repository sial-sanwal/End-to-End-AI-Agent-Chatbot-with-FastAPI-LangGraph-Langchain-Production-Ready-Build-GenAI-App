# Step 1: Setup API Keys for Groq and Tavily 

import os
from dotenv import load_dotenv
load_dotenv()
# Get the API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")

# Check if the key is loaded correctly
if GROQ_API_KEY:
    print("GROQ_API_KEY  loaded successfully")
else:
    print("Error: GROQ_API_KEY not found")
    
if TAVILY_API_KEY:
    print("TAVILY_API_KEY API Key loaded successfully")
else:
    print("Error: TAVILY_API_KEY not found")
    

# Step 2: Setup LLM & Tools 
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

groq_llm=ChatGroq(model="llama-3.3-70b-versatile")
serach_tool=TavilySearchResults(max_results=2)





# Step 3: Setup AI Agents with Search Tools and functionality 
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage
system_prompt="Act as an AI chatbot who is smart and Friendly"

def get_responce_from_ai_agents(llm_id,query,allow_search,system_prompt,provider):
    if provider=="Groq":
        llm=ChatGroq(model=llm_id)
    tools=[TavilySearchResults(max_results=2) if allow_search else []]


    agent=create_react_agent(
        model=groq_llm,
        tools=tools,
        state_modifier=system_prompt
    )
 
query="tell me about the today date  in pakistan"
state={"messages":query}
responce=agent.invoke(state)
messages=responce.get("messages")
ai_messages=[message.content for message in messages if isinstance (message,AIMessage)]
print(ai_messages[-1])