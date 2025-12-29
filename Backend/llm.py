import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_text(prompt: str, max_tokens: int = 2000) -> str:
    """
    Generates text from Groq LLaMA-3 model.
    max_tokens can be increased for long content.
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content

def generate_hashtags(content, language="English"):
    prompt = f"""
    Generate 5-10 relevant hashtags for this LinkedIn post.
    Output them inline separated by spaces, without numbers or extra commentary.
    Language: {language}
    Post content:{content}
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=100
    )
    return response.choices[0].message.content.strip()  # <-- ensures clean output

def clean_formatting(text: str) -> str:
    """
    Converts Markdown symbols to plain text bullets and removes bold formatting.
    """
    return text.replace("* ", "• ").replace("**", "")
