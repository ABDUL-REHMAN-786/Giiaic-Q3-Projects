import streamlit as st
import random
import re

st.set_page_config(page_title="Markov Chain Text Composer", layout="centered")
st.title("🧠 Markov Chain Text Composer")
st.markdown("Upload a text file and generate new text based on Markov chains!")

# Function to tokenize and clean the text
def tokenize_text(text):
    text = re.sub(r"[^\w\s]", "", text.lower())
    return text.split()

# Build Markov Chain model
def build_markov_chain(words, n=1):
    markov_chain = {}
    for i in range(len(words) - n):
        key = tuple(words[i:i + n])
        next_word = words[i + n]
        if key not in markov_chain:
            markov_chain[key] = []
        markov_chain[key].append(next_word)
    return markov_chain

# Generate text
def generate_text(chain, length=50, n=1):
    start_key = random.choice(list(chain.keys()))
    result = list(start_key)
    for _ in range(length - n):
        current_state = tuple(result[-n:])
        next_words = chain.get(current_state)
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)
    return " ".join(result)

# Upload section
uploaded_file = st.file_uploader("📄 Upload a plain text (.txt) file", type=["txt"])

if uploaded_file:
    raw_text = uploaded_file.read().decode("utf-8")
    tokens = tokenize_text(raw_text)

    if len(tokens) < 10:
        st.warning("The text file is too short. Please upload a longer file.")
    else:
        st.success("Text uploaded and tokenized successfully!")

        n = st.slider("Markov Chain Order (n-gram)", 1, 3, 1)
        length = st.slider("Number of Words to Generate", 10, 500, 100)

        if st.button("📝 Generate Text"):
            markov_model = build_markov_chain(tokens, n)
            output = generate_text(markov_model, length, n)
            st.subheader("🧾 Generated Text:")
            st.write(output)

            st.download_button(
                "📥 Download Generated Text",
                data=output,
                file_name="generated_text.txt",
                mime="text/plain"
            )
else:
    st.info("Please upload a text file to begin.")

