import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image, ImageDraw
import random
import time

# Config
st.set_page_config(page_title="🐍 Snake Game", layout="wide")
st.title("🐍 Streamlit Snake Game")

BOARD_SIZE = 20
CELL_SIZE = 20
SPEED = 1  # seconds per move

# Initialize session state
if "snake" not in st.session_state:
    st.session_state.snake = [(5, 10), (4, 10), (3, 10)]
    st.session_state.food = (random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1))
    st.session_state.direction = "RIGHT"
    st.session_state.score = 0
    st.session_state.game_over = False

# Draw board
def draw_board(snake, food):
    img = Image.new("RGB", (BOARD_SIZE * CELL_SIZE, BOARD_SIZE * CELL_SIZE), "black")
    draw = ImageDraw.Draw(img)
    # Draw food
    fx, fy = food
    draw.rectangle([fx*CELL_SIZE, fy*CELL_SIZE, (fx+1)*CELL_SIZE, (fy+1)*CELL_SIZE], fill="red")
    # Draw snake
    for i, (x, y) in enumerate(snake):
        color = "green" if i == 0 else "lime"
        draw.rectangle([x*CELL_SIZE, y*CELL_SIZE, (x+1)*CELL_SIZE, (y+1)*CELL_SIZE], fill=color)
    return img

# Move snake
def move_snake():
    head_x, head_y = st.session_state.snake[0]
    dx, dy = {
        "UP": (0, -1),
        "DOWN": (0, 1),
        "LEFT": (-1, 0),
        "RIGHT": (1, 0)
    }[st.session_state.direction]

    new_head = (head_x + dx, head_y + dy)

    # Check collision
    if (
        new_head in st.session_state.snake or
        not (0 <= new_head[0] < BOARD_SIZE) or
        not (0 <= new_head[1] < BOARD_SIZE)
    ):
        st.session_state.game_over = True
        return

    st.session_state.snake.insert(0, new_head)

    # Eat food
    if new_head == st.session_state.food:
        st.session_state.score += 1
        while True:
            new_food = (random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1))
            if new_food not in st.session_state.snake:
                break
        st.session_state.food = new_food
    else:
        st.session_state.snake.pop()

# Controls
col1, col2, col3 = st.columns(3)
with col2:
    st.markdown("### Controls")
    up = st.button("⬆️ Up")
with col1:
    left = st.button("⬅️ Left")
with col3:
    right = st.button("➡️ Right")
with col2:
    down = st.button("⬇️ Down")

if up and st.session_state.direction != "DOWN":
    st.session_state.direction = "UP"
elif down and st.session_state.direction != "UP":
    st.session_state.direction = "DOWN"
elif left and st.session_state.direction != "RIGHT":
    st.session_state.direction = "LEFT"
elif right and st.session_state.direction != "LEFT":
    st.session_state.direction = "RIGHT"

# Game Loop
if not st.session_state.game_over:
    move_snake()
    img = draw_board(st.session_state.snake, st.session_state.food)
    st.image(img)
    st.write(f"**Score:** {st.session_state.score}")

    # ✅ Update query params (modern usage)
    st.query_params.update({"score": str(st.session_state.score)})

    time.sleep(SPEED)
    st.rerun()
else:
    st.markdown("## 💀 Game Over!")
    st.write(f"**Final Score:** {st.session_state.score}")
    if st.button("🔁 Restart"):
        for key in ["snake", "food", "direction", "score", "game_over"]:
            del st.session_state[key]
        st.rerun()
