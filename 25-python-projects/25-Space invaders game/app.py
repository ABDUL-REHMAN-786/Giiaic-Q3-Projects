import streamlit as st
import random
import time

# Emojis
INVADER = "👾"
PLAYER = "🚀"
BULLET = "🔼"
EMPTY = "⬛"
EXPLOSION = "💥"
HEART = "❤️"

# Grid size
GRID_WIDTH = 10
GRID_HEIGHT = 10

# Init state
if "invaders" not in st.session_state:
    st.session_state.invaders = [(random.randint(0, GRID_WIDTH - 1), 0)]
    st.session_state.player_pos = GRID_WIDTH // 2
    st.session_state.bullets = []
    st.session_state.score = 0
    st.session_state.lives = 3
    st.session_state.explosions = []
    st.session_state.game_over = False

# Handle query params for keyboard input
query = st.query_params
key = query.get("key", "")

# Move player with query param key
if key == "left":
    st.session_state.player_pos = max(0, st.session_state.player_pos - 1)
elif key == "right":
    st.session_state.player_pos = min(GRID_WIDTH - 1, st.session_state.player_pos + 1)
elif key == "fire":
    st.session_state.bullets.append((st.session_state.player_pos, GRID_HEIGHT - 2))

# Reset key param
st.query_params.clear()

# Move invaders down
new_invaders = []
for x, y in st.session_state.invaders:
    if y + 1 < GRID_HEIGHT:
        new_invaders.append((x, y + 1))
    else:
        st.session_state.lives -= 1
        if st.session_state.lives <= 0:
            st.session_state.game_over = True
st.session_state.invaders = new_invaders

# Move bullets up
st.session_state.bullets = [(x, y - 1) for x, y in st.session_state.bullets if y > 0]

# Detect collisions
explosions = []
hit_invaders = []
for b in st.session_state.bullets:
    for inv in st.session_state.invaders:
        if b == inv:
            hit_invaders.append(inv)
            explosions.append(inv)
            st.session_state.score += 10
st.session_state.explosions = explosions
st.session_state.invaders = [i for i in st.session_state.invaders if i not in hit_invaders]
st.session_state.bullets = [b for b in st.session_state.bullets if b not in hit_invaders]

# Random new invader
if random.random() < 0.3 and not st.session_state.game_over:
    st.session_state.invaders.append((random.randint(0, GRID_WIDTH - 1), 0))

# UI Controls (fallback for no keyboard)
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅️ Left"):
        st.session_state.player_pos = max(0, st.session_state.player_pos - 1)
with col2:
    if st.button("🔫 Fire"):
        st.session_state.bullets.append((st.session_state.player_pos, GRID_HEIGHT - 2))
with col3:
    if st.button("➡️ Right"):
        st.session_state.player_pos = min(GRID_WIDTH - 1, st.session_state.player_pos + 1)

# Draw grid
grid = [[EMPTY for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
for x, y in st.session_state.invaders:
    grid[y][x] = INVADER
for x, y in st.session_state.bullets:
    grid[y][x] = BULLET
for x, y in st.session_state.explosions:
    grid[y][x] = EXPLOSION
grid[GRID_HEIGHT - 1][st.session_state.player_pos] = PLAYER

# Display grid
st.markdown("### Space Invaders")
for row in grid:
    st.markdown("".join(row))

# Display stats
hearts = HEART * st.session_state.lives
st.markdown(f"**Score:** {st.session_state.score} &nbsp;&nbsp; **Lives:** {hearts}")

# Game over
if st.session_state.game_over:
    st.error("👾 GAME OVER! All lives lost.")
    if st.button("🔁 Restart"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# Inject JavaScript for real-time keyboard control
st.markdown("""
<script>
document.addEventListener('keydown', function(event) {
    if (event.key === "ArrowLeft") {
        window.location.search = "?key=left";
    } else if (event.key === "ArrowRight") {
        window.location.search = "?key=right";
    } else if (event.key === " ") {
        window.location.search = "?key=fire";
    }
});
</script>
""", unsafe_allow_html=True)
