import streamlit as st
import csv
import os
from datetime import datetime
from edutrack import run_all  # ✅ You already created this!

# ✅ Save the result to CSV
def save_result(name, iq, study, sleep, motivation, final_score):
    file_exists = os.path.isfile("results.csv")
    write_header = not file_exists or os.path.getsize("results.csv") == 0
    with open("results.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(["Timestamp", "Name", "IQ Score", "Study Score", "Sleep Score", "Motivation Score", "Final Score"])
        writer.writerow([datetime.now(), name, iq, study, sleep, motivation, final_score])

# Sidebar input
st.sidebar.title("👤 Student Info")
name = st.sidebar.text_input("Enter your name")

if name:
    # ✅ Run the whole quiz workflow from edutrack.py
    iq, study, sleep, motivation, final_score = run_all()

    # ✅ Save when button is clicked
    if st.button("✅ Submit & Save Result"):
        save_result(name, iq, study, sleep, motivation, final_score)
        st.success(f"Results for {name} saved successfully!")
else:
    st.warning("⚠ Please enter your name in the sidebar to begin.")
# ✅ Display the results
st.subheader("📊 Your Results")