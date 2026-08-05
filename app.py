import streamlit as st

# Configure the browser tab title and a cute heart icon
st.set_page_config(page_title="For My Wife ❤️", page_icon="💖", layout="centered")

# --- ROMANTIC STYLING CODE ---
st.markdown("""
    <style>
    /* Gradient romantic background */
    .stApp { 
        background: linear-gradient(135deg, #ffe5ec 0%, #ffc2d1 100%); 
    }
    /* The romantic display box */
    .romantic-box {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0px 10px 30px rgba(255, 75, 115, 0.2);
        text-align: center;
        border: 2px solid #ff8fab;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    /* Make your text look large and beautiful */
    .romantic-text { 
        font-size: 28px !important; 
        color: #ff477e !important; 
        font-weight: bold;
        font-family: 'Microsoft YaHei', sans-serif;
    }
    /* Pretty pink next button */
    div.stButton > button:first-child {
        background-color: #ff477e !important; 
        color: white !important;
        border-radius: 25px !important;
        border: none !important;
        padding: 10px 30px !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #ff7096 !important;
    }
    /* Completely hide Streamlit's default header and padding at the very top */
    header {visibility: hidden;}
    .main .block-container {padding-top: 2rem;}
    </style>
""", unsafe_allow_html=True)

# Initialize page
if "page" not in st.session_state: 
    st.session_state.page = 1

# Open the beautiful white box
st.markdown('<div class="romantic-box">', unsafe_allow_html=True)

# Content mapping (Only your exact text)
pages = {
    1: "Hello World! Welcome to my website.",
    2: "Hello 老婆",
    3: "我爱你",
    4: "想和你约会",
    5: """🌷🌸🌷🌸
🌸🌷🌸🌷🌸
 Λ🌷🌸🌷🌸🌷
( ˘ ᵕ ˘🌷🌸🌷
 ヽ つ＼ ／ UU 
    / 🎀 \ """,
    6: "爱你宝贝",
    7: "好爱你"
}

text = pages[st.session_state.page]

# Display your code or your text based on the page
if st.session_state.page == 5:
    st.text(text)
else:
    st.markdown(f'<p class="romantic-text">{text}</p>', unsafe_allow_html=True)

# Close the white box
st.markdown('</div>', unsafe_allow_html=True)
    
# Next Button
if st.button("Next ➡️"):
    st.session_state.page = (st.session_state.page % 7) + 1
    st.rerun()
