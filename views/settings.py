import streamlit as st

def settings_page():
    st.title("⚙️ Settings")

    st.selectbox(
        "Default Tone",
        ["Professional", "Casual", "Friendly", "Persuasive", "Formal"]
    )

    st.selectbox(
        "Default Language",
        ["English", "Hindi", "Spanish", "French", "German"]
    )

    st.info("Settings will be saved in future updates.")
