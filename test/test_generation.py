from Backend.content_generation import generate_content

if __name__ == "__main__":
    prompt = "AI in digital marketing"

    content_types = ["LinkedIn", "Email", "Advertisement", "Conversation"]

    for ctype in content_types:
        print(f"\n--- {ctype} ---")
        print(generate_content(prompt, ctype))
