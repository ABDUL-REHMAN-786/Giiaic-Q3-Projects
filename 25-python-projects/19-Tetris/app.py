import streamlit as st
import numpy as np
import random
import time

# Config
st.set_page_config(page_title="Tetris Game", layout="centered")
st.title("🎮 Tetris Game")

# Set the background color of the app using inline CSS
st.markdown(
    """
    <style>
        body {
            background-color: #2E2E2E;  /* Dark background color for the app */
        }
        .streamlit-expanderHeader {
            background-color: #444444;  /* Darker header */
        }
    </style>
    """, unsafe_allow_html=True
)

# Constants
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
EMPTY = 0
TILE_SIZE = 30  # Pixels
MOVE_DELAY = 0.5  # Seconds (time between automatic moves)

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = np.zeros((BOARD_HEIGHT, BOARD_WIDTH), dtype=int)
    st.session_state.current_piece = None
    st.session_state.current_pos = None
    st.session_state.game_over = False
    st.session_state.score = 0

# Tetromino shapes and colors (Custom color changes)
SHAPES = [
    [(1, 1, 1, 1)],  # I
    [(1, 1), (1, 1)],  # O
    [(0, 1, 0), (1, 1, 1)],  # T
    [(1, 1, 0), (0, 1, 1)],  # S
    [(0, 1, 1), (1, 1, 0)],  # Z
    [(1, 0, 0), (1, 1, 1)],  # L
    [(0, 0, 1), (1, 1, 1)]   # J
]

# Updated Tetromino colors
SHAPE_COLORS = ["#00FFFF", "#FFFF00", "#800080", "#32CD32", "#FF0000", "#FFA500", "#0000FF"]  # Cyan, Yellow, Purple, Green, Red, Orange, Blue

def get_random_piece():
    idx = random.randint(0, len(SHAPES) - 1)
    return SHAPES[idx], SHAPE_COLORS[idx]

# Check if a piece can be placed at a given position
def is_valid_move(board, piece, position):
    piece_height = len(piece)
    piece_width = len(piece[0])
    x, y = position

    for i in range(piece_height):
        for j in range(piece_width):
            if piece[i][j]:
                if x + i >= BOARD_HEIGHT or y + j < 0 or y + j >= BOARD_WIDTH or board[x + i][y + j]:
                    return False
    return True

# Rotate the piece 90 degrees
def rotate(piece):
    return [list(row) for row in zip(*piece[::-1])]

# Drop the piece on the board
def drop_piece(board, piece, position):
    x, y = position
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j]:
                board[x + i][y + j] = piece[i][j]  # Place the colored block on the board
    return board

# Clear completed lines
def clear_lines(board):
    new_board = [row for row in board if any(val == 0 for val in row)]
    lines_cleared = BOARD_HEIGHT - len(new_board)
    new_board = [[0] * BOARD_WIDTH] * lines_cleared + new_board
    return new_board, lines_cleared

# Display the game board with custom background color
def display_board(board):
    st.write("### Current Game Board:")
    # Set the custom background color for the game board (dark gray)
    board_img = np.full((BOARD_HEIGHT * TILE_SIZE, BOARD_WIDTH * TILE_SIZE, 3), 50, dtype=np.uint8)  # Dark background color
    for r in range(BOARD_HEIGHT):
        for c in range(BOARD_WIDTH):
            if board[r][c]:
                # Set color for blocks based on their value (color assigned when piece is dropped)
                block_color = (255, 255, 255)  # Default to white for now
                # Assign specific color based on piece value
                if board[r][c] == 1:
                    block_color = (0, 255, 255)  # Cyan for I piece
                elif board[r][c] == 2:
                    block_color = (255, 255, 0)  # Yellow for O piece
                elif board[r][c] == 3:
                    block_color = (128, 0, 128)  # Purple for T piece
                elif board[r][c] == 4:
                    block_color = (50, 205, 50)  # Green for S piece
                elif board[r][c] == 5:
                    block_color = (255, 0, 0)  # Red for Z piece
                elif board[r][c] == 6:
                    block_color = (255, 165, 0)  # Orange for L piece
                elif board[r][c] == 7:
                    block_color = (0, 0, 255)  # Blue for J piece

                # Color each block
                board_img[r * TILE_SIZE: (r + 1) * TILE_SIZE, c * TILE_SIZE: (c + 1) * TILE_SIZE] = block_color

    st.image(board_img)

# Game loop and logic
def game_logic():
    if st.session_state.game_over:
        st.write(f"Game Over! Final Score: {st.session_state.score}")
        return

    # Handle piece movement
    piece, color = st.session_state.current_piece
    x, y = st.session_state.current_pos

    # Check if piece can move down
    if not is_valid_move(st.session_state.board, piece, (x + 1, y)):
        # Place the piece and clear lines
        st.session_state.board = drop_piece(st.session_state.board, piece, (x, y))
        st.session_state.board, lines_cleared = clear_lines(st.session_state.board)
        st.session_state.score += lines_cleared * 100
        # Get a new piece
        st.session_state.current_piece = get_random_piece()
        st.session_state.current_pos = [0, BOARD_WIDTH // 2 - 1]
        # Check for game over
        if not is_valid_move(st.session_state.board, st.session_state.current_piece[0], st.session_state.current_pos):
            st.session_state.game_over = True
        return

    # Move piece down
    st.session_state.current_pos[0] += 1

# Keyboard controls
def handle_key_presses():
    if st.session_state.game_over:
        return

    piece, color = st.session_state.current_piece
    x, y = st.session_state.current_pos

    keys = st.session_state.get("keys", [])
    if "ArrowLeft" in keys:
        if is_valid_move(st.session_state.board, piece, (x, y - 1)):
            st.session_state.current_pos[1] -= 1
    if "ArrowRight" in keys:
        if is_valid_move(st.session_state.board, piece, (x, y + 1)):
            st.session_state.current_pos[1] += 1
    if "ArrowDown" in keys:
        if is_valid_move(st.session_state.board, piece, (x + 1, y)):
            st.session_state.current_pos[0] += 1
    if "ArrowUp" in keys:
        rotated_piece = rotate(piece)
        if is_valid_move(st.session_state.board, rotated_piece, (x, y)):
            st.session_state.current_piece = (rotated_piece, color)

# Initialize a new game
if "game_started" not in st.session_state:
    st.session_state.game_started = False
    st.session_state.game_over = False
    st.session_state.current_piece = get_random_piece()
    st.session_state.current_pos = [0, BOARD_WIDTH // 2 - 1]

# Start the game
if not st.session_state.game_started:
    if st.button("Start Game"):
        st.session_state.game_started = True
        st.session_state.game_over = False

if st.session_state.game_started:
    # Handle user input
    handle_key_presses()

    # Perform game logic
    game_logic()

    # Display the board
    display_board(st.session_state.board)

    # Score display
    st.write(f"Score: {st.session_state.score}")

    # Refresh the game every 500ms
    time.sleep(MOVE_DELAY)
    st.rerun()  # Re-run the app to update the game state
