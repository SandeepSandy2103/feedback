import streamlit as st

# Page config
st.set_page_config(page_title="Feedback App", layout="centered")

# Apply custom CSS
st.markdown("""
    <style>
        .main-container {
            background-color: #f5f7fa;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #4a90e2;
        }
        .stButton>button {
            background-color: #4a90e2;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            font-size: 16px;
            margin: 0.5rem 0;
        }
        .stButton>button:hover {
            background-color: #3b7dd8;
        }
        .feedback-card {
            background-color: #ffffff;
            padding: 1rem;
            margin-top: 1rem;
            border-left: 5px solid #4a90e2;
            border-radius: 5px;
        }
        .username {
            font-weight: bold;
            color: #333;
        }
        .message {
            color: #666;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize feedback storage
if 'feedbacks' not in st.session_state:
    st.session_state.feedbacks = []

# App layout
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("🌟 Feedback Application")

# Feedback form
username = st.text_input("Enter your name:")
message = st.text_area("Your message:")

if st.button("Submit Feedback"):
    if username and message:
        st.session_state.feedbacks.append({'username': username, 'message': message})
        st.success("Thank you for your feedback!")
    else:
        st.error("Please fill in both fields.")

# Display feedback
if st.button("View All Feedback"):
    if st.session_state.feedbacks:
        st.markdown("### 💬 All Feedbacks")
        for fb in reversed(st.session_state.feedbacks):
            st.markdown(f"""
                <div class="feedback-card">
                    <div class="username">@{fb['username']}</div>
                    <div class="message">{fb['message']}</div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No feedback submitted yet.")

st.markdown('</div>', unsafe_allow_html=True)
