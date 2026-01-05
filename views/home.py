import streamlit as st

def home_page():
    st.markdown("<h1 style='text-align:center;'>TextFlow AI - AI Content Creator</h1>",unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center;'>Create professional content in seconds</h4>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    cards = [
        ("LinkedIn Post", "Create professional posts for you network. "
        "Boost engagement and showcase your expertise."),
        ("Professional Email", "Draft formal emails in seconds. Save time and communicate clearly."),
        ("Ad Content", "Generate ad copy that converts. Grab attention and increase sales."),
        ("Instagram Caption", "Write catchy captions. Engage your audience instantly. "),
        ("Conversation Draft", "Draft natural messages for any chat. Sound professional and friendly.")
    ]

    for i, (title, desc) in enumerate(cards):
        with col1 if i % 2 == 0 else col2:
            st.markdown(
                f"""
                <div class="card">
                    <h3>{title}</h3>
                    <p>{desc}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            
