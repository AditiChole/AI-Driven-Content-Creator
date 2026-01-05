import streamlit as st
import sqlite3
import os
from io import BytesIO
import pandas as pd
import plotly.express as px
from auth.auth_services import update_password

def profile_page():
    st.markdown("<h1 style='text-align:center;'>👤 Profile</h1>", unsafe_allow_html=True)

    # --- DB connection ---
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DB_PATH = os.path.join(BASE_DIR, "users.db")
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()

    # --- Check login ---
    if not st.session_state.get("logged_in") or not st.session_state.get("username"):
        st.info("Please log in to view your profile.")
        return

    user_email = st.session_state.username  # username stores email

    # ---------- Avatar Upload ----------
    st.subheader("Profile Picture")
    if "avatar" not in st.session_state:
        st.session_state.avatar = None

    col1, col2 = st.columns([1,3])
    with col1:
        avatar_file = st.file_uploader("Upload Avatar", type=["png","jpg","jpeg"])
        if avatar_file:
            st.session_state.avatar = avatar_file

    with col2:
        if st.session_state.avatar:
            # Show uploaded avatar immediately
            img_bytes = avatar_file.read() if avatar_file else None
            if img_bytes:
                st.image(BytesIO(img_bytes), width=120)
            else:
                st.image(st.session_state.avatar, width=120)
        else:
            st.image("https://via.placeholder.com/120?text=Avatar", width=120)

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------- Account Info & Stats ----------
    # Total contents generated
    cursor.execute("SELECT COUNT(*) FROM history WHERE username = ?", (user_email,))
    total_generated = cursor.fetchone()[0]

    col1, col2 = st.columns([3,2])
    with col1:
        st.markdown(f"""
        <div style='
            background-color:#f0f2f6; 
            padding:20px; 
            border-radius:10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        '>
        <h3>Account Info</h3>
        <p><b>Email:</b> {user_email}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style='
            background-color:#f0f2f6; 
            padding:20px; 
            border-radius:10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            text-align:center;
        '>
        <h3>Stats</h3>
        <h2 style='color:#6a0dad'>{total_generated}</h2>
        <p>Total AI Contents Generated</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------- Change Password ----------
    st.subheader("Change Password 🔑")
    with st.form(key="change_password_form"):
        current_password = st.text_input("Current Password", type="password")
        new_password = st.text_input("New Password", type="password")
        submit = st.form_submit_button("Update Password")
        if submit:
            if not current_password or not new_password:
                st.error("Please fill both fields")
            else:
                success, msg = update_password(user_email, current_password, new_password)
                if success:
                    st.success(msg)
                else:
                    st.error(msg)

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------- Weekly Usage Line Graph ----------
    st.subheader("Weekly AI Content Usage 📈")
    cursor.execute("""
        SELECT strftime('%Y-%W', created_at) as week, COUNT(*) as count
        FROM history 
        WHERE username = ?
        GROUP BY week
        ORDER BY week ASC
    """, (user_email,))
    data = cursor.fetchall()

    if data:
        df = pd.DataFrame(data, columns=["Week", "Contents Generated"])
        # Optional: make week readable
        df["Week Label"] = df["Week"].apply(lambda x: f"Week {x.split('-')[1]}, {x.split('-')[0]}")
        fig = px.line(
            df,
            x="Week Label",
            y="Contents Generated",
            markers=True,
            title="Weekly AI Content Usage",
            labels={"Contents Generated": "AI Contents Generated", "Week Label": "Week"}
        )
        fig.update_traces(line=dict(color="#6a0dad", width=3))
        fig.update_layout(
            xaxis_tickangle=-45,
            plot_bgcolor="white",
            xaxis=dict(showgrid=True, gridcolor="#f0f0f0"),
            yaxis=dict(showgrid=True, gridcolor="#f0f0f0")
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No activity yet. Start generating AI content!")

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("You can logout anytime from the sidebar.")
    conn.close()
