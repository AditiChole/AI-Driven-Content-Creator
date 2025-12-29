from Backend.llm import generate_text, generate_hashtags, clean_formatting
from Backend.prompt_engine import build_prompt

def generate_content(user_input, content_type, tone, length_value, language="English"):
    """
    Generates content based on type, tone, length, and language.
    For LinkedIn posts, hashtags are generated separately in the same language.
    """

    # Build the prompt
    prompt = build_prompt(content_type, user_input, tone, length_value, language)

    # Set max_tokens based on length
    max_tokens = 4000 if length_value == 3 else 2000

    # Generate main content and clean formatting
    content = clean_formatting(generate_text(prompt, max_tokens=max_tokens))

    # Generate hashtags only for LinkedIn posts
    if content_type == "LinkedIn Post":
        hashtags = generate_hashtags(content, language=language)
        return f"{content}\n\n{hashtags}"

    return content
