import streamlit as st

# Configure the browser tab
st.set_page_config(page_title="For You", page_icon="🐈", layout="centered")

# --- COOL MINIMALIST STYLING CODE ---
st.markdown("""
    <style>
    /* Sleek charcoal background */
    .stApp { 
        background-color: #1e1e24 !important;
    }
    
    /* Center alignment and clean typography */
    .content-wrapper {
        text-align: center;
        margin-top: 50px;
    }
    
    /* Cool text style (Crisp white with a hint of romantic coral-red instead of bright pink) */
    .cool-text { 
        font-size: 32px !important; 
        color: #ffffff !important; 
        font-weight: bold;
        font-family: 'Courier New', Courier, monospace;
        letter-spacing: 1px;
        margin-bottom: 20px;
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
    
    /* Monospace style specifically for your flower art */
    .flower-art {
        color: #ff758f !important;
        font-family: monospace !important;
        font-size: 18px !important;
        line-height: 1.2 !important;
        background: transparent !important;
        display: inline-block;
        text-align: left;
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

# 🐈 The cute cat animation asset
st.image("https://giphy.com", width=120)

# Content mapping (Starts directly with "Hello 老婆")
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
    6: "好爱你"
}

# Safely fetch the current page text without exceeding page 6 boundaries
text = pages.get(st.session_state.page, "好爱你")

# Display text safely based on the page (Flower art is now on page 4)
if st.session_state.page == 4:
    st.markdown(f'<pre class="flower-art">{text}</pre>', unsafe_allow_html=True)
else:
    st.markdown(f'<p class="cool-text">{text}</p>', unsafe_allow_html=True)

# Close our content container
st.markdown('</div>', unsafe_allow_html=True)
    
# Clean Next Button
if st.button("NEXT >"):
    # Mathematically caps at page 6 and cycles properly back to 1
    if st.session_state.page < 6:
        st.session_state.page += 1
    else:
        st.session_state.page = 1
    st.rerun()
