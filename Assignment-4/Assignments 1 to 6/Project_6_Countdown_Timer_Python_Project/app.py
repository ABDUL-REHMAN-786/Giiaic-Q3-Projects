import streamlit as st
import time
from streamlit.components.v1 import html

# Function to display countdown animation
def countdown_timer(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        remaining_time = end_time - time.time()
        mins, secs = divmod(int(remaining_time), 60)
        time_str = f"{mins:02}:{secs:02}"

        # Display countdown in Streamlit
        st.text(time_str)
        
        # HTML for circular countdown with animation (colorful and dynamic)
        html_code = """
        <style>
        @keyframes countdown {
            0% {transform: rotate(0deg);}
            100% {transform: rotate(360deg);}
        }
        .countdown-circle {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            border: 12px solid #ff6347;
            border-top: 12px solid transparent;
            animation: countdown 60s linear infinite;
            margin: 0 auto;
        }
        </style>
        <div class="countdown-circle"></div>
        """
        html(html_code)
        
        # Pause for a second before updating the timer
        time.sleep(1)
    
    # Trigger balloon animation when time is up
    trigger_balloon_animation()

# Function to show balloon animation when time is up
def trigger_balloon_animation():
    html_code = """
    <style>
    @keyframes balloonAnim {
        0% {transform: translateY(0); opacity: 1;}
        25% {transform: translateY(-100px); opacity: 0.8;}
        50% {transform: translateY(-200px); opacity: 0.6;}
        75% {transform: translateY(-300px); opacity: 0.4;}
        100% {transform: translateY(-400px); opacity: 0;}
    }
    .balloon {
        width: 80px;
        height: 120px;
        background-color: #ff6347;
        border-radius: 50%;
        position: absolute;
        bottom: 0;
        animation: balloonAnim 3s ease-out forwards;
    }
    .balloon1 {left: 15%; background-color: #ff6347; animation-delay: 0s;}
    .balloon2 {left: 35%; background-color: #ff1493; animation-delay: 0.5s;}
    .balloon3 {left: 55%; background-color: #7cfc00; animation-delay: 1s;}
    .balloon4 {left: 75%; background-color: #1e90ff; animation-delay: 1.5s;}
    </style>
    <div class="balloon balloon1"></div>
    <div class="balloon balloon2"></div>
    <div class="balloon balloon3"></div>
    <div class="balloon balloon4"></div>
    <div style="text-align:center; font-size: 24px; color: #32cd32; font-weight: bold; margin-top: 20px;">
        🎉 Time's Up! 🎉
    </div>
    """
    html(html_code)

# Streamlit app UI
st.title("Countdown Timer with Fun Balloon Animation 🎈")
st.markdown("""
This app shows a colorful countdown timer with a playful balloon animation when time's up! The timer rotates while counting down, and when it finishes, balloons rise up to celebrate!
""")

# Input for countdown duration (in minutes)
minutes = st.number_input("Enter countdown time in minutes:", min_value=1, value=1, step=1)

# Button to start the countdown
if st.button("Start Countdown"):
    st.write("Timer Started!")
    countdown_timer(minutes * 60)
