import streamlit as st
import time

st.set_page_config(page_title="Countdown Timer", layout="centered")

st.title("⏳ Countdown Timer")

# Input: Minutes and Seconds
minutes = st.number_input("Minutes", min_value=0, max_value=60, value=0, step=1)
seconds = st.number_input("Seconds", min_value=0, max_value=59, value=30, step=1)

total_time = int(minutes * 60 + seconds)

# Start Button
if st.button("Start Countdown"):
    if total_time == 0:
        st.warning("⛔ Please set a valid countdown time.")
    else:
        placeholder = st.empty()
        for i in range(total_time, -1, -1):
            mins, secs = divmod(i, 60)
            timer_display = f"{mins:02d}:{secs:02d}"
            placeholder.markdown(f"## ⏱ Time Left: {timer_display}")
            time.sleep(1)
        st.success("🎉 Time's up!")

