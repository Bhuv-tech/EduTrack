import streamlit as st
from iqtest import iq_test
from study_habits import study_habits
from mental_energy_check import mental_energy
from motivation import motivation_booster

def run_all():
    st.write("🧠 EduTrack - Student Wellness Analyzer\n")

    iq_score = iq_test()
    study_score = study_habits()
    sleep_score = mental_energy()
    motivation_score, _ = motivation_booster()

    # Combine all to calculate final score
    final_score = (iq_score + study_score + sleep_score + (motivation_score * 10)) / 4

    st.write("🎓 Final Wellness Score:", f"{final_score:.2f}%")
    if final_score >= 80:
        st.balloons()
        st.write("🌟 You're doing great! Stay consistent.")
    elif final_score >= 60:
        st.write("💪 Good job! You can push a little more.")
    else:
        st.write("🌱 Keep going. You're growing, and that matters.")

if __name__ == "__main__":
    result = run_all()
    st.write(result)