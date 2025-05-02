import streamlit as st
import numpy as np

st.set_page_config(page_title="Sudoku Solver", page_icon="🧩", layout="centered")

st.title("🧩 Sudoku Solver")
st.markdown("Enter your Sudoku puzzle below. Leave cells blank for unknowns.")

# --- Initialize session state
if "grid" not in st.session_state:
    st.session_state.grid = [["" for _ in range(9)] for _ in range(9)]

# --- Sudoku Solver Functions
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    startRow, startCol = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[startRow + i][startCol + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# --- Sudoku Input Grid
def sudoku_input():
    grid = []
    for i in range(9):
        cols = st.columns(9)
        row = []
        for j in range(9):
            value = cols[j].text_input("", value=st.session_state.grid[i][j], key=f"cell-{i}-{j}", max_chars=1)
            row.append(value if value.isdigit() and 1 <= int(value) <= 9 else "")
        grid.append(row)
    return grid

input_grid = sudoku_input()

# --- Buttons
col1, col2, col3 = st.columns(3)
solve_btn = col1.button("✅ Solve")
clear_btn = col2.button("🧹 Clear")
sample_btn = col3.button("🎲 Sample Puzzle")

# --- Convert to int matrix
def to_matrix(grid):
    return [[int(cell) if cell != "" else 0 for cell in row] for row in grid]

# --- Main Logic
if solve_btn:
    board = to_matrix(input_grid)
    if solve_sudoku(board):
        st.success("✅ Sudoku Solved!")
        for i in range(9):
            for j in range(9):
                st.session_state.grid[i][j] = str(board[i][j])
    else:
        st.error("❌ No solution found. Please check your input.")

if clear_btn:
    st.session_state.grid = [["" for _ in range(9)] for _ in range(9)]
    st.rerun()

if sample_btn:
    sample = [
        [5, 3, "", "", 7, "", "", "", ""],
        [6, "", "", 1, 9, 5, "", "", ""],
        ["", 9, 8, "", "", "", "", 6, ""],
        [8, "", "", "", 6, "", "", "", 3],
        [4, "", "", 8, "", 3, "", "", 1],
        [7, "", "", "", 2, "", "", "", 6],
        ["", 6, "", "", "", "", 2, 8, ""],
        ["", "", "", 4, 1, 9, "", "", 5],
        ["", "", "", "", 8, "", "", 7, 9],
    ]
    st.session_state.grid = [[str(cell) if cell != "" else "" for cell in row] for row in sample]
    st.rerun()

# --- Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Sudoku Solver © 2025")
