import streamlit as st

def study_habits():
    st.header("📚 Let's talk about your real study habits.")

    with st.form("study_habits_form"):
        focus_hours = st.slider("🕰 On a good day, how many hours do you study with full focus?", 0.0, 6.0, 0.0, 0.5)
        distracted = st.radio("📱 Do you often get distracted by your phone or social media while studying?", ["yes", "no"])
        social_media_time = 0.0
        if distracted == "yes":
            social_media_time = st.slider("⏳ Roughly how long do you use social media during study hours? (in hours)", 0.0, 6.0, 0.0, 0.5)
        submitted = st.form_submit_button("Check My Study Efficiency")

    if submitted:
        # Scoring logic
        if focus_hours >= 4 and social_media_time < 1:
            efficiency = 90
        elif focus_hours >= 2:
            efficiency = 70
        elif focus_hours >= 1:
            efficiency = 50
        else:
            efficiency = 30

        if social_media_time > 2:
            st.write("📉 Oops, social media seems to be eating a lot of your time.")
            efficiency -= 10

        efficiency = max(efficiency, 0)
        st.subheader(f"📈 Your Study Efficiency: {efficiency}%")
        st.session_state["study_score"] = efficiency  # efficiency should be out of 100
        st.session_state["study_habits_answers"] = {
            "focus_hours": focus_hours,
            "distracted": distracted,
            "social_media_time": social_media_time   
        }
        return efficiency

    # If not submitted, return the last score from session state (if any)
    return st.session_state.get("study_score", 0)

if __name__ == "__main__":
    study_habits()
    # This is for testing purposes, you can remove it when integrating with the main app
    # result = study_habits()
    # print(f"Study Habits Score: {result}%")