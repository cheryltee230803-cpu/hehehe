import streamlit as st

# Configure the browser tab
st.set_page_config(page_title="For You", page_icon="🐈", layout="centered")

# --- COOL MINIMALIST STYLING CODE ---
st.markdown("""
    <style>
    /* Sleek charcoal background */
    .stApp { background-color: #1e1e24 !important; }
    
    /* Center alignment and clean typography */
    .content-wrapper { text-align: center; margin-top: 50px; }
    
    /* Massive cute cat styling */
    .cat-display { font-size: 80px !important; margin-bottom: 10px; display: block; }
    
    /* Cool text style (Crisp white with a monospace look) */
    .cool-text { 
        font-size: 32px !important; 
        color: #ffffff !important; 
        font-weight: bold;
        font-family: 'Courier New', Courier, monospace;
        letter-spacing: 1px;
        margin-bottom: 25px;
    }
    
    /* Sleek minimalist button */
    div.stButton > button:first-child {
        background-color: transparent !important; 
        color: #a3e635 !important; /* Cool neon lime accent */
        border: 2px solid #a3e635 !important;
        border-radius: 8px !important;
        padding: 8px 24px !important;
        font-size: 16px !important;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold !important;
        transition: all 0.2s ease-in-out;
    }
    
    div.stButton > button:first-child:hover {
        background-color: #a3e635 !important;
        color: #1e1e24 !important;
        box-shadow: 0px 0px 15px rgba(163, 230, 53, 0.4);
    }
    
    /* Monospace container style for the art layouts */
    .art-container {
        color: #ffffff !important;
        font-family: monospace !important;
        font-size: 22px !important;
        white-space: pre !important;
        display: inline-block;
        text-align: left;
        margin-bottom: 25px;
    }

    /* Hide standard Streamlit header clutter */
    header {visibility: hidden;}
    .main .block-container {padding-top: 3rem;}
    </style>
""", unsafe_allow_html=True)

# Initialize page state
if "page" not in st.session_state: 
    st.session_state.page = 1

# Open our clean content container
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# 🐈 Render a giant text-based cat emoji.
st.markdown('<span class="cat-display">🐈‍⬛</span>', unsafe_allow_html=True)

# Content mapping (Page 8 updated with your new hugging cats art!)
pages = {
    1: "Hello 老婆",
    2: "我爱你",
    3: "想和你约会",
    4: """🌷🌸🌷🌸
🌸🌷🌸🌷🌸
 Λ🌷🌸🌷🌸🌷
( ˘ ᵕ ˘🌷🌸🌷
 ヽ つ＼ ／ UU 
    / 🎀 \ """,
    5: "爱你宝贝",
    6: "好爱你",
    7: "好想你",
    8: """  /\_ /\  /\ _ /\ 
 (,, ´∀`,,) W<   )--♡
   /︵  づ⊂︵ \ """,
    9: "byebye"
}

# Safely fetch the current page text
text = pages.get(st.session_state.page, "好爱你")

# Display text safely based on the page
if st.session_state.page == 4:
    st.text(text)
    st.markdown('<p class="cool-text">给你花花</p>', unsafe_allow_html=True)
elif st.session_state.page == 8:
    # Uses a special clean alignment rule so your new cats stay perfectly in shape
    st.markdown(f'<div class="art-container">{text}</div>', unsafe_allow_html=True)
else:
    st.markdown(f'<p class="cool-text">{text}</p>', unsafe_allow_html=True)

# Close our content container
st.markdown('</div>', unsafe_allow_html=True)
    
# Clean Next Button
if st.button("NEXT >"):
    # Allows a seamless transition through all 9 pages
    if st.session_state.page < 9:
        st.session_state.page += 1
    else:
        st.session_state.page = 1
    st.rerun()
