import streamlit as st

def load_css():
    st.markdown("""
        <style>
        /* Main background */
        .stApp {
            background-color: #F8FAFC;
            color: #0F172A;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #0F172A;
            color: white;
        }

        section[data-testid="stSidebar"] * {
            color: white;
        }

        /* Buttons */
        .stButton>button {
            background-color: #4F46E5;
            color: white;
            border-radius: 8px;
            padding: 10px 16px;
            border: none;
            font-weight: 500;
        }

        .stButton>button:hover {
            background-color: #4338CA;
        }

        /* Inputs */
        input, textarea, select {
            border-radius: 8px !important;
        }

        /* Card */
        .card {
        background-color: white;
        padding: 24px;
        border-radius: 14px;
        border: 1px solid #E5E7EB;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.04);
        margin-bottom: 20px;
        cursor: pointer;
        transition: all 0.2s ease-in-out;
        position: relative;
        }


        .card:hover {
        transform: translateY(-3px);
        box-shadow: 0px 10px 24px rgba(0,0,0,0.08);
        border-color: #4F46E5;
    }

    .card p {
        color: #64748B;
        font-size: 14px;
    }

    .card-btn button {
        position: absolute;
        inset: 0;
        opacity: 0;
        cursor: pointer;
    }
        </style>
    """, unsafe_allow_html=True)
