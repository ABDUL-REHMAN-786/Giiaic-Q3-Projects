import streamlit as st
import random
import time

# --------------------------
# Setup
st.set_page_config(page_title="🎯 Guess the Number", layout="centered")
st.title("🎯 Guess the Number Game")
st.markdown("Try to guess the number chosen by the computer!")

# --------------------------
# Session State Init
if "number" not in st.session_state:
    st.session_state.number = 0
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Easy"
if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = []

# --------------------------
# Difficulty
difficulty_levels = {
    "Easy": 10,
    "Medium": 50,
    "Hard": 100
}

with st.sidebar:
    st.subheader("⚙️ Settings")
    difficulty = st.radio("Select Difficulty", list(difficulty_levels.keys()), index=["Easy", "Medium", "Hard"].index(st.session_state.difficulty))
    if difficulty != st.session_state.difficulty:
        st.session_state.difficulty = difficulty
        st.session_state.number = random.randint(1, difficulty_levels[difficulty])
        st.session_state.attempts = 0
        st.session_state.start_time = time.time()
        st.success(f"Difficulty set to {difficulty}. New number selected!")

# --------------------------
# Generate new number if not set
if st.session_state.number == 0:
    st.session_state.number = random.randint(1, difficulty_levels[st.session_state.difficulty])
    st.session_state.start_time = time.time()

# --------------------------
# Guess Input
guess = st.number_input("Enter your guess", min_value=1, max_value=difficulty_levels[st.session_state.difficulty], step=1)
if st.button("🎯 Submit Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.info("📉 Too low! Try again.")
    elif guess > st.session_state.number:
        st.info("📈 Too high! Try again.")
    else:
        elapsed = int(time.time() - st.session_state.start_time)
        score = max(100 - elapsed - st.session_state.attempts * 2, 0)
        st.success(f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts and {elapsed} seconds.")
        st.balloons()

        name = st.text_input("Enter your name for the leaderboard:")
        if st.button("🏆 Submit Score") and name:
            st.session_state.leaderboard.append({
                "name": name,
                "attempts": st.session_state.attempts,
                "time": elapsed,
                "score": score
            })
            # Reset game
            st.session_state.number = random.randint(1, difficulty_levels[st.session_state.difficulty])
            st.session_state.attempts = 0
            st.session_state.start_time = time.time()
            st.success("New number generated. Play again!")

# --------------------------
# Leaderboard
if st.session_state.leaderboard:
    st.subheader("🏅 Leaderboard")
    sorted_board = sorted(st.session_state.leaderboard, key=lambda x: (-x["score"], x["time"]))
    for i, entry in enumerate(sorted_board[:5], 1):
        st.markdown(f"**#{i}** - {entry['name']} | Attempts: {entry['attempts']} | Time: {entry['time']}s | Score: {entry['score']}")

# --------------------------
# Reset button
if st.button("🔄 Reset Game"):
    st.session_state.number = random.randint(1, difficulty_levels[st.session_state.difficulty])
    st.session_state.attempts = 0
    st.session_state.start_time = time.time()
    st.success("Game has been reset!")
