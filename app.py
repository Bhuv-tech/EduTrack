import streamlit as st
import random

from analysis import analysis
from iqtest import iq_test
from mental_energy_check import mental_energy
from study_habits import study_habits

default_quotes = [
    "Believe in yourself and all that you are.",
    "Every day is a new beginning.",
    "You are capable of amazing things.",
    "Stay positive, work hard, make it happen.",
    "Difficult roads often lead to beautiful destinations."
]

def load_quotes(filename="quotes.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return default_quotes

quotes = load_quotes()

def motivation_booster():
    st.header("🌟 Motivation Booster")
    with st.form("motivation_form"):
        feeling = st.radio("How are you feeling today?", ["Great", "Okay", "Not so good"])
        submitted = st.form_submit_button("Get Motivation Boost")
    if submitted:
        if feeling == "Great":
            score = 10
            st.write("🌈 Awesome! Keep that energy up! You're unstoppable!")
        elif feeling == "Okay":
            score = 7
            st.write("🌤 It's a good day! Remember, every step counts. You're doing well!")
        else:
            score = 4
            st.write("🌧️ It's okay to have off days. Remember, even the best athletes have bad days. You're still making progress!")
        quote = random.choice(quotes).strip()
        st.write(f"\n💬 Motivation Quote: {quote}\n")
        st.success(f"Motivation score: {score}/10")
        st.info(f"{quote}")

def home():
    st.markdown(
        """
        <div style="text-align:center">
            <h1 style="font-size:3em; color:#6c63ff;">🎓 Welcome to EduTrack!</h1>
            <img src="https://cdn.pixabay.com/photo/2017/01/31/13/14/brain-2029365_1280.png" width="200"/>
            <h2 style="color:#ff6f61;">Your Personal Learning & Wellness Companion</h2>
            <p style="font-size:1.2em;">
                Unlock your potential with fun IQ quizzes, boost your motivation, check your mental energy, and improve your study habits.<br>
                <b>Navigate using the menu on the left to get started!</b>
            </p>
            <hr style="margin:2em 0;">
            <blockquote style="font-size:1.1em; color:#555;">
                “The beautiful thing about learning is that nobody can take it away from you.”<br>
                <span style="font-size:0.9em;">– B.B. King</span>
            </blockquote>
        </div>
        """,
        unsafe_allow_html=True
    )

# Sidebar navigation
st.sidebar.title("EduTrack Menu")
page = st.sidebar.radio(
    "Choose a page:",
    ("Home", "IQ Test", "Mental Energy Check", "Study Habits", "Motivation Booster", "Analysis")
)

if page == "Home":
    home()
elif page == "IQ Test":
    iq_test()
elif page == "Mental Energy Check":
    mental_energy()
elif page == "Study Habits":
    study_habits()
elif page == "Motivation Booster":
    motivation_booster()
elif page == "Analysis":
    analysis()