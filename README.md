# AI Content Creator

**AI Content Creator is a Python-based tool that generates LinkedIn posts, Ad copy, professional emails, and conversation drafts using Groq LLaMA-3. It supports multiple content lengths, tones, and languages.**

---

## **Features**

* Generate **LinkedIn posts** with structured sections (Intro, Main Points, Conclusion)
* Plain text bullets (`•`) and clean formatting
* Generate **inline hashtags** for LinkedIn posts
* Support for **Ad copy, professional emails, and conversation drafts**
* Adjustable **content length**: Short, Medium, Long
* Multiple **tones**: Professional, Casual, Persuasive
* Multilingual content generation:
  - Supports English, Hindi, French, Spanish, German, Chinese, Japanese, Arabic, Portuguese, Russian, Italian, Korean, Dutch, Turkish, Indonesian
  - Hashtags are also generated in the selected language
  - Dropdown selection in Streamlit for easy language choice

---

## **Usage**

```python
from Backend.content_generation import generate_content

post = generate_content(
    user_input="Digital Marketing Strategies",
    content_type="LinkedIn Post",
    tone="Professional",
    length_value=3  # 1=Short, 2=Medium, 3=Long
    language = "English"
)

print(post)
```

* Generates content with **plain bullets** and **inline hashtags** for LinkedIn posts.
* Works similarly for Ad copy, emails, and conversation drafts.

---

## **Function Reference**

* `generate_content(user_input, content_type, tone, length_value)` → main function
* `generate_text(prompt, max_tokens=2000)` → calls Groq LLaMA-3
* `generate_hashtags(content)` → generates LinkedIn hashtags
* `clean_formatting(text)` → converts Markdown to plain text bullets
* `build_prompt(content_type, user_input, tone, length_value)` → creates structured prompt

---

## **Example Output (LinkedIn Post, Long)**

```
• Introduction:
Digital marketing is essential for business growth in the modern era...

• Key Strategies:
• Build a comprehensive content plan including blogs, videos, and social media posts...
• Optimize your website for SEO...

• Conclusion:
Implementing these strategies helps increase visibility and generate leads.

#DigitalMarketing #BusinessGrowth #MarketingStrategy #SocialMedia #LeadGeneration
```

---

## Flow Diagram explaining the working of model
   +-----------------------+
   |   User Input/Settings |
   |-----------------------|
   | topic, content_type,  |
   | tone, length_value    |
   +-----------+-----------+
               |
               v
   +-----------------------+
   |  prompt_engine.py     |
   |-----------------------|
   | build_prompt()        |
   | Creates structured    |
   | prompt based on type, |
   | tone, and length      |
   +-----------+-----------+
               |
               v
   +-----------------------+
   |       llm.py          |
   |-----------------------|
   | generate_text()       |
   | Sends prompt to LLaMA |
   | model and gets output |
   |-----------------------|
   | clean_formatting()    |
   | Converts Markdown     |
   | bullets to plain text |
   |-----------------------|
   | generate_hashtags()   |
   | Generates inline      |
   | LinkedIn hashtags     |
   +-----------+-----------+
               |
               v
   +-----------------------+
   | content_generation.py |
   |-----------------------|
   | Calls build_prompt()  |
   | Calls generate_text() |
   | Calls generate_hashtags() |
   | Combines final output |
   +-----------+-----------+
               |
               v
   +-----------------------+
   |  Final Output         |
   |-----------------------|
   | LinkedIn Post / Ad /  |
   | Email / Conversation  |
   | With bullets & hashtags|
   +-----------------------+


## **Notes**

* Hashtags are generated **only for LinkedIn posts**.
* Long content uses **higher max tokens** to prevent truncation.
* Output formatting is clean and ready to post.


