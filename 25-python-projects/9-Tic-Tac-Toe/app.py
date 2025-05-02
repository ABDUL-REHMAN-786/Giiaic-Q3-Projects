import streamlit as st

st.set_page_config(page_title="Tic-Tac-Toe", page_icon="❌⭕", layout="centered")
st.title("🎮 Tic-Tac-Toe")
st.markdown("Play against a friend. X goes first!")

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.scores = {"X": 0, "O": 0, "Draws": 0}

# Winning combinations
wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def check_winner():
    board = st.session_state.board
    for i, j, k in wins:
        if board[i] == board[j] == board[k] and board[i] != "":
            return board[i]
    if "" not in board:
        return "Draw"
    return None

def handle_click(index):
    if st.session_state.board[index] == "" and not st.session_state.winner:
        st.session_state.board[index] = st.session_state.current_player
        st.session_state.winner = check_winner()

        if st.session_state.winner:
            if st.session_state.winner in ["X", "O"]:
                st.session_state.scores[st.session_state.winner] += 1
            else:
                st.session_state.scores["Draws"] += 1
        else:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# Grid layout
cols = st.columns(3)
for i in range(9):
    with cols[i % 3]:
        st.button(
            st.session_state.board[i] or " ",
            key=i,
            on_click=handle_click,
            args=(i,),
            disabled=bool(st.session_state.board[i] or st.session_state.winner),
            use_container_width=True
        )

# Display result
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.info("🤝 It's a draw!")
    else:
        st.success(f"🎉 Player {st.session_state.winner} wins!")

# Scoreboard
st.markdown("---")
st.subheader("📊 Scoreboard")
st.markdown(f"- Player ❌ X: **{st.session_state.scores['X']}**")
st.markdown(f"- Player ⭕ O: **{st.session_state.scores['O']}**")
st.markdown(f"- 🤝 Draws: **{st.session_state.scores['Draws']}**")

# Reset button
if st.button("🔄 New Game"):
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
