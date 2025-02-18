# Step 1: Setup API Keys for Groq and Tavily 

import os
from dotenv import load_dotenv
load_dotenv()
# Get the API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Check if the key is loaded correctly
if GROQ_API_KEY:
    print("API Key loaded successfully")
else:
    print("Error: GROQ_API_KEY not found")
# Step 2: Setup LLM & Tools 
# Step 3: Setup AI Agents with Search Tools and functionality 
 