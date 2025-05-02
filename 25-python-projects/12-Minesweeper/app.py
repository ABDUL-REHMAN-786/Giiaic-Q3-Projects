# import streamlit as st
# import random

# st.set_page_config(page_title="💣 Minesweeper", layout="centered")
# st.title("💣 Minesweeper")

# # Game settings
# ROWS, COLS = 8, 8
# MINES = 10

# # Initialize game state
# def init_game():
#     grid = [["" for _ in range(COLS)] for _ in range(ROWS)]
#     revealed = [[False for _ in range(COLS)] for _ in range(ROWS)]
#     flagged = [[False for _ in range(COLS)] for _ in range(ROWS)]

#     # Place mines randomly
#     mine_positions = set()
#     while len(mine_positions) < MINES:
#         r, c = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
#         mine_positions.add((r, c))

#     for r, c in mine_positions:
#         grid[r][c] = "💣"

#     # Calculate adjacent numbers
#     for r in range(ROWS):
#         for c in range(COLS):
#             if grid[r][c] == "💣":
#                 continue
#             count = 0
#             for dr in [-1, 0, 1]:
#                 for dc in [-1, 0, 1]:
#                     nr, nc = r + dr, c + dc
#                     if 0 <= nr < ROWS and 0 <= nc < COLS:
#                         if grid[nr][nc] == "💣":
#                             count += 1
#             grid[r][c] = count if count > 0 else ""

#     return grid, revealed, flagged, False, False

# # Session state
# if "grid" not in st.session_state:
#     st.session_state.grid, st.session_state.revealed, st.session_state.flagged, st.session_state.game_over, st.session_state.win = init_game()

# # Reveal cells recursively
# def reveal_cell(r, c):
#     if st.session_state.revealed[r][c] or st.session_state.flagged[r][c]:
#         return
#     st.session_state.revealed[r][c] = True
#     if st.session_state.grid[r][c] == "💣":
#         st.session_state.game_over = True
#         return
#     if st.session_state.grid[r][c] == "":
#         for dr in [-1, 0, 1]:
#             for dc in [-1, 0, 1]:
#                 nr, nc = r + dr, c + dc
#                 if 0 <= nr < ROWS and 0 <= nc < COLS:
#                     reveal_cell(nr, nc)

# # Check win condition
# def check_win():
#     for r in range(ROWS):
#         for c in range(COLS):
#             if st.session_state.grid[r][c] != "💣" and not st.session_state.revealed[r][c]:
#                 return False
#     return True

# # Display game board
# for r in range(ROWS):
#     cols = st.columns(COLS)
#     for c in range(COLS):
#         cell_value = ""
#         if st.session_state.revealed[r][c]:
#             cell_value = st.session_state.grid[r][c]
#         elif st.session_state.flagged[r][c]:
#             cell_value = "🚩"
#         else:
#             cell_value = ""

#         # Game over: reveal mines
#         if st.session_state.game_over and st.session_state.grid[r][c] == "💣":
#             cell_value = "💣"

#         if cols[c].button(str(cell_value), key=f"{r}-{c}"):
#             if not st.session_state.revealed[r][c] and not st.session_state.flagged[r][c]:
#                 reveal_cell(r, c)
#                 if not st.session_state.game_over and check_win():
#                     st.session_state.win = True
#                     st.success("🎉 You won the game!")
#                 elif st.session_state.game_over:
#                     st.error("💥 Game Over! You clicked a mine.")

# # Restart game
# if st.button("🔄 Restart Game"):
#     st.session_state.grid, st.session_state.revealed, st.session_state.flagged, st.session_state.game_over, st.session_state.win = init_game()






# import streamlit as st
# import random

# st.set_page_config(page_title="💣 Minesweeper", layout="centered")
# st.title("💣 Minesweeper")

# ROWS, COLS = 8, 8
# MINES = 10

# # Game state initialization
# def init_game():
#     grid = [["" for _ in range(COLS)] for _ in range(ROWS)]
#     revealed = [[False for _ in range(COLS)] for _ in range(ROWS)]
#     flagged = [[False for _ in range(COLS)] for _ in range(ROWS)]

#     # Place mines
#     mine_positions = set()
#     while len(mine_positions) < MINES:
#         r, c = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
#         mine_positions.add((r, c))

#     for r, c in mine_positions:
#         grid[r][c] = "💣"

#     # Fill numbers
#     for r in range(ROWS):
#         for c in range(COLS):
#             if grid[r][c] == "💣":
#                 continue
#             count = sum(1 for dr in [-1, 0, 1] for dc in [-1, 0, 1]
#                         if 0 <= r+dr < ROWS and 0 <= c+dc < COLS and grid[r+dr][c+dc] == "💣")
#             grid[r][c] = count if count > 0 else ""

#     return grid, revealed, flagged, False, False, 0

# # Init session state
# if "grid" not in st.session_state:
#     st.session_state.grid, st.session_state.revealed, st.session_state.flagged, st.session_state.game_over, st.session_state.win, st.session_state.score = init_game()

# # Reveal logic
# def reveal_cell(r, c):
#     if st.session_state.revealed[r][c] or st.session_state.flagged[r][c]:
#         return
#     st.session_state.revealed[r][c] = True
#     st.session_state.score += 1
#     if st.session_state.grid[r][c] == "💣":
#         st.session_state.game_over = True
#         return
#     if st.session_state.grid[r][c] == "":
#         for dr in [-1, 0, 1]:
#             for dc in [-1, 0, 1]:
#                 nr, nc = r + dr, c + dc
#                 if 0 <= nr < ROWS and 0 <= nc < COLS:
#                     reveal_cell(nr, nc)

# # Win checker
# def check_win():
#     for r in range(ROWS):
#         for c in range(COLS):
#             if st.session_state.grid[r][c] != "💣" and not st.session_state.revealed[r][c]:
#                 return False
#     return True

# # Colored numbers
# def get_display(value):
#     color_map = {
#         1: "🔵", 2: "🟢", 3: "🟡", 4: "🟠",
#         5: "🔴", 6: "🟣", 7: "⚫", 8: "⚪"
#     }
#     return color_map.get(value, value)

# # Display board
# for r in range(ROWS):
#     cols = st.columns(COLS)
#     for c in range(COLS):
#         value = ""
#         if st.session_state.revealed[r][c]:
#             val = st.session_state.grid[r][c]
#             value = "💣" if val == "💣" else get_display(val)
#         elif st.session_state.flagged[r][c]:
#             value = "🚩"
#         else:
#             value = ""

#         # Reveal mines after game over
#         if st.session_state.game_over and st.session_state.grid[r][c] == "💣":
#             value = "💣"

#         if cols[c].button(str(value), key=f"{r}-{c}"):
#             if not st.session_state.revealed[r][c] and not st.session_state.flagged[r][c]:
#                 reveal_cell(r, c)
#                 if check_win():
#                     st.session_state.win = True
#                     st.success("🎉 You won!")
#                 elif st.session_state.game_over:
#                     st.error("💥 Boom! You hit a mine!")

# # Display score
# st.markdown(f"### 🧮 Score: `{st.session_state.score}`")
# if st.session_state.win:
#     st.balloons()
# elif st.session_state.game_over:
#     st.warning("Game Over! Try again.")

# # Restart button
# if st.button("🔄 Restart"):
#     st.session_state.grid, st.session_state.revealed, st.session_state.flagged, st.session_state.game_over, st.session_state.win, st.session_state.score = init_game()
#     st.session_state.score = 0
#     st.experimental_rerun()










import streamlit as st
import random
import time

st.set_page_config(page_title="💣 Minesweeper", layout="centered")
st.title("💣 Minesweeper")

ROWS, COLS = 8, 8
MINES = 10

# Initialize game
def init_game():
    grid = [["" for _ in range(COLS)] for _ in range(ROWS)]
    revealed = [[False for _ in range(COLS)] for _ in range(ROWS)]
    flagged = [[False for _ in range(COLS)] for _ in range(ROWS)]

    mine_positions = set()
    while len(mine_positions) < MINES:
        r, c = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
        mine_positions.add((r, c))

    for r, c in mine_positions:
        grid[r][c] = "💣"

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "💣":
                continue
            count = sum(
                1
                for dr in [-1, 0, 1]
                for dc in [-1, 0, 1]
                if 0 <= r + dr < ROWS and 0 <= c + dc < COLS and grid[r + dr][c + dc] == "💣"
            )
            grid[r][c] = count if count > 0 else ""

    return grid, revealed, flagged, False, False, 0

if "grid" not in st.session_state:
    st.session_state.grid, st.session_state.revealed, st.session_state.flagged, st.session_state.game_over, st.session_state.win, st.session_state.score = init_game()

# Reveal logic
def reveal_cell(r, c):
    if st.session_state.revealed[r][c] or st.session_state.flagged[r][c]:
        return
    st.session_state.revealed[r][c] = True
    st.session_state.score += 1
    if st.session_state.grid[r][c] == "💣":
        st.session_state.game_over = True
        return
    if st.session_state.grid[r][c] == "":
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    reveal_cell(nr, nc)

# Check win
def check_win():
    for r in range(ROWS):
        for c in range(COLS):
            if st.session_state.grid[r][c] != "💣" and not st.session_state.revealed[r][c]:
                return False
    return True

def get_display(val):
    color_map = {
        1: "🔵", 2: "🟢", 3: "🟡", 4: "🟠",
        5: "🔴", 6: "🟣", 7: "⚫", 8: "⚪"
    }
    return color_map.get(val, val)

# Draw game grid
for r in range(ROWS):
    cols = st.columns(COLS)
    for c in range(COLS):
        value = ""
        if st.session_state.revealed[r][c]:
            val = st.session_state.grid[r][c]
            value = "💥" if val == "💣" else get_display(val)
        elif st.session_state.flagged[r][c]:
            value = "🚩"
        else:
            value = "⬜"

        # Reveal mines after game over
        if st.session_state.game_over and st.session_state.grid[r][c] == "💣":
            value = "💣"

        if cols[c].button(str(value), key=f"{r}-{c}"):
            if not st.session_state.revealed[r][c] and not st.session_state.flagged[r][c]:
                reveal_cell(r, c)
                if check_win():
                    st.session_state.win = True
                    st.success("🎉 You won the game!")
                    st.balloons()
                elif st.session_state.game_over:
                    st.error("💥 Boom! You hit a mine!")
                    st.snow()

# Score display with effects
st.markdown(f"### 🎯 Current Score: `{st.session_state.score}`")

# Feedback
if st.session_state.win:
    st.success("🏆 You cleared the minefield! Well played!")
elif st.session_state.game_over:
    st.warning("💀 Game Over! Click Restart to try again.")

# Restart
if st.button("🔄 Restart Game"):
    st.session_state.grid, st.session_state.revealed, st.session_state.flagged, st.session_state.game_over, st.session_state.win, st.session_state.score = init_game()
    st.toast("Game reset! Good luck! 🍀", icon="♻️")
