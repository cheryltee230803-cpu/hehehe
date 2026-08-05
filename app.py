import streamlit as st

# Configure the browser tab
st.set_page_config(page_title="For You", page_icon="🐈", layout="centered")

# --- MINIMALIST STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #1e1e24 !important; }
    .content-wrapper { text-align: center; margin-top: 50px; }
    .cat-display { font-size: 80px !important; margin-bottom: 10px; display: block; }
    .cool-text { font-size: 32px !important; color: #ffffff !important; font-family: 'Courier New', Courier, monospace; }
    div.stButton > button:first-child { background-color: transparent !important; color: #a3e635 !important; border: 2px solid #a3e635 !important; }
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# State management
if "page" not in st.session_state: st.session_state.page = 1
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
st.markdown('<span class="cat-display">🐈‍⬛</span>', unsafe_allow_html=True)

# Content dictionary (Fixed commas & triple-quotes applied)
pages = {
    1: "Hello 老婆",
    2: "我爱你",
    3: "想和你约会",
    4: """🌷🌸🌷🌸\n🌸🌷🌸🌷🌸\n Λ🌷🌸🌷🌸🌷\n( ˘ ᵕ ˘🌷🌸🌷\n ヽ つ＼ ／ UU \n    / 🎀 \ """,
    5: "爱你宝贝",
    6: "好爱你",
    7: "好想你",
    8: """[Large ASCII/Braille Art Placeholder - See Original Code]"""
}

# Display logic
text = pages.get(st.session_state.page, "好爱你")
if st.session_state.page in [4, 8]: st.text(text)
else: st.markdown(f'<p class="cool-text">{text}</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Navigation
if st.button("NEXT >"):
    st.session_state.page = st.session_state.page + 1 if st.session_state.page < 8 else 1
    st.rerun()
