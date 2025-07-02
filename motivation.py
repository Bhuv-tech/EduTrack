import streamlit as st
import random

# Default quotes in case quotes.txt is missing
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
        return default_quotes  # fallback to default list if file not found

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

        # Store score in session state for analysis/results
        st.session_state["motivation_score"] = score * 10  # out of 100
        st.session_state["motivation_answer"] = feeling

        return score * 10, quote  # Return score out of 100 for consistency

    # If not submitted, return the last score from session state (if any)
    score = st.session_state.get("motivation_score", 0)
    quote = ""
    return score, quote

if __name__ == "__main__":
    motivation_booster()