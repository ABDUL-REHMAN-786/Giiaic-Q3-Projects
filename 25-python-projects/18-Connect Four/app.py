import streamlit as st
import numpy as np

# Config
st.set_page_config(page_title="Connect Four", layout="centered")
st.title("🎮 Connect Four Game")

# Constants
ROWS = 6
COLS = 7
EMPTY = 0
PLAYER_1 = 1  # Red
PLAYER_2 = 2  # Yellow

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = np.zeros((ROWS, COLS), int)
    st.session_state.turn = PLAYER_1  # Player 1 starts
    st.session_state.winner = None
    st.session_state.game_over = False

# Check if there is a winner
def check_winner(board, player):
    # Horizontal, vertical, diagonal checks
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r, c + i] == player for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r + i, c] == player for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i, c + i] == player for i in range(4)):
                return True
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i, c + i] == player for i in range(4)):
                return True
    return False

# Drop the disc into the selected column
def drop_disc(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row, col] == EMPTY:
            board[row, col] = player
            return row, col
    return None  # If the column is full, return None

# Display the game board
def display_board(board):
    st.write("### Current Game Board:")
    board_img = np.full((ROWS * 100, COLS * 100, 3), 255, dtype=np.uint8)  # White background
    for r in range(ROWS):
        for c in range(COLS):
            color = (255, 0, 0) if board[r, c] == PLAYER_1 else (255, 255, 0) if board[r, c] == PLAYER_2 else (200, 200, 200)
            board_img[r * 100: (r + 1) * 100, c * 100: (c + 1) * 100] = color

    st.image(board_img)

# Game logic
def game_logic(col):
    if st.session_state.game_over:
        return

    player = st.session_state.turn
    result = drop_disc(st.session_state.board, col, player)

    if result is None:  # Column is full
        st.warning(f"Column {col + 1} is full. Try another column.")
        return

    row, col = result

    if check_winner(st.session_state.board, player):
        st.session_state.winner = player
        st.session_state.game_over = True
        st.write(f"🎉 **Player {player} wins!** 🎉")
    else:
        # Switch turn
        st.session_state.turn = PLAYER_2 if player == PLAYER_1 else PLAYER_1

# User interface
if st.session_state.game_over:
    if st.button("🔁 Restart Game"):
        for key in ["board", "turn", "winner", "game_over"]:
            del st.session_state[key]
        st.rerun()  # Use st.rerun() instead of st.experimental_rerun()
else:
    # Display game board and column buttons
    display_board(st.session_state.board)
    st.write(f"**Player {st.session_state.turn}'s Turn**")

    columns = st.columns(COLS)
    for col_num in range(COLS):
        with columns[col_num]:
            if st.button(f"Drop in Column {col_num + 1}"):
                game_logic(col_num)
