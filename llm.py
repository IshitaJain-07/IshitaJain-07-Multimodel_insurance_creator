import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GENAI_API_KEY")

# Initialize client
client = genai.Client(api_key=api_key)


#client = genai.Client(api_key="AIzaSyBE0utxG6JH-AG9Fgx0LZXaw2de56WNJOQ ")

def generate_text(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",              
        contents=f"Explain this insurance topic in very simple language:\n{prompt}"
    )
    return response.text