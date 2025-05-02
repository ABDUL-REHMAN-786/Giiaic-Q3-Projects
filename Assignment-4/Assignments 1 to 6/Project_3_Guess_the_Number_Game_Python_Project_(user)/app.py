import streamlit as st
import random
import time

# Set up the game state and variables
def get_game_state():
    if "number" not in st.session_state:
        st.session_state["number"] = random.randint(1, 100)  # Random number to guess
        st.session_state["attempts"] = 0  # Number of attempts made
        st.session_state["start_time"] = time.time()  # Track start time
        st.session_state["difficulty"] = "Medium"  # Default difficulty
        st.session_state["player_guess"] = None
        st.session_state["is_ai"] = False  # Whether it's AI mode
    return st.session_state

# AI guessing function
def ai_guess():
    if "ai_range" not in st.session_state:
        st.session_state["ai_range"] = [1, 100]
    
    low, high = st.session_state["ai_range"]
    guess = random.randint(low, high)
    st.session_state["ai_guess"] = guess
    return guess

# Leaderboard system (simplified with session state)
def update_leaderboard(time_taken, attempts):
    if "leaderboard" not in st.session_state:
        st.session_state["leaderboard"] = []
    
    # Add the current player's score to the leaderboard
    st.session_state["leaderboard"].append({"time": time_taken, "attempts": attempts})
    # Sort leaderboard by time (faster is better)
    st.session_state["leaderboard"] = sorted(st.session_state["leaderboard"], key=lambda x: x["time"])

# Game logic
def guess_the_number():
    st.title("Guess the Number Game")

    game_state = get_game_state()

    # Select Difficulty
    difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])
    if difficulty != game_state["difficulty"]:
        game_state["difficulty"] = difficulty
        game_state["number"] = random.randint(1, 100)
        game_state["attempts"] = 0

    # Player's Guess
    player_guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)
    if player_guess:
        game_state["player_guess"] = player_guess
        game_state["attempts"] += 1

    # Start the Game
    if st.button("Start Game"):
        if game_state["player_guess"] == game_state["number"]:
            end_time = time.time() - game_state["start_time"]
            st.success(f"Correct! It took you {game_state['attempts']} attempts and {end_time:.2f} seconds.")
            update_leaderboard(end_time, game_state["attempts"])
            st.session_state["number"] = random.randint(1, 100)  # New number for the next round
            st.session_state["attempts"] = 0  # Reset attempts
            st.session_state["start_time"] = time.time()  # Reset start time

        elif game_state["player_guess"] < game_state["number"]:
            st.warning("Too low! Try again.")
        elif game_state["player_guess"] > game_state["number"]:
            st.warning("Too high! Try again.")

    # AI Mode Option
    is_ai_mode = st.checkbox("Enable AI Opponent")
    if is_ai_mode != game_state["is_ai"]:
        game_state["is_ai"] = is_ai_mode
        game_state["number"] = random.randint(1, 100)
        game_state["attempts"] = 0

    if game_state["is_ai"]:
        ai_guess_value = ai_guess()
        st.write(f"AI is guessing: {ai_guess_value}")
        if ai_guess_value == game_state["number"]:
            st.success(f"AI guessed the number {game_state['number']} correctly!")
            end_time = time.time() - game_state["start_time"]
            update_leaderboard(end_time, game_state["attempts"])
            st.session_state["number"] = random.randint(1, 100)  # New number for the next round
            st.session_state["attempts"] = 0  # Reset attempts
            st.session_state["start_time"] = time.time()  # Reset start time

    # Display leaderboard
    st.subheader("Leaderboard")
    leaderboard = st.session_state.get("leaderboard", [])
    if leaderboard:
        for idx, entry in enumerate(leaderboard[:5], start=1):
            st.write(f"{idx}. {entry['time']:.2f}s, {entry['attempts']} attempts")
    else:
        st.write("No leaderboard data available yet.")

if __name__ == "__main__":
    guess_the_number()
