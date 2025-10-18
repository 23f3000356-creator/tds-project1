# openai_utils.py
import os
from openai import OpenAI

# Load model name and API key from environment variables
_MODEL = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")
_API_KEY = os.getenv("OPENAI_API_KEY")

if not _API_KEY:
    raise RuntimeError("OPENAI_API_KEY not set in environment")

# Initialize OpenAI client
client = OpenAI(api_key=_API_KEY)

def generate_code_snippet(prompt: str, max_output_tokens: int = 1024) -> str:
    """
    Generate text/code from OpenAI using the 'responses.create' method.
    Returns the generated text or raises an error on failure.
    """
    try:
        response = client.responses.create(
            model=_MODEL,
            input=prompt,
            max_output_tokens=max_output_tokens
        )

        # Extract the text content safely
        if response.output and len(response.output) > 0:
            return response.output[0].content[0].text
        else:
            return "⚠️ No output generated."

    except Exception as e:
        raise RuntimeError(f"OpenAI generation failed: {e}")
