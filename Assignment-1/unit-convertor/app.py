import streamlit as st
import pint

# Configure Streamlit
st.set_page_config(page_title="Advanced Unit Converter", page_icon="🔄", layout="centered")

# Initialize Pint for unit conversions
ureg = pint.UnitRegistry()

# Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Custom CSS for styling
st.markdown("""
    <style>
    .stButton>button {
        display: block;
        margin: 0 auto;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .card {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background-color: white;
        margin-bottom: 20px;
        color: #2C3E50;
    }
    .header {
        text-align: center;
        color: #2C3E50;
    }
    .footer {
        text-align: center;
        color: #7f8c8d;
        margin-top: 30px;
    }
    body {
        background-color: #f0f2f6;
        color: #2C3E50;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class="header">
        <h1 style='color: green;'>🔄 Advanced Unit Converter</h1>
        <h4 style='color: red;'>Convert between 1000+ units across multiple categories</h4>
        <hr style='border: 1px solid #ddd;'>
    </div>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🔄 Unit Converter App")
st.sidebar.markdown("### Select a category:")
page = st.sidebar.radio("Go to", [
    "🏠 Home",
    "📏 Length & Distance",
    "⚖️ Weight & Mass",
    "🌡 Temperature",
    "🛢 Volume",
    "🚀 Speed",
    "📐 Area",
    "🎛 Power",
    "💡 Energy",
    "⏳ Time",
    "📦 Density"
])

# Homepage
if page == "🏠 Home":
    st.markdown("""
        <div class="card">
            <div style='text-align: center;'>
                <h2>Welcome to the Ultimate Unit Converter</h2>
                <p style='color: #2C3E50;'>A powerful, responsive, and professional unit converter supporting 1000+ units.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Features List
    st.markdown("""
        <div class="card">
            <h3>✅ Features:</h3>
            <ul>
                <li>Supports <strong>1000+ units</strong> across multiple categories</li>
                <li>Auto-Detect Units</li>
                <li>Responsive & Mobile-Friendly UI</li>
                <li>Copy Results & Conversion History</li>
                <li>Open Source & Free</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
else:


    unit_categories = {
    "📏 Length & Distance": ["meter", "kilometer", "mile", "inch", "foot", "yard", "centimeter", "millimeter", "micrometer", "nanometer"],
    "⚖️ Weight & Mass": ["gram", "kilogram", "pound", "ounce", "ton", "stone", "carat"],
    "🌡 Temperature": ["celsius", "fahrenheit", "kelvin"],
    "🛢 Volume": ["liter", "milliliter", "gallon", "cup", "fluid_ounce_us", "pint", "quart"],
    "🚀 Speed": ["meter/second", "kilometer/hour", "mile/hour", "knot", "foot/second"],
    "📐 Area": ["square meter", "square kilometer", "square mile", "square foot", "acre", "hectare"],
    "🎛 Power": ["watt", "kilowatt", "horsepower", "megawatt"],
    "💡 Energy": ["joule", "calorie", "electron volt", "kilojoule", "megajoule", "watt hour", "kilowatt hour"],
    "⏳ Time": ["second", "minute", "hour", "day", "week", "month", "year"],
    "📦 Density": ["kilogram/meter**3", "gram/milliliter", "pound/gallon", "ounce/inch**3"]
}

    st.markdown(f"<h2 style='text-align: center; color: #2C3E50;'>{page}</h2>", unsafe_allow_html=True)
    
    # Select Units
    units = unit_categories[page]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("Convert from:", units, key="from_unit")
    with col2:
        to_unit = st.selectbox("Convert to:", units, key="to_unit")
    
    # Input Value
    value = st.number_input("Enter Value:", format="%.4f", min_value=0.0, key="value")
    
    # Perform Conversion
    if st.button("Convert", key="convert_button"):
        try:
            # Get unit dimensionality
            from_dim = ureg(from_unit).dimensionality
            to_dim = ureg(to_unit).dimensionality

            # Check if units are compatible
            if from_dim != to_dim:
                st.error(f"⚠ Units are incompatible: Cannot convert {from_unit} to {to_unit}.")
            else:
                # Handle temperature separately due to offset units
                if from_unit in ["celsius", "fahrenheit", "kelvin"] or to_unit in ["celsius", "fahrenheit", "kelvin"]:
                    temp_quantity = ureg.Quantity(value, getattr(ureg, from_unit))
                    result = temp_quantity.to(getattr(ureg, to_unit))
                else:
                    result = (value * ureg(from_unit)).to(ureg(to_unit))

                st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

                # Add to history
                st.session_state.history.append({
                    "from": f"{value} {from_unit}",
                    "to": f"{result:.4f} {to_unit}",
                    "category": page
                })

        except pint.errors.UndefinedUnitError:
            st.error("⚠ Invalid unit selected. Please check your inputs.")
        except Exception as e:
            st.error(f"⚠ An unexpected error occurred: {str(e)}")

    # Display Conversion History
    if st.session_state.history:
        st.markdown("### 📜 Conversion History")
        for idx, entry in enumerate(st.session_state.history, start=1):
            st.markdown(f"""
                <div class="card">
                    <p><strong>{idx}.</strong> **{entry['from']}** → **{entry['to']}** (Category: {entry['category']})</p>
                </div>
            """, unsafe_allow_html=True)

        # Clear History Button
        if st.button("Clear History", key="clear_history_button"):
            st.session_state.history = []
            st.rerun()

# --- FOOTER ---
st.markdown("""
    <hr style='border: 1px solid #ddd;'>
    <div class="footer">
        <p>Developed by <strong>Abdul Rehman</strong> | 📌 <i>Built with Streamlit & Pint</i></p>
    </div>
""", unsafe_allow_html=True)
# ############################################################################################################
