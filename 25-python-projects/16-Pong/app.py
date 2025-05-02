import streamlit as st
import random
import streamlit.components.v1 as components

# Constants
GAME_WIDTH = 600
GAME_HEIGHT = 400
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 80
BALL_SIZE = 10
BALL_SPEED = 5

# Set up the Streamlit page
st.set_page_config(page_title="Pong Game", layout="centered")
st.title("🏓 Pong Game in Streamlit")

# Instructions
with st.expander("📘 How to Play", expanded=True):
    st.markdown("""
    - Use the **radio buttons** to move your paddle **Up** or **Down**.
    - The **AI paddle** will automatically move.
    - Click **"Next Frame"** to advance the game step-by-step.
    - First to a higher score wins (or play endlessly).
    - Click **"Play Game"** below to start or reset.
    """)

# Play button
if st.button("▶️ Play Game"):
    st.session_state.ball_x = GAME_WIDTH // 2
    st.session_state.ball_y = GAME_HEIGHT // 2
    st.session_state.ball_dx = BALL_SPEED * random.choice([-1, 1])
    st.session_state.ball_dy = BALL_SPEED * random.choice([-1, 1])
    st.session_state.player_y = GAME_HEIGHT // 2 - PADDLE_HEIGHT // 2
    st.session_state.cpu_y = GAME_HEIGHT // 2 - PADDLE_HEIGHT // 2
    st.session_state.player_score = 0
    st.session_state.cpu_score = 0
    st.session_state.game_started = True

# Initialize state if not yet started
if "game_started" not in st.session_state:
    st.session_state.game_started = False

# Game runs only if started
if st.session_state.game_started:
    # Paddle control
    move = st.radio("🎮 Move Your Paddle", ["None", "Up", "Down"], index=0, horizontal=True)
    if move == "Up":
        st.session_state.player_y = max(0, st.session_state.player_y - 20)
    elif move == "Down":
        st.session_state.player_y = min(GAME_HEIGHT - PADDLE_HEIGHT, st.session_state.player_y + 20)

    # CPU Paddle AI
    if st.session_state.cpu_y + PADDLE_HEIGHT // 2 < st.session_state.ball_y:
        st.session_state.cpu_y += 4
    else:
        st.session_state.cpu_y -= 4
    st.session_state.cpu_y = max(0, min(GAME_HEIGHT - PADDLE_HEIGHT, st.session_state.cpu_y))

    # Ball movement
    st.session_state.ball_x += st.session_state.ball_dx
    st.session_state.ball_y += st.session_state.ball_dy

    # Bounce on top/bottom
    if st.session_state.ball_y <= 0 or st.session_state.ball_y >= GAME_HEIGHT - BALL_SIZE:
        st.session_state.ball_dy *= -1

    # Player paddle hit
    if (
        st.session_state.ball_x <= PADDLE_WIDTH and
        st.session_state.player_y <= st.session_state.ball_y <= st.session_state.player_y + PADDLE_HEIGHT
    ):
        st.session_state.ball_dx *= -1

    # CPU paddle hit
    if (
        st.session_state.ball_x >= GAME_WIDTH - PADDLE_WIDTH - BALL_SIZE and
        st.session_state.cpu_y <= st.session_state.ball_y <= st.session_state.cpu_y + PADDLE_HEIGHT
    ):
        st.session_state.ball_dx *= -1

    # Scoring
    if st.session_state.ball_x < 0:
        st.session_state.cpu_score += 1
        st.session_state.ball_x = GAME_WIDTH // 2
        st.session_state.ball_y = GAME_HEIGHT // 2
    elif st.session_state.ball_x > GAME_WIDTH:
        st.session_state.player_score += 1
        st.session_state.ball_x = GAME_WIDTH // 2
        st.session_state.ball_y = GAME_HEIGHT // 2

    # Render SVG
    svg = f"""
    <svg width="{GAME_WIDTH}" height="{GAME_HEIGHT}" style="background:black">
      <circle cx="{st.session_state.ball_x}" cy="{st.session_state.ball_y}" r="{BALL_SIZE}" fill="white" />
      <rect x="0" y="{st.session_state.player_y}" width="{PADDLE_WIDTH}" height="{PADDLE_HEIGHT}" fill="white" />
      <rect x="{GAME_WIDTH - PADDLE_WIDTH}" y="{st.session_state.cpu_y}" width="{PADDLE_WIDTH}" height="{PADDLE_HEIGHT}" fill="white" />
      <text x="{GAME_WIDTH//2 - 50}" y="30" fill="white" font-size="24">{st.session_state.player_score}</text>
      <text x="{GAME_WIDTH//2 + 30}" y="30" fill="white" font-size="24">{st.session_state.cpu_score}</text>
    </svg>
    """
    components.html(svg, height=GAME_HEIGHT + 20)

    # Manual frame update
    st.button("🔄 Next Frame (click repeatedly to animate)")
else:
    st.info("Click **Play Game** above to start.")
