import streamlit as st  
import base64
import os

# ---------- Helper ----------
def get_base64_file(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def landing_pg():
    st.set_page_config(layout="wide", page_title="TextFlow AI | Turning Ideas into Real Impact")

    # ---------- Hide default Streamlit UI ----------
    st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {padding:0; margin:0;}
        html, body, [data-testid="stAppViewContainer"] {height:100%; margin:0; overflow-x:hidden;}
    </style>
    """, unsafe_allow_html=True)

    # ---------- Paths ----------
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # project root
    VIDEO_PATH = os.path.join(BASE_DIR, "assets", "vid2.mp4")
    ABOUT_BG = os.path.join(BASE_DIR, "assets", "background.jpg")
    SUBS_BG = os.path.join(BASE_DIR, "assets", "background.jpg")

    video_base64 = get_base64_file(VIDEO_PATH)
    about_bg_base64 = get_base64_file(ABOUT_BG)
    subs_bg_base64 = get_base64_file(SUBS_BG)

    # ---------- Navbar & Hero CSS ----------
    st.markdown("""
    <style>
    /* Navbar container */
    .navbar {
        position: fixed;
        top: 0;  /* moved to top to remove blank space */
        right: 40px;
        z-index: 10;
        display: flex;
        align-items: center;
        gap: 30px;
    }

    .nav-link {
        color:white !important;
        font-weight:600;
        text-decoration:none;
        cursor:pointer;
        font-size:16px;
    }
    .nav-link:hover { color:#f6c453 !important; }

    /* Hero & sections */
    .section {
        position:relative;
        height:100vh;
        width:100%;
        display:flex;
        justify-content:center;
        align-items:center;
        text-align:center;
        color:white;
        font-size:36px;
        text-shadow:2px 2px 5px black;
        scroll-margin-top:0;  /* removed extra scroll margin */
        flex-direction:column;
        padding:0;  /* removed extra padding */
    }
    .section .overlay {
        position:absolute; inset:0;
        background:rgba(0,0,0,0.55);
        z-index:1;
    }
    .section-content {
        position:relative;
        z-index:2;
        max-width:900px;
        padding:20px;
    }

    /* Hero video */
    .hero video {
        position:absolute;
        top:0; left:0;
        width:100%; height:100%;
        object-fit:cover;
        z-index:1;
    }
    .hero .overlay { position:absolute; inset:0; background:rgba(0,0,0,0.55); z-index:2; }
    .hero-content { position:relative; z-index:3; max-width:900px; padding:20px; }
    .hero-content h1 { font-size:40px; font-weight:bold; }
    .hero-content p { font-size:20px; line-height:1.6; }
    </style>
    """, unsafe_allow_html=True)

    # ---------- Navbar using Streamlit columns ----------
    col1, col2, col3, col4 = st.columns([6,0.9,1,1])
    with col2:
        if st.button("About"):
            st.experimental_set_query_params(section="about")
    with col3:
        if st.button("Subscription"):
            st.experimental_set_query_params(section="subscription")
    with col4:
        if st.button("Login / Sign Up"):
            st.session_state.current_page = "login"  # redirect to login page

    # ---------- Hero Section ----------
    st.markdown(f"""
    <div class="section hero" id="hero">
        <video autoplay muted loop playsinline>
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
    </div>
    """, unsafe_allow_html=True)

    # ---------- About Section ----------
    st.markdown(f"""
    <div class="section" id="about" style="background: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)), url('data:image/png;base64,{about_bg_base64}') center/cover no-repeat;">
        <div class="overlay"></div>
        <div class="section-content">
            <h2>About Us</h2>
            <p>A smart content creation platform designed to transform your ideas into
            clear, compelling, and impactful text. TextFlow AI helps you write faster,
            better, and with confidence.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---------- Subscription Section ----------
    st.markdown(f"""
    <div class="section" id="subscription" style="background: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)), url('data:image/png;base64,{subs_bg_base64}') center/cover no-repeat;">
        <div class="overlay"></div>
        <div class="section-content">
            <h2>Subscribe for Updates</h2>
    """, unsafe_allow_html=True)

    email = st.text_input("Enter your email")
    if st.button("Subscribe"):
        st.success(f"Subscribed with {email}")

    st.markdown("</div></div>", unsafe_allow_html=True)
