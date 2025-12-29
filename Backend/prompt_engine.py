def build_prompt(
    content_type: str,
    user_input: str,
    tone: str,
    length_value: int,
    language: str = "English"   
) -> str:
    """
    Builds structured prompt based on content type and language
    """

    # slider value to length instruction
    if length_value == 1:
        length_instruction = "Short and concise (100 words)."
    elif length_value == 2:
        length_instruction = "Medium length (300-500 words)."
    else:
        length_instruction = "Detailed and lengthy with clear sections: introduction, main points, conclusion (800+ words)."

    base_instruction = f"""
    You are an expert content creator.
    Tone: {tone}
    Content Length: {length_instruction}
    Language: {language}  
    Write in plain text using • for bullet points, commas, dashes,double and single inverted commas and proper punctuation.
    """

    if content_type == "LinkedIn Post":
        prompt = f"""
        {base_instruction}
        Write a professional LinkedIn post on the topic:
        "{user_input}"
        
        Include:
        - Engaging opening
        - Clear insights in sections
        - Conclusion
        
        """
    elif content_type == "Ad Content":
        prompt = f"""
        {base_instruction}
        Create ad for:"{user_input}"
        
        Include:
        - Product description and benefits
        - Call to Action
        - Sense of urgency
        """
    elif content_type == "Professional Email":
        prompt = f"""
        {base_instruction}
        Write a professional email regarding:
        "{user_input}"
        
        Include:
        - Subject line
        - Greeting
        - Clear message
        - Polite closing
        """
    else:  # Conversation Draft
        prompt = f"""
        {base_instruction}
        Generate a natural conversation draft about:"{user_input}"
        """

    return prompt.strip()
