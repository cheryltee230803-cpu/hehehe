import streamlit as st

# Initialize the text screen count if it doesn't exist
if "page" not in st.session_state:
    st.session_state.page = 1

# Display different text based on the "page" number
if st.session_state.page == 1:
    st.write("Hello World! Welcome to my website.")
elif st.session_state.page == 2:
    st.write("Hello 老婆")
elif st.session_state.page == 3:
    st.write("我爱你")
elif st.session_state.page == 4:
    st.write("想和你约会")
elif st.session_state.page == 5:
    st.text("""🌷🌸🌷🌸
🌸🌷🌸🌷🌸
 Λ🌷🌸🌷🌸🌷
( ˘ ᵕ ˘🌷🌸🌷
 ヽ つ＼ ／ UU 
    / 🎀 \ """)
elif st.session_state.page == 6:
    st.write("爱你宝贝")
elif st.session_state.page == 7:
    st.write("好爱你")
    
# Create the "Next" button
if st.button("Next"):
    if st.session_state.page < 5:  # Changed to 5 so it goes all the way to the flowers
        st.session_state.page += 1
    else:
        st.session_state.page = 1  # Loop back to page 1
    st.rerun()
