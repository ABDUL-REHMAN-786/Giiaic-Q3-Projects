import streamlit as st
import copy

st.set_page_config(page_title="Tic-Tac-Toe AI", page_icon="🤖", layout="centered")
st.title("🤖 Tic-Tac-Toe vs AI")

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.human = "X"
    st.session_state.ai = "O"
    st.session_state.turn = "X"
    st.session_state.winner = None

# Winning combinations
wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)]

def check_winner(board):
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == st.session_state.ai:
        return 1
    elif winner == st.session_state.human:
        return -1
    elif winner == "Draw":
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == "":
                board[i] = st.session_state.ai
                score = minimax(board, False)
                board[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == "":
                board[i] = st.session_state.human
                score = minimax(board, True)
                board[i] = ""
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -float("inf")
    move = -1
    for i in range(9):
        if st.session_state.board[i] == "":
            st.session_state.board[i] = st.session_state.ai
            score = minimax(st.session_state.board, False)
            st.session_state.board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    return move

def make_move(index):
    if st.session_state.board[index] == "" and not st.session_state.winner:
        st.session_state.board[index] = st.session_state.human
        st.session_state.winner = check_winner(st.session_state.board)
        st.session_state.turn = st.session_state.ai

        if not st.session_state.winner:
            ai_index = best_move()
            if ai_index != -1:
                st.session_state.board[ai_index] = st.session_state.ai
            st.session_state.winner = check_winner(st.session_state.board)
            st.session_state.turn = st.session_state.human

# Display grid
cols = st.columns(3)
for i in range(9):
    with cols[i % 3]:
        st.button(
            st.session_state.board[i] or " ",
            key=i,
            on_click=make_move,
            args=(i,),
            disabled=bool(st.session_state.board[i] or st.session_state.winner),
            use_container_width=True
        )

# Show result
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.info("🤝 It's a draw!")
    else:
        msg = "🎉 You win!" if st.session_state.winner == st.session_state.human else "💻 AI wins!"
        st.success(msg)

# Reset button
if st.button("🔄 Play Again"):
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None
