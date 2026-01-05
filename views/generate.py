import streamlit as st
from Backend.content_generation import generate_content, save_history

def generate_page():
    st.markdown("<h2>Generate Content</h2>", unsafe_allow_html=True)
    st.markdown("<h4>Fill the details and let AI do the work</h4>", unsafe_allow_html=True)

    # Initialize session state
    if "generated_content" not in st.session_state:
        st.session_state.generated_content = ""

    # --- Form for inputs + button ---
    with st.form(key="generate_form"):
        col1, col2 = st.columns([1, 2])

        with col1:
            content_type = st.selectbox(
                "Content Type",
                ["LinkedIn Post", "Professional Email", "Ad Content", "Instagram Caption", "Conversation Draft"]
            )
            audience = st.selectbox(
                "Target Audience",
                ["General Audience", "Students", "Professionals", "Entrepreneurs", "Marketers", "Developers", "Business Owners"]
            )
            tone = st.selectbox(
                "Tone",
                ["Professional", "Casual", "Friendly", "Persuasive", "Formal"]
            )
            language = st.selectbox(
                "Language",
                ["English", "Hindi", "Spanish", "French", "German"]
            )
            length_value = st.slider(
                "Select Content Length",
                1, 3, 2,
                help="Short ≈ 100 words | Medium ≈ 200 words | Long ≈ 400+ words"
            )
            length_label = {1: "Short (~100 words)", 2: "Medium (~200 words)", 3: "Long (~400+ words)"}
            st.caption(f"📝 Selected length: **{length_label[length_value]}**")

        with col2:
            user_input = st.text_area(
                "Topic / Prompt",
                height=200,
                placeholder="Enter your topic or idea..."
            )

        # ✅ Generate button inside form
        submit_button = st.form_submit_button("Generate Content")

    # --- Handle generation ---
    if submit_button:
        if not user_input.strip():
            st.warning("Please enter a topic.")
        else:
            with st.spinner("Generating content..."):
                # Generate content
                content = generate_content(
                    user_input,
                    content_type,
                    tone,
                    audience,
                    length_value,
                    language
                )
                


                # Save to history if user is logged in
                if st.session_state.get("logged_in", False) and st.session_state.get("username"):
                    save_history(st.session_state.username, user_input, content)

                # Assign to session state to display
                st.session_state.generated_content = content
                


    # --- Show output ---
    if st.session_state.generated_content:
        st.success("Content Generated Successfully!")
        st.text_area("Generated Content", st.session_state.generated_content, height=300)

        colA, colB, colC = st.columns(3)
        with colA:
            st.download_button(
                label="⬇️ Download",
                data=st.session_state.generated_content,
                file_name="generated_content.txt",
                mime="text/plain"
            )

        with colC:
            if st.button("🔁 Regenerate"):
                st.session_state.generated_content = ""
