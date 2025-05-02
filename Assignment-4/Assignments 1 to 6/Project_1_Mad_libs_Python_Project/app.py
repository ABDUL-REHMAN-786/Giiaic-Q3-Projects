   
import streamlit as st
import random
import time

# Custom CSS for colorful UI and footer
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
            color: #333;
        }
        .sidebar .sidebar-content {
            background-color: #4CAF50;
            color: white;
        }
        h1, h2, h3 {
            color: #ff6347;  /* Tomato */
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #2f2f2f;
            color: white;
            text-align: center;
            padding: 10px;
        }
        .footer a {
            color: #ff6347;
        }
        .footer a:hover {
            color: #ff4500;
        }
    </style>
    """, unsafe_allow_html=True)

# List of categories with options for users to select
adjectives = ["funny", "excited", "lazy", "brave", "strange", "silly", "beautiful", "brilliant"]
nouns = ["dog", "robot", "city", "banana", "tree", "alien", "car", "pirate"]
verbs = ["jump", "run", "dance", "play", "sing", "swim", "travel", "explore"]
places = ["mountain", "forest", "desert", "ocean", "castle", "cave", "village"]
emotions = ["happy", "angry", "excited", "nervous", "scared", "sad", "confused"]
creatures = ["dragon", "troll", "goblin", "vampire", "werewolf", "fairy", "griffin"]
plural_nouns = ["trees", "bottles", "rocks", "birds", "books", "apples", "dollars"]

# Function for Mad Libs with user input for word selection
def mad_libs_with_user_input():
    st.title("Mad Libs Game (With Word Selection)")

    # Select words from each category
    adjective = st.selectbox("Choose an adjective:", adjectives, key="adjective")
    noun = st.selectbox("Choose a noun:", nouns, key="noun")
    verb = st.selectbox("Choose a verb:", verbs, key="verb")
    adjective2 = st.selectbox("Choose another adjective:", adjectives, key="adjective2")
    noun2 = st.selectbox("Choose another noun:", nouns, key="noun2")
    verb2 = st.selectbox("Choose another verb:", verbs, key="verb2")
    place = st.selectbox("Choose a place:", places, key="place")
    emotion = st.selectbox("Choose an emotion:", emotions, key="emotion")
    creature = st.selectbox("Choose a creature:", creatures, key="creature")
    plural_noun = st.selectbox("Choose a plural noun:", plural_nouns, key="plural_noun")

    # Long story template with placeholders
    story = f"""
    The Great Adventure
    ---------------------
    A young adventurer, full of excitement, set off on a quest to find the {adjective} {noun} hidden deep in the {place}. 
    Along the way, the adventurer met a {adjective2} {noun2} who was {verb} and {emotion}. 
    Together, they faced many challenges, including crossing a {adjective} river full of {noun}s, and navigating a {adjective2} forest filled with {plural_noun}. 
    After a long journey, they finally reached the {noun}, only to discover that it was guarded by a {adjective} {creature}. 
    The adventurer and the creature had an epic battle, and only one would come out victorious.
    """

    st.write(story)

    # Option to save the generated story as a text file
    save_button = st.download_button(
        label="Download your story",
        data=story,
        file_name="mad_libs_story.txt",
        mime="text/plain"
    )

# Function for random Mad Libs with predefined word categories
def mad_libs_with_random_words():
    st.title("Random Mad Libs Game")

    # Randomly select words from the predefined lists
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    adjective2 = random.choice(adjectives)
    noun2 = random.choice(nouns)
    verb2 = random.choice(verbs)
    place = random.choice(places)
    emotion = random.choice(emotions)
    creature = random.choice(creatures)
    plural_noun = random.choice(plural_nouns)

    # Random story template with placeholders filled in
    story = f"""
    The Great Adventure
    ---------------------
    A young adventurer, full of excitement, set off on a quest to find the {adjective} {noun} hidden deep in the {place}. 
    Along the way, the adventurer met a {adjective2} {noun2} who was {verb} and {emotion}. 
    Together, they faced many challenges, including crossing a {adjective} river full of {noun}s, and navigating a {adjective2} forest filled with {plural_noun}. 
    After a long journey, they finally reached the {noun}, only to discover that it was guarded by a {adjective} {creature}. 
    The adventurer and the creature had an epic battle, and only one would come out victorious.
    """

    st.write(story)

    # Option to save the random story as a text file
    save_button = st.download_button(
        label="Download your random story",
        data=story,
        file_name="random_mad_libs_story.txt",
        mime="text/plain"
    )

# Function for handling user profile and preferences
def user_profile():
    st.sidebar.header("User Profile")
    name = st.sidebar.text_input("Enter your name:")
    favorite_template = st.sidebar.selectbox("Pick your favorite Mad Libs template:", ["A Day at the Park", "Magical Adventure", "Wild Journey"])
    
    if st.sidebar.button("Save Profile"):
        st.sidebar.write(f"Profile saved! Welcome back, {name}. Your favorite template is: {favorite_template}")

# Function to add a timer challenge to the Mad Libs game
def timer_challenge():
    st.sidebar.header("Timer Challenge")
    timer = st.sidebar.slider("Set your timer (in seconds):", 10, 60, 30)
    
    st.sidebar.write(f"You have {timer} seconds to complete the Mad Libs game!")
    
    start_button = st.sidebar.button("Start Timer")
    if start_button:
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > timer:
                st.sidebar.write("Time's up! Please submit your Mad Libs answers.")
                break

# Main function to allow the user to choose between manual or random Mad Libs
def choose_story_template():
    st.title("Welcome to Mad Libs Game!")
    
    # Display user profile
    user_profile()

    # Timer challenge
    timer_challenge()

    # Choose story template
    choice = st.radio("Choose your Mad Libs game mode:", 
                      ("Mad Libs with Word Selection (Choose words)", 
                       "Random Mad Libs (Random words from a list)"))

    if choice == "Mad Libs with Word Selection (Choose words)":
        mad_libs_with_user_input()  # Run Mad Libs with user input
    elif choice == "Random Mad Libs (Random words from a list)":
        mad_libs_with_random_words()  # Run random Mad Libs with predefined words

# Footer for developer info
def footer():
    st.markdown("""
        <div class="footer">
            <p>Developed by <a href="https://www.linkedin.com/in/abdul-rehman-xyz">Abdul Rehman</a></p>
        </div>
    """, unsafe_allow_html=True)

# Main execution
if __name__ == "__main__":
    choose_story_template()
    footer()