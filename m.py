import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file (if used)
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize client
client = OpenAI(api_key=api_key)

# Try a simple API call
try:
    response = client.models.list()
    print(" OpenAI API key is valid!")
    print("Available models:")
    for model in response.data[:5]:  # show first 5
        print(" -", model.id)
except Exception as e:
    print("❌ Invalid or expired OpenAI API key.")
    print("Error details:", e)
        