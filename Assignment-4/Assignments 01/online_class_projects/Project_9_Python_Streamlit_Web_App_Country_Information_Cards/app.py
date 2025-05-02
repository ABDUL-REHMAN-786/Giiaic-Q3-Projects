import streamlit as st
import requests
import pydeck as pdk

# Streamlit Page Config
st.set_page_config(page_title="Country Info Cards", layout="wide")

st.title("🌍 Country Information Cards")

# Cache API Calls
@st.cache_data
def get_country_data():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []

@st.cache_data
def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {}

# Fetch Country Data
countries = get_country_data()
exchange_rates = get_exchange_rates().get("rates", {})

# Sidebar: Search and Filters
st.sidebar.header("🔍 Search & Filters")
search_query = st.sidebar.text_input("Search Country", "")
region_filter = st.sidebar.selectbox("🌎 Select Region", ["All"] + list(set([c.get("region", "Unknown") for c in countries])))

# Filter Logic
filtered_countries = [c for c in countries if search_query.lower() in c['name']['common'].lower()]
if region_filter != "All":
    filtered_countries = [c for c in filtered_countries if c.get("region", "Unknown") == region_filter]

# CSS Styles
st.markdown("""
    <style>
        .country-card {
            border-radius: 15px;
            padding: 15px;
            margin: 10px;
            box-shadow: 4px 4px 20px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s ease-in-out;
            background: linear-gradient(135deg, #e0f7fa, #b2ebf2);
            text-align: center;
            color: #000;
        }
        .country-card:hover {
            transform: scale(1.05);
            background: linear-gradient(135deg, #b2ebf2, #80deea);
        }

        /* Adjust background and text color for dark mode */
        .stApp.dark .country-card {
            background: linear-gradient(135deg, #333333, #444444);
            color: white;
        }
        .stApp.dark .country-card:hover {
            background: linear-gradient(135deg, #555555, #666666);
        }
    </style>
""", unsafe_allow_html=True)

# Display Cards
cols = st.columns(3)
for i, country in enumerate(filtered_countries[:9]):
    with cols[i % 3]:
        currency = list(country["currencies"].keys())[0] if "currencies" in country else "N/A"
        conversion = f"1 {currency} = {exchange_rates.get(currency, 'N/A')} USD" if currency in exchange_rates else "N/A"
        
        st.markdown(f"""
            <div class='country-card'>
                <h3>{country['name']['common']}</h3>
                <img src="{country['flags']['png']}" width="100%">
                <p><b>Region:</b> {country.get("region", "Unknown")}</p>
                <p><b>Capital:</b> {country.get("capital", ["N/A"])[0]}</p>
                <p><b>Population:</b> {country.get("population", "Unknown"):,}</p>
                <p><b>Currency:</b> {currency} ({conversion})</p>
            </div>
        """, unsafe_allow_html=True)

# Country Comparison Mode
compare_mode = st.sidebar.multiselect("Compare Countries", [c['name']['common'] for c in countries])

if compare_mode:
    st.header("📊 Country Comparison")
    compare_countries = [c for c in countries if c["name"]["common"] in compare_mode]
    
    for country in compare_countries:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(country['flags']['png'], width=150)
        with col2:
            st.subheader(country['name']['common'])
            st.write(f"**Region:** {country.get('region', 'Unknown')}")
            st.write(f"**Capital:** {country.get('capital', ['N/A'])[0]}")
            st.write(f"**Population:** {country.get('population', 'Unknown'):,}")
            st.write(f"**Currency:** {list(country['currencies'].keys())[0] if 'currencies' in country else 'N/A'}")

# Map Visualization
st.header("🗺️ Country Locations")
map_data = {
    "lat": [c["latlng"][0] for c in countries if "latlng" in c],
    "lon": [c["latlng"][1] for c in countries if "latlng" in c],
    "name": [c["name"]["common"] for c in countries if "latlng" in c]
}
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(latitude=20, longitude=0, zoom=1),
    layers=[pdk.Layer(
        "ScatterplotLayer",
        data=map_data,
        get_position=["lon", "lat"],
        get_radius=100000,
        get_color=[0, 0, 255, 160],
        pickable=True
    )]
))

# National Anthem Player (If Available)
if len(filtered_countries) == 1:
    country = filtered_countries[0]
    anthem_url = country.get("anthems", {}).get("official", "")

    if anthem_url:
        st.audio(anthem_url, format="audio/mp3")
    else:
        st.write("🎶 No official national anthem found.")

# Footer
st.write("💡 Data provided by [REST Countries API](https://restcountries.com) & [Exchange Rate API](https://exchangerate-api.com)")
st.write("🔗 Developed by [ABDUL REHMAN]")
st.write("📅 Last Updated: October 2025")