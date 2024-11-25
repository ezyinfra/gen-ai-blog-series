from dotenv import load_dotenv
from openai import OpenAI
from typing import Optional
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")
RUN_IN_CLOUD = os.getenv("RUN_IN_CLOUD")

print(f"Starting the App using: OPENAI_API_KEY: {OPENAI_API_KEY}, MODEL_NAME: {MODEL_NAME}, RUN_IN_CLOUD: {RUN_IN_CLOUD}")

def query(
    prompt: str,
    model: str = MODEL_NAME,
    temperature: float = 0.7,
    max_tokens: Optional[int] = None
) -> str:
    """
    Get a chat completion response from OpenAI API or Local LLM model using Ollama.
    
    Args:
        prompt (str): The input prompt/question
        model (str): The model to use (default: gpt-3.5-turbo)
        temperature (float): Controls randomness in the response (0-1)
        max_tokens (Optional[int]): Maximum tokens in the response
        
    Returns:
        str: The model's response text
    """
    if RUN_IN_CLOUD == "true":
        client = OpenAI(api_key=OPENAI_API_KEY)
    else:
        # Local LLM model using Ollama
        client = OpenAI(api_key=OPENAI_API_KEY, base_url="http://localhost:11434/v1")
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        raise Exception(f"Error getting chat completion: {str(e)}")
