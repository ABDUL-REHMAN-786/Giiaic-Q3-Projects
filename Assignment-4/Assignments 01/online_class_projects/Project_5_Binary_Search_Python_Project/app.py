import streamlit as st
import numpy as np
import time
import plotly.graph_objects as go

# Set Streamlit page config for Dark Mode
st.set_page_config(page_title="Binary Search Visualization", layout="centered")

# Custom CSS for better UI
st.markdown(
    """
    <style>
    body { background-color: #1e1e1e; color: white; }
    .stButton>button { background-color: #ff4b4b; color: white; border-radius: 10px; }
    .stSlider { color: white; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Binary Search Function
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    steps = []

    while left <= right:
        mid = (left + right) // 2
        steps.append((left, mid, right))  # Store search range

        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, steps  # Target not found

# App Title
st.title("🔍 Binary Search Visualization")

# User Input: Custom or Random Array
array_input = st.text_input("Enter sorted numbers separated by commas (or leave empty for random)", "")

if array_input:
    try:
        arr = np.array([int(x.strip()) for x in array_input.split(",")])
        arr.sort()  # Ensure it's sorted
    except ValueError:
        st.error("Invalid input! Please enter numbers only.")
        st.stop()
else:
    size = st.slider("Select array size:", 5, 20, 10)
    arr = np.sort(np.random.randint(1, 100, size))

st.write("🔢 **Generated Sorted Array:**", arr)

# Target Input
target = st.number_input("🎯 Enter number to search:", min_value=1, max_value=100, value=arr[len(arr)//2])

# Search Button
if st.button("🔎 Start Search"):
    index, steps = binary_search(arr, target)

    # Visualization using Plotly
    st.subheader("🔍 Search Progress")
    placeholder = st.empty()

    for i, (left, mid, right) in enumerate(steps):
        fig = go.Figure()

        # Bar chart representation of the array
        bar_colors = ["blue" if left <= x <= right else "gray" for x in range(len(arr))]
        bar_colors[mid] = "red"  # Highlight the mid element

        fig.add_trace(go.Bar(x=list(range(len(arr))), y=arr, marker_color=bar_colors))

        fig.update_layout(
            title=f"Step {i+1}: Checking index {mid}",
            xaxis_title="Index",
            yaxis_title="Value",
            template="plotly_dark",
        )

        placeholder.plotly_chart(fig)
        time.sleep(0.5)  # Animation effect

    # Final result
    if index != -1:
        st.success(f"✅ Element found at index {index}")
    else:
        st.error("❌ Element not found")
