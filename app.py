import streamlit as st

# Configure the browser tab title and a cute heart icon
st.set_page_config(page_title="For My Wife ❤️", page_icon="💖", layout="centered")

# --- ROMANTIC STYLING CODE ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #ffe5ec 0%, #ffc2d1 100%); }
    .romantic-box {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0px 10px 30px rgba(255, 75, 115, 0.2);
        text-align: center;
        border: 2px solid #ff8fab;
    }
    h1 { color: #ff477e !important; font-family: 'Georgia', serif; }
    .romantic-text { font-size: 24px !important; color: #4a4a4a !important; }
    div.stButton > button:first-child {
        background-color: #ff477e !important; color: white !important;
        border-radius: 25px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize page
if "page" not in st.session_state: st.session_state.page = 1

st.markdown('<div class="romantic-box">', unsafe_allow_html=True)

# Content mapping (Your Chinese text + New Design)
pages = {
    1: ("Welcome", "Hello World! Welcome to my website."),
    2: ("Dear 老婆", "Hello 老婆"),
    3: ("My Heart", "我爱你"),
    4: ("Date Request", "想和你约会"),
    5: ("Flowers For You", """🌷🌸🌷🌸
🌸🌷🌸🌷🌸
 Λ🌷🌸🌷🌸🌷
( ˘ ᵕ ˘🌷🌸🌷
 ヽ つ＼ ／ UU 
    / 🎀 \ """),
    6: ("Sweetheart", "爱你宝贝"),
    7: ("Forever", "好爱你")
}

title, text = pages[st.session_state.page]
st.markdown(f"<h1>{title}</h1>", unsafe_allow_html=True)

if st.session_state.page == 5:
    st.text(text)
else:
    st.markdown(f'<p class="romantic-text">{text}</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
    
if st.button("Next ➡️"):
    st.session_state.page = (st.session_state.page % 7) + 1
    st.rerun()
