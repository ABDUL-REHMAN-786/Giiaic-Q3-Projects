import streamlit as st
import random

st.set_page_config(page_title="Hangman Game", page_icon="🪢", layout="centered")
st.title("🪢 Hangman Game")
st.markdown("Guess the word one letter at a time!")

# Word Bank
words = {
    "Fruits": ["apple", "banana", "mango", "grapes", "pineapple"],
    "Animals": ["elephant", "giraffe", "kangaroo", "dolphin", "penguin"],
    "Countries": ["canada", "brazil", "germany", "japan", "pakistan"]
}

# Initialize session state
if "word" not in st.session_state:
    st.session_state.category = random.choice(list(words.keys()))
    st.session_state.word = random.choice(words[st.session_state.category]).upper()
    st.session_state.guessed = []
    st.session_state.attempts = 6
    st.session_state.score = 0
    st.session_state.game_over = False

# Display category
st.markdown(f"**Category**: 🏷️ `{st.session_state.category}`")

# Show the current guessed word
def get_display_word():
    return " ".join([letter if letter in st.session_state.guessed else "_" for letter in st.session_state.word])

# Show hangman stages
def get_hangman_art(attempts):
    stages = [
        "💀 |----|\n    |    O\n    |   /|\\\n    |   / \\\n  __|__",
        "😵 |----|\n    |    O\n    |   /|\\\n    |   / \n  __|__",
        "😰 |----|\n    |    O\n    |   /|\\\n    |    \n  __|__",
        "😬 |----|\n    |    O\n    |   /|\n    |    \n  __|__",
        "😐 |----|\n    |    O\n    |    |\n    |    \n  __|__",
        "😕 |----|\n    |    O\n    |     \n    |    \n  __|__",
        "🙂 |----|\n    |     \n    |     \n    |    \n  __|__"
    ]
    return f"```\n{stages[6 - attempts]}\n```"

# Display hangman
st.markdown(get_hangman_art(st.session_state.attempts))

# Show guessed word
st.subheader("📝 Word")
st.markdown(f"**{get_display_word()}**")

# Input for guessing
if not st.session_state.game_over:
    letter = st.text_input("Enter a letter:", max_chars=1).upper()

    if letter and letter not in st.session_state.guessed:
        st.session_state.guessed.append(letter)
        if letter not in st.session_state.word:
            st.session_state.attempts -= 1

    # Check for win or lose
    if all(char in st.session_state.guessed for char in st.session_state.word):
        st.success(f"🎉 You guessed the word: {st.session_state.word}")
        st.session_state.score += 1
        st.session_state.game_over = True
    elif st.session_state.attempts == 0:
        st.error(f"💔 You lost! The word was: {st.session_state.word}")
        st.session_state.game_over = True

# Show guessed letters
st.markdown("**Guessed Letters:**")
st.write(", ".join(st.session_state.guessed))

# Scoreboard
st.markdown("---")
st.subheader("📊 Scoreboard")
st.markdown(f"**Score:** {st.session_state.score}")

# Restart button
if st.button("🔄 New Word" if st.session_state.game_over else "❌ Give Up"):
    st.session_state.category = random.choice(list(words.keys()))
    st.session_state.word = random.choice(words[st.session_state.category]).upper()
    st.session_state.guessed = []
    st.session_state.attempts = 6
    st.session_state.game_over = False
    st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown("DEVELOP BY ❤️ ABDUL-REHMAN")
