import streamlit as st

# Set page config
st.set_page_config(page_title="Computer Guesses Your Number", layout="centered")

# Title and instructions
st.title("🎯 Computer Guesses Your Number!")
st.markdown("Think of a number between 1 and 100. The computer will try to guess it. Click the buttons to guide it!")

# Initialize session state variables
if "low" not in st.session_state:
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.attempts = 0
    st.session_state.guess = None
    st.session_state.finished = False

# Function to make a guess
def make_guess():
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
    st.session_state.attempts += 1

# First guess if not already done
if st.session_state.guess is None and not st.session_state.finished:
    make_guess()

# Game loop
if not st.session_state.finished:
    st.subheader(f"🤖 Is your number **{st.session_state.guess}**?")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🔼 Too Low"):
            st.session_state.low = st.session_state.guess + 1
            make_guess()

    with col2:
        if st.button("🔽 Too High"):
            st.session_state.high = st.session_state.guess - 1
            make_guess()

    with col3:
        if st.button("✅ Correct!"):
            st.success(f"🎉 The computer guessed your number in {st.session_state.attempts} tries!")
            st.session_state.finished = True

else:
    st.balloons()
    if st.button("🔁 Play Again"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
