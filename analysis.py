import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_analysis(iq_score, study_score, sleep_score, motivation_score, iq_level):
    # Calculate overall percentage
    total = iq_score + study_score + sleep_score + motivation_score
    percent = (total / 400) * 100

    st.title("📊 EduTrack Student Performance Analysis")

    st.info(f"🧠 IQ Level: {iq_level}")
    st.success(f"📈 Overall Performance Score: {percent:.2f}%")

    # Prepare DataFrame
    data = {
        "Category": ["IQ Test", "Study Habits", "Mental Energy", "Motivation"],
        "Score": [iq_score, study_score, sleep_score, motivation_score]
    }
    df = pd.DataFrame(data)

    # --- 📊 Bar Chart ---
    st.subheader("📊 Bar Chart")
    fig1, ax1 = plt.subplots()
    sns.barplot(x="Score", y="Category", data=df, palette="Blues_d", ax=ax1)
    ax1.set_xlim(0, 100)
    ax1.set_title("Scores by Category")
    st.pyplot(fig1)

    # --- 🥧 Pie Chart ---
    st.subheader("🥧 Pie Chart")
    fig2, ax2 = plt.subplots()
    ax2.pie(df["Score"], labels=df["Category"], autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
    ax2.axis("equal")
    st.pyplot(fig2)

    # --- 💬 Text-Based Suggestions ---
    st.subheader("💬 Suggestions to Improve")
    if percent >= 80:
        st.success("🌟 Excellent! You’ve maintained a well-balanced academic and personal profile.")
    elif percent >= 60:
        st.info("🚀 You’re on the right track. Try to improve your consistency in 1 or 2 areas.")
    else:
        st.warning("📌 Time to take small steps. Focus more on sleep, habits, or motivation.")

def analysis():
    st.header("📊 Analysis Page")

    # Get scores from session_state, default to 0 if not present
    iq_score = st.session_state.get("iq_score", 0)
    study_score = st.session_state.get("study_score", 0)
    sleep_score = st.session_state.get("sleep_score", 0)
    motivation_score = st.session_state.get("motivation_score", 0)
    iq_level = st.session_state.get("iq_level", "Not attempted")

    if any([iq_score, study_score, sleep_score, motivation_score]):
        show_analysis(iq_score, study_score, sleep_score, motivation_score, iq_level)
    else:
        st.info("No data available yet. Please complete the quizzes to see your analysis.")

if __name__ == "__main__":
    analysis()