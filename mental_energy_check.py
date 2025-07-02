import streamlit as st

def mental_energy():
    st.header("🧠 Mental Energy Level Analyzer")

    with st.form("mental_energy_form"):
        sleep_hours = st.number_input("How many hours do you sleep daily?", min_value=0.0, max_value=24.0, step=0.5)
        learner_type = st.selectbox("Are you a slow, average, or fast learner?", ["slow", "average", "fast"])
        stress_level = st.selectbox("Do you feel stressed/anxious during study?", ["mild", "moderate", "high"])
        phone_night = st.selectbox("Do you use phone or social media at late nights?", ["yes", "no"])
        submitted = st.form_submit_button("Check My Mental Energy")

    if submitted:
        # Sleep score
        if sleep_hours >= 8:
            sleep_score = 3
        elif sleep_hours >= 6:
            sleep_score = 2
        else:
            sleep_score = 1

        # Learning type score
        if learner_type == "fast":
            st.write("🚀 You're a fast learner! Just don't forget to take breaks — even rockets need to refuel.")
            learn_score = 3
        elif learner_type == "average":
            st.write("🧘 You're an average learner — and guess what? Most successful people are too. It's all about consistency, not speed!")
            learn_score = 2
        else:
            st.write("🐢 You're a slow learner — but remember, even turtles win races when they don't give up. You're doing great 💙")
            learn_score = 1

        # Stress level penalty
        if stress_level == "mild":
            st.write("🟢 Mild: You're as calm as a monk sipping green tea on a mountain. Keep it up, Sensei!")
            stress_penalty = 3
        elif stress_level == "moderate":
            st.write("🟡 Moderate: You're walking the fine line between focus and frustration... classic student mode activated!")
            stress_penalty = 2
        else:
            st.write("🔴 High: If throwing the book was an Olympic sport, you'd win gold! Take a deep breath — you're stronger than this.")
            stress_penalty = 1

        # Phone/social media late night penalty
        if phone_night == "yes":
            st.write("So you and your phone are in a full-time relationship huh? Even your sleep said ‘I give up bro 💀’")
            phone_penalty = 1
        else:
            st.write("Respect boss! While we were arguing with alarms, you were already in REM sleep!")
            phone_penalty = 3

        # Total mental energy score out of 100
        score = sleep_score + learn_score + stress_penalty + phone_penalty
        mental_score = (score / 12) * 100
        st.subheader(f"🧠 Your Mental Energy Score: {mental_score:.2f}%")

        # Final interpretation of mental score
        st.write("🧾 Mental Energy Summary:")
        if mental_score >= 80:
            st.success("🌟 Your mental energy is shining bright! Keep nurturing your mind with good habits.")
        elif mental_score >= 60:
            st.info("💪 You're mentally strong — just polish a few habits and you'll feel even better.")
        elif mental_score >= 40:
            st.warning("🌱 You're doing okay, but your mind is asking for more care. Small changes, big impact.")
        else:
            st.error("🫂 Your mental energy seems low. Please be kind to yourself, rest, and take things one step at a time.")

        # Store score and answers in session state
        st.session_state["sleep_score"] = mental_score  # mental_score should be out of 100
        st.session_state["mental_energy_answers"] = {
            "sleep_hours": sleep_hours,
            "learner_type": learner_type,
            "stress_level": stress_level,
            "phone_night": phone_night
        }

        return mental_score
    
    # If not submitted, return the last score from session state (if any)
    return st.session_state.get("sleep_score", 0)

if __name__ == "__main__":
    mental_energy()