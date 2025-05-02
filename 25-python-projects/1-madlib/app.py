import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Set page title and icon
st.set_page_config(page_title="Growth Mindset App", page_icon="🌱")

# Header
def header():
    st.markdown(
        """
        <div style="background-color:#8B4513;padding:10px;border-radius:10px;text-align:center;color:white;">
            <h1>🌟 Growth Mindset App 🌟</h1>
            <p>Welcome to your personal growth journey! Explore the features below to build resilience, positivity, and a growth mindset.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Footer
def footer():
    st.markdown(
        """
        <div style="background-color:#8B4513;padding:10px;border-radius:10px;text-align:center;color:white;">
            <p>Developed by <strong>Abdul Rehman</strong></p>
            <p>Connect with me on <a style="color:white;" href="https://www.linkedin.com/in/abdulrehman0786/">LinkedIn</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Home Page
def home():
    st.header("🏠 Home")
    st.markdown(
        """
        <div style="text-align: center; font-size: 24px; font-weight: bold; color: #2E8B57;">
            Welcome to the Growth Mindset App! <br>
            Explore various tools and resources to develop a growth mindset.
        </div>
        """,
        unsafe_allow_html=True
    )
    st.image("mindset.jpeg", use_container_width=True)  # Updated to use_container_width

# Journaling & Reflection
def journaling():
    st.header("📔 Journaling & Reflection")
    st.write("Write your daily reflections and review past entries.")

    # Input for new journal entry
    entry = st.text_area("Write your reflection for today:")
    if st.button("Save Entry"):
        with open("journal_entries.txt", "a", encoding="utf-8") as f:
            f.write(f"{pd.Timestamp.now()},{entry}\n---\n")
        st.success("Entry saved!")

    # Display past entries
    st.subheader("Past Entries")
    try:
        with open("journal_entries.txt", "r", encoding="utf-8") as f:
            st.text(f.read())
    except FileNotFoundError:
        st.write("No entries yet. Start journaling!")

# Mindset Challenges
def mindset_challenges():
    st.header("💪 Mindset Challenges")
    st.write("Complete weekly challenges to build resilience and positivity.")

    challenges = [
        "Try something new today.",
        "Reflect on a recent failure and what you learned.",
        "Write down three things you're grateful for.",
        "Compliment someone today.",
        "Spend 10 minutes meditating.",
    ]

    selected_challenge = st.selectbox("Choose a challenge:", challenges)
    if st.button("Start Challenge"):
        with open("challenges_log.txt", "a", encoding="utf-8") as f:
            f.write(f"{pd.Timestamp.now()},{selected_challenge}\n---\n")
        st.write(f"Your challenge: {selected_challenge}")
        st.write("Good luck! 🚀")

# Visualization Board
def visualization_board():
    st.header("🎨 Visualization Board")
    st.write("Upload images or quotes for motivation.")

    uploaded_file = st.file_uploader("Upload an image or quote:", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Your motivational image", use_container_width=True)  # Updated to use_container_width

# Community Support
def community_support():
    st.header("🤝 Community Support")
    st.write("Join the discussion and share your growth journey.")

    # Simple forum
    message = st.text_area("Share your thoughts:")
    if st.button("Post"):
        with open("community_posts.txt", "a", encoding="utf-8") as f:
            f.write(f"{pd.Timestamp.now()},{message}\n---\n")
        st.success("Posted!")

    # Display posts
    st.subheader("Recent Posts")
    try:
        with open("community_posts.txt", "r", encoding="utf-8") as f:
            st.text(f.read())
    except FileNotFoundError:
        st.write("No posts yet. Be the first to share!")

# Mood Tracker
def mood_tracker():
    st.header("😊 Mood Tracker")
    st.write("Track your emotions over time and gain insights.")

    mood = st.selectbox("How are you feeling today?", ["😊 Happy", "😐 Neutral", "😢 Sad", "😡 Angry", "😌 Calm"])
    if st.button("Log Mood"):
        with open("mood_log.csv", "a", encoding="utf-8") as f:
            f.write(f"{pd.Timestamp.now()},{mood}\n")
        st.success("Mood logged!")

    # Display mood history
    try:
        df = pd.read_csv("mood_log.csv", names=["Date", "Mood"], encoding="utf-8")
        st.subheader("Mood History")
        st.line_chart(df.set_index("Date"))
    except FileNotFoundError:
        st.write("No mood data yet. Start tracking!")

# Gamification
def gamification():
    st.header("🏆 Gamification")
    st.write("Earn badges and rewards for completing tasks.")

    # Example badges
    badges = {
        "Journaling Streak": "📔 Write 7 journal entries in a row.",
        "Challenge Master": "💪 Complete 5 mindset challenges.",
        "Mood Tracker Pro": "😊 Log your mood for 30 days.",
        "Meditation Guru": "🧘 Meditate for 10 days in a row.",
    }

    for badge, description in badges.items():
        st.write(f"{badge}: {description}")

# Meditation & Relaxation
def meditation():
    st.header("🧘 Meditation & Relaxation")
    st.write("Take a moment to relax with guided meditations.")

    if st.button("Start 5-Minute Breathing Exercise"):
        st.write("Breathe in... Breathe out... 🧘‍♀️")
        st.write("Relax and focus on your breath.")

# AI Coach
def ai_coach():
    st.header("🤖 AI Coach")
    st.write("Get personalized recommendations based on your progress.")

    # Example AI suggestions
    suggestions = [
        "Read 'Mindset' by Carol Dweck.",
        "Watch a TED Talk on growth mindset.",
        "Try a new hobby to challenge yourself.",
        "Practice gratitude journaling for a week.",
    ]

    st.write("Your AI Coach suggests:")
    for suggestion in suggestions:
        st.write(f"- {suggestion}")

# Growth Analytics
def growth_analytics():
    st.header("📊 Growth Analytics")
    st.write("Visualize your personal growth journey.")

    # Example data
    data = pd.DataFrame({
        "Date": pd.date_range(start="2023-01-01", periods=30),
        "Progress": np.random.randint(1, 10, size=30),
    })

    st.line_chart(data.set_index("Date"))

# Reminder System
def reminders():
    st.header("⏰ Reminder System")
    st.write("Set reminders for your habits and goals.")

    habit = st.text_input("Enter a habit or goal:")
    time = st.time_input("Set a reminder time:")
    if st.button("Set Reminder"):
        st.success(f"Reminder set for {habit} at {time}!")

# History
def history():
    st.header("📜 History")
    st.write("View your past activities and progress.")

    # Journaling History
    st.subheader("Journaling History")
    try:
        with open("journal_entries.txt", "r", encoding="utf-8") as f:
            st.text(f.read())
    except FileNotFoundError:
        st.write("No journal entries yet.")

    # Mood History
    st.subheader("Mood History")
    try:
        df = pd.read_csv("mood_log.csv", names=["Date", "Mood"], encoding="utf-8")
        st.line_chart(df.set_index("Date"))
    except FileNotFoundError:
        st.write("No mood data yet.")

    # Challenges History
    st.subheader("Challenges History")
    try:
        with open("challenges_log.txt", "r", encoding="utf-8") as f:
            st.text(f.read())
    except FileNotFoundError:
        st.write("No challenges completed yet.")

# Sidebar Navigation
st.sidebar.title("Navigation")
options = [
    "Home", "Journaling & Reflection", "Mindset Challenges", "Visualization Board",
    "Community Support", "Mood Tracker", "Gamification", "Meditation & Relaxation",
    "AI Coach", "Growth Analytics", "Reminder System", "History"
]
choice = st.sidebar.selectbox("Choose a feature:", options)

# Display Header
header()

# Display selected feature
if choice == "Home":
    home()
elif choice == "Journaling & Reflection":
    journaling()
elif choice == "Mindset Challenges":
    mindset_challenges()
elif choice == "Visualization Board":
    visualization_board()
elif choice == "Community Support":
    community_support()
elif choice == "Mood Tracker":
    mood_tracker()
elif choice == "Gamification":
    gamification()
elif choice == "Meditation & Relaxation":
    meditation()
elif choice == "AI Coach":
    ai_coach()
elif choice == "Growth Analytics":
    growth_analytics()
elif choice == "Reminder System":
    reminders()
elif choice == "History":
    history()

# Display Footer
footer()