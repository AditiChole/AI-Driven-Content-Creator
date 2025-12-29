from Backend.llm import generate_text, generate_hashtags, clean_formatting
from Backend.prompt_engine import build_prompt

def generate_content(user_input, content_type, tone, length_value):
    """
    Generates content based on type, tone, and length.
    For LinkedIn posts, hashtags are generated separately.
    """

    # 1. Build the prompt
    prompt = build_prompt(content_type, user_input, tone, length_value)

    # 2. Set max_tokens based on length
    max_tokens = 4000 if length_value == 3 else 2000

    # 3. Generate main content and clean formatting
    content = clean_formatting(generate_text(prompt, max_tokens=max_tokens))

    # 4. Generate hashtags only for LinkedIn
    if content_type == "LinkedIn Post":
        hashtags = generate_hashtags(content)
        return f"{content}\n\n{hashtags}"

    return content


