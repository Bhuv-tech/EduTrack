import streamlit as st
from iqtest import iq_test
from study_habits import study_habits
from mental_energy_check import mental_energy
from motivation import motivation_booster
from analysis import analysis

def run_all():
    st.write("🧠 EduTrack - Student Wellness Analyzer\n")

    iq_result = iq_test() or (0, "")
    study_result = study_habits() or 0
    sleep_result = mental_energy() or 0
    motivation_result = motivation_booster() or (0, "")

    iq_score = iq_result[0] if isinstance(iq_result, tuple) else iq_result
    study_score = study_result[0] if isinstance(study_result, tuple) else study_result
    sleep_score = sleep_result[0] if isinstance(sleep_result, tuple) else sleep_result
    motivation_score = motivation_result[0] if isinstance(motivation_result, tuple) else motivation_result

    final_score = (iq_score + study_score + sleep_score + motivation_score) / 4

    st.subheader(f"🧠 Final Wellness Score: {final_score:.2f}")
    st.write("Here's how you did:")
    if final_score >= 80:
        st.success("🌟 You're doing great! Stay consistent.")
    elif final_score >= 60:
        st.info("💪 Good job! You can push a little more.")
    else:
        st.warning("🌱 Keep going. You're growing, and that matters.")
    
    analysis()

    return iq_score, study_score, sleep_score, motivation_score, final_score