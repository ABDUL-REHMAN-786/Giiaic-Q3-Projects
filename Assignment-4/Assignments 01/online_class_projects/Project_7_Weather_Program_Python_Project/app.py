import streamlit as st
import requests

# OpenWeatherMap API Key (Replace with your own key)
API_KEY = "ea815a44ac089b6f28d755bacec67f30"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    return response.json() if response.status_code == 200 else None

# Streamlit UI
st.title("🌦️ Weather App")
city = st.text_input("Enter City Name", "New York")

if st.button("Get Weather"):
    weather_data = get_weather(city)

    if weather_data:
        st.subheader(f"Weather in {city}")
        temp = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        weather_desc = weather_data["weather"][0]["description"].title()
        icon = weather_data["weather"][0]["icon"]

        st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png", width=100)
        st.write(f"**Temperature:** {temp}°C")
        st.write(f"**Humidity:** {humidity}%")
        st.write(f"**Wind Speed:** {wind_speed} m/s")
        st.write(f"**Condition:** {weather_desc}")
    else:
        st.error("City not found. Please enter a valid city name.")

