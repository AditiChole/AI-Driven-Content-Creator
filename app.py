import streamlit as st
from auth.auth_services import signup_user, login_user
from styles import load_css
import base64
import os

# -------- IMPORT VIEWS --------
from views.landing import landing_pg
from views.home import home_page
from views.generate import generate_page
from views.history import history_page
from views.profile import profile_page
from views.settings import settings_page

load_css()
st.set_page_config(
    page_title="TextFlow AI | Turning Ideas into Real Impact",
    page_icon="assets/logo3.png", layout="centered")

# -------- SESSION STATE --------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_page" not in st.session_state:
    st.session_state.current_page = "landing"
if "username" not in st.session_state:
    st.session_state.username = None



# -------- AUTH PAGE --------
def auth_page():
    

    # ---------- PATH ----------
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    VIDEO_PATH = os.path.join(BASE_DIR, "assets", "bg2.mp4")

    with open(VIDEO_PATH, "rb") as f:
        video_base64 = base64.b64encode(f.read()).decode()

    # ---------- GLOBAL STYLES ----------
    st.markdown("""
    <style>
.block-container {
    padding: 0 !important;
    margin: 0 !important;
}

html, body, [data-testid="stAppViewContainer"] {
    height: 100%;
    overflow: hidden;
}

/* Full height columns */
div[data-testid="column"] {
    height: 100vh;
}

/* LEFT VIDEO */
.left-video {
    position: relative;
    width: 100%;
    height: 100vh;
    overflow: hidden;
    margin: 0;
    padding: 0;
}

.left-video video {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;  /* cover entire area without gaps */
}

/* RIGHT COLUMN FLEX CENTER */
.right-col > div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.login-box {
    max-width: 420px;
    width: 100%;
}


    </style>
    """, unsafe_allow_html=True)

    # ---------- LAYOUT ----------
    col_left, col_right = st.columns([1, 1], gap="small")

    # ---------- LEFT : VIDEO ----------
    with col_left:
        st.markdown(f"""
        <div class="left-video">
            <video autoplay muted loop playsinline>
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            </video>
        </div>
        """, unsafe_allow_html=True)

    # ---------- RIGHT : LOGIN ----------
    with col_right:
        st.markdown("<div class='right-col'>", unsafe_allow_html=True)
        st.markdown("<div class='login-box'>", unsafe_allow_html=True)

        st.markdown(f"""
        <h2>Welcome to TextFlow AI</h2>
                   """,unsafe_allow_html=True )

        mode = st.radio("", ["Login", "Sign Up"], horizontal=True)

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button(mode, use_container_width=True):
            if mode == "Login":
                success, msg = login_user(email, password)
            else:
                success, msg = signup_user(email, password)

            if success:
                st.session_state.logged_in = True
                st.session_state.username = email
                st.session_state.current_page = "home"
                st.rerun()
            else:
                st.error(msg)

        st.markdown("</div></div>", unsafe_allow_html=True)

# -------- MAIN APP --------
def main_app():
    import streamlit as st
    import base64
    import os

    # ---------------- SESSION ----------------
    st.session_state.setdefault("page", "Home")

    # ---------------- LOGO ----------------
    BASE_DIR = os.path.dirname(__file__)
    LOGO_PATH = os.path.join(BASE_DIR, "assets", "logo4.png")

    with open(LOGO_PATH, "rb") as f:
        logo_base64 = base64.b64encode(f.read()).decode()

    # ---------------- CSS ----------------
    st.markdown("""
    <style>
        /* Sidebar background */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0b132b, #1c2541);
            padding-top: 0 !important;
        }

        /* Logo */
        .logo-box {
            display: flex;
            align-items: left;
            gap: 12px;
            padding: 1px 1px 20px 1px;
        }

        .logo-box img {
            width: 45px;
        }

        .logo-text {
            font-size: 32px;
            font-weight: 600;
            color: white;
        }

        /* Sidebar buttons */
        div.stButton > button {
            background-color: transparent;
            color: #ffffff;
            text-align: right;
            padding: 8px 5px;
            width: 100%;
            border: none;
            border-radius: 12px;
            margin-bottom: 10px;
            font-size: 30px;
            cursor: pointer;
            transition: background 0.2s, transform 0.1s;
        }

        div.stButton > button:hover {
            background: rgba(255,255,255,0.08);
            transform: translateX(5px);
        }

        div.stButton > button:focus {
            outline: none;
        }

        /* Logout button at bottom */
        .logout-btn {
            margin-top: auto;
            background: transparent;
            border: none;
            width: 100%;
            padding: 10px 10px;
            font-size: 18px;
            color: #d1d5db;
            text-align: left;
            border-radius: 20px;
            cursor: pointer;
        }

        .logout-btn:hover {
            background: rgba(255,255,255,0.08);
            transform: translateX(5px);
        }
    </style>
    """, unsafe_allow_html=True)

    # ---------------- SIDEBAR ----------------
    with st.sidebar:

        # Logo
        st.markdown(f"""
        <div class="logo-box">
            <img src="data:image/png;base64,{logo_base64}">
            <div class="logo-text">TextFlow AI</div>
        </div>
        """, unsafe_allow_html=True)

        # Navigation buttons
        nav_items = {
            "Home": "🏠",
            "Generate": "✨",
            "History": "🕘",
            "Profile": "👤",
            "Settings": "⚙️"
        }

        for name, icon in nav_items.items():
            if st.button(f"{icon}  {name}", key=f"nav_{name}"):
                st.session_state.page = name
                st.rerun()

        # Logout button at bottom
        if st.button("🚪 Logout", key="logout"):
            st.session_state.clear()
            st.rerun()

    # ---------------- ROUTING ----------------
    if st.session_state.page == "Home":
        home_page()
    elif st.session_state.page == "Generate":
        generate_page()
    elif st.session_state.page == "History":
        history_page()
    elif st.session_state.page == "Profile":
        profile_page()
    elif st.session_state.page == "Settings":
        settings_page()

# -------- ROUTER (MOST IMPORTANT PART) -------- 
if not st.session_state.logged_in: 
    if st.session_state.current_page == "landing": 
        landing_pg()
    elif st.session_state.current_page == "login":
        auth_page() 
else: 
    main_app()