import streamlit as st
import sqlite3
import os

def history_page():
    st.markdown("<h2>📜 Content History</h2>", unsafe_allow_html=True)

    # --- DB connection ---
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DB_PATH = os.path.join(BASE_DIR, "users.db")
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()

    # --- Check login ---
    if not st.session_state.get("logged_in") or not st.session_state.get("username"):
        st.info("Please log in to see your history.")
        return

    # --- Fetch user history ---
    cursor.execute("""
        SELECT prompt, content, created_at
        FROM history
        WHERE username = ?
        ORDER BY created_at DESC
    """, (st.session_state.username,))
    rows = cursor.fetchall()

    if not rows:
        st.info("No content generated yet.")
        return

    # --- Initialize selected item ---
    if "selected_history" not in st.session_state:
        st.session_state.selected_history = None

    col1, col2 = st.columns([1.5, 3.7])

    # ---------- LEFT COLUMN: PROMPT LIST ----------
    with col1:
        st.markdown("### 📝 Prompts")

        # Create a list of titles (shortened)
        titles = [item[0] if len(item[0]) <= 35 else item[0][:32] + "..." for item in rows]

        # Determine the safe index
        prev_selection = st.session_state.selected_history[0] if st.session_state.selected_history else None
        selected_index = titles.index(prev_selection) if prev_selection in titles else 0

        # Use radio to select a prompt
        selected_title = st.radio("", titles, index=selected_index)

        # Update selected_history based on radio choice
        for item in rows:
            item_title = item[0] if len(item[0]) <= 35 else item[0][:32] + "..."
            if item_title == selected_title:
                st.session_state.selected_history = item
                break

        # Add CSS for radio buttons
        st.markdown("""
        <style>
        div[role="radiogroup"] label {
            display: block;
            background-color: light-grey;
            color: #000000;
            padding: 1px 1px;
            margin-bottom: 5px;
            border-radius: 8px;
            cursor: pointer;
        }
        div[role="radiogroup"] label:hover {
            background-color: #d4d4d4;
        }
        div[role="radiogroup"] input:checked + span {
            background-color: #a0c4ff;
            font-weight: 800;
        }
        </style>
        """, unsafe_allow_html=True)

    # ---------- RIGHT COLUMN: DISPLAY SELECTED CONTENT ----------
    with col2:
        if st.session_state.selected_history:
            prompt, content, created_at = st.session_state.selected_history
            st.markdown("### 🧾 Content")
            st.markdown(f"""
            <div style="
                background-color: #f0f0f0;
                padding: 10px;
                border-radius: 8px;
                color: #000000;
                font-weight: 500;
            ">
                ✏️ {prompt}
            </div>
            """, unsafe_allow_html=True)
            st.markdown("### 🤖 Generated Content")
            st.write(content)
            st.caption(f"🕒 Generated on: {created_at}")
        else:
            st.info("Select a prompt on the left to view generated content.")
