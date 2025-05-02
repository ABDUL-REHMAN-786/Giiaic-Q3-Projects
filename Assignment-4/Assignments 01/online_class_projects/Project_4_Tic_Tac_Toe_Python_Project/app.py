"""
Tic-Tac-Toe Game using Streamlit
Developed by Abdul Rehman
"""

import streamlit as st
import numpy as np

# Custom CSS for better UI and animations
st.markdown(
    """
    <style>
        body {
            background-color: #f0f0f0;
            text-align: center;
        }
        .stButton > button {
            width: 120px;
            height: 120px;
            font-size: 36px;
            font-weight: bold;
            color: white;
            border-radius: 10px;
            transition: all 0.3s ease-in-out;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: auto;
        }
        .stButton > button:hover {
            transform: scale(1.1);
            box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
        }
        .winner {
            animation: winner-glow 1s infinite alternate;
        }
        @keyframes winner-glow {
            from { background-color: #ffcc00; }
            to { background-color: #ff9900; }
        }
        .center-text {
            text-align: center;
        }
        .center-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize the game board
def initialize_board():
    return np.full((3, 3), "", dtype=object)

# Check for a winner
def check_winner(board):
    for row in board:
        if all(row == row[0]) and row[0] != "":
            return row[0]
    
    for col in board.T:
        if all(col == col[0]) and col[0] != "":
            return col[0]
    
    if all([board[i, i] == board[0, 0] and board[0, 0] != "" for i in range(3)]):
        return board[0, 0]
    
    if all([board[i, 2 - i] == board[0, 2] and board[0, 2] != "" for i in range(3)]):
        return board[0, 2]
    
    if "" not in board:
        return "Draw"
    
    return None

# Streamlit UI
st.markdown("<h1 class='center-text'>✨ Tic-Tac-Toe ✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='center-text' style='color: #ff5733;'>Developed by <b>Abdul Rehman</b></h3>", unsafe_allow_html=True)
st.markdown("<h4 class='center-text'>Player 1: ❌ | Player 2: ⭕</h4>", unsafe_allow_html=True)

# Session state for game state
if "board" not in st.session_state:
    st.session_state.board = initialize_board()
    st.session_state.current_player = "❌"
    st.session_state.winner = None

# Display the board using buttons
st.markdown("<div class='center-container'>", unsafe_allow_html=True)
for i in range(3):
    cols = st.columns([1, 1, 1], gap="small")
    for j in range(3):
        with cols[j]:
            label = st.session_state.board[i, j] if st.session_state.board[i, j] != "" else " "
            btn_class = "winner" if st.session_state.winner and st.session_state.board[i, j] == st.session_state.winner else ""
            if st.button(label, key=f"{i}{j}", disabled=st.session_state.board[i, j] != "" or st.session_state.winner is not None):
                st.session_state.board[i, j] = st.session_state.current_player
                st.session_state.winner = check_winner(st.session_state.board)
                
                if not st.session_state.winner:
                    st.session_state.current_player = "⭕" if st.session_state.current_player == "❌" else "❌"
st.markdown("</div>", unsafe_allow_html=True)

# Show game result
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.markdown("<h2 class='center-text' style='color: #ff5733;'>🎭 It's a Draw!</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 class='center-text' style='color: #28a745;'>🎉 Player {st.session_state.winner} wins!</h2>", unsafe_allow_html=True)

# Reset button in center
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<div class='center-container'>", unsafe_allow_html=True)
if st.button("🔄 Restart Game", key="reset", help="Click to restart the game"):
    st.session_state.board = initialize_board()
    st.session_state.current_player = "❌"
    st.session_state.winner = None
st.markdown("</div>", unsafe_allow_html=True)