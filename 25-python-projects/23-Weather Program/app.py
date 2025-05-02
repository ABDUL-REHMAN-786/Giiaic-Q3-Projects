import streamlit as st
import requests

# OpenWeatherMap API Key
API_KEY = "ea815a44ac089b6f28d755bacec67f30"

# Function to get weather data
def get_weather(city_name: str) -> dict:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Custom Streamlit Styling (CSS)
st.markdown(
    """
    <style>
        .main {
            background-color: #f4f4f4;
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
            border: 2px solid #4CAF50;
            padding: 10px;
            font-size: 18px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 20px;
            transition: 0.3s;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .weather-container {
            text-align: center;
            padding: 20px;
            background-color: white;
            border-radius: 15px;
            box-shadow: 3px 3px 15px rgba(0,0,0,0.1);
            margin-top: 20px;
        }
        .bold-center {
            font-weight: bold;
            text-align: center;
            font-size: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App title with emoji
st.markdown("<h1 style='text-align: center; font-weight: bold;'>🌤️ Weather App</h1>", unsafe_allow_html=True)

# City input with placeholder
city = st.text_input("🌍 **Enter city name**", placeholder="Type a city name...")

if st.button("🔍 Get Weather"):
    weather_data = get_weather(city_name=city)
    
    if weather_data:
        st.markdown(f"<h2 class='bold-center'>Weather in {city}</h2>", unsafe_allow_html=True)

        temp = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"].capitalize()
        icon = weather_data["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"

        # Weather Info in a Container
        st.markdown("<div class='weather-container'>", unsafe_allow_html=True)
        col1, col2 = st.columns([2, 1])
        col1.metric("🌡️ Temperature", f"{temp}°C")
        col1.markdown(f"<p class='bold-center'>{description}</p>", unsafe_allow_html=True)
        col2.image(icon_url, caption=description, width=100)
        st.markdown("</div>", unsafe_allow_html=True)

        # Additional weather details
        with st.expander("📌 **More Weather Details**"):
            st.markdown(f"<p class='bold-center'>🌪️ Wind Speed: {weather_data['wind']['speed']} m/s</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='bold-center'>🌡️ Feels Like: {weather_data['main']['feels_like']}°C</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='bold-center'>💧 Humidity: {weather_data['main']['humidity']}%</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='bold-center'>🔆 Pressure: {weather_data['main']['pressure']} hPa</p>", unsafe_allow_html=True)
    else:
        st.error("🚫 **City not found! Please try again.**")