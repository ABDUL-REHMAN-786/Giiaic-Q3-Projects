import streamlit as st
import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a draw!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Initialize session state to keep track of scores
def init_game():
    if "player_score" not in st.session_state:
        st.session_state.player_score = 0
        st.session_state.computer_score = 0

# Function to handle the game logic
def play_game(player_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(player_choice, computer_choice)
    
    if result == "You win!":
        st.session_state.player_score += 1
    elif result == "Computer wins!":
        st.session_state.computer_score += 1

    st.write(f"Computer chose: {computer_choice}")
    st.write(result)

# Streamlit UI
def rock_paper_scissors():
    st.title("Rock, Paper, Scissors Game")

    # Initialize the game state
    init_game()

    # Display current score
    st.subheader("Current Score")
    st.write(f"Player: {st.session_state.player_score}")
    st.write(f"Computer: {st.session_state.computer_score}")

    # User makes a choice
    st.subheader("Choose your move")
    choices = ["Rock", "Paper", "Scissors"]
    player_choice = st.radio("Choose", choices)

    if player_choice:
        # Play the game when user selects a move
        if st.button("Play"):
            play_game(player_choice)

    # Option to restart the game
    if st.button("Restart Game"):
        st.session_state.player_score = 0
        st.session_state.computer_score = 0
        st.experimental_rerun()

if __name__ == "__main__":
    rock_paper_scissors()
