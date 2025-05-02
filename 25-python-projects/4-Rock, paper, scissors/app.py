import streamlit as st
import random
import time

st.set_page_config(page_title="Rock Paper Scissors", page_icon="✊", layout="centered")

st.title("🎮 Rock, Paper, Scissors")
st.markdown("Choose your move and see if you can beat the computer!")

# Emoji mapping
emoji_map = {
    "Rock": "✊",
    "Paper": "📄",
    "Scissors": "✂️"
}

# Initialize session state
if "player_score" not in st.session_state:
    st.session_state.player_score = 0
if "ai_score" not in st.session_state:
    st.session_state.ai_score = 0
if "result" not in st.session_state:
    st.session_state.result = ""
if "player_move" not in st.session_state:
    st.session_state.player_move = ""
if "ai_move" not in st.session_state:
    st.session_state.ai_move = ""

# Game logic
def get_ai_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(player, ai):
    if player == ai:
        return "It's a draw! 🤝"
    elif (
        (player == "Rock" and ai == "Scissors") or
        (player == "Paper" and ai == "Rock") or
        (player == "Scissors" and ai == "Paper")
    ):
        st.session_state.player_score += 1
        return "You win! 🎉"
    else:
        st.session_state.ai_score += 1
        return "Computer wins! 💻"

# Move buttons
st.subheader("Your Move:")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("✊ Rock"):
        st.session_state.player_move = "Rock"
with col2:
    if st.button("📄 Paper"):
        st.session_state.player_move = "Paper"
with col3:
    if st.button("✂️ Scissors"):
        st.session_state.player_move = "Scissors"

# Game play
if st.session_state.player_move:
    st.session_state.ai_move = get_ai_choice()
    time.sleep(0.5)
    st.session_state.result = determine_winner(
        st.session_state.player_move, st.session_state.ai_move
    )

    st.markdown("---")
    st.subheader("Results")
    st.markdown(f"**You:** {emoji_map[st.session_state.player_move]} {st.session_state.player_move}")
    st.markdown(f"**Computer:** {emoji_map[st.session_state.ai_move]} {st.session_state.ai_move}")
    st.success(st.session_state.result)

    # Scoreboard
    st.markdown("---")
    st.subheader("📊 Scoreboard")
    st.markdown(f"**You:** {st.session_state.player_score}")
    st.markdown(f"**Computer:** {st.session_state.ai_score}")

# Reset button
if st.button("🔄 Reset Game"):
    st.session_state.player_score = 0
    st.session_state.ai_score = 0
    st.session_state.result = ""
    st.session_state.player_move = ""
    st.session_state.ai_move = ""
    st.success("Game reset!")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
