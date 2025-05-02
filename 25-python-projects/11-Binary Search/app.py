import streamlit as st
import time

st.set_page_config(page_title="Binary Search Visualizer", layout="centered")
st.title("🔍 Binary Search Visualizer")

# Initialize state
if "steps" not in st.session_state:
    st.session_state.steps = []
    st.session_state.found = None
    st.session_state.index = -1

def binary_search_visual(arr, target):
    low, high = 0, len(arr) - 1
    st.session_state.steps = []

    while low <= high:
        mid = (low + high) // 2
        st.session_state.steps.append((low, mid, high))
        if arr[mid] == target:
            st.session_state.found = True
            st.session_state.index = mid
            return
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    st.session_state.found = False
    st.session_state.index = -1

# User input
with st.form("input_form"):
    arr_input = st.text_input("Enter a sorted list of integers (comma-separated)", "1,3,5,7,9,11,13")
    target_input = st.text_input("Enter the number to search for", "7")
    submitted = st.form_submit_button("Search")

if submitted:
    try:
        arr = list(map(int, arr_input.split(",")))
        target = int(target_input)
        st.session_state.found = None
        st.session_state.steps = []
        binary_search_visual(arr, target)
    except ValueError:
        st.error("Please enter valid integers.")

# Show results
if st.session_state.steps:
    st.subheader("🔄 Search Progress")
    arr = list(map(int, arr_input.split(",")))
    for i, (low, mid, high) in enumerate(st.session_state.steps):
        cols = st.columns(len(arr))
        for idx in range(len(arr)):
            bg_color = "white"
            if idx == mid:
                bg_color = "#FFD700"  # Yellow for mid
            elif low <= idx <= high:
                bg_color = "#ADD8E6"  # Light blue for active range
            with cols[idx]:
                st.markdown(
                    f"<div style='text-align:center; padding:8px; background-color:{bg_color}; border-radius:8px;'>{arr[idx]}</div>",
                    unsafe_allow_html=True
                )
        st.caption(f"Step {i+1}: low={low}, mid={mid}, high={high}")
        time.sleep(0.3)

    # Show result
    if st.session_state.found:
        st.success(f"✅ Found {target} at index {st.session_state.index}.")
    else:
        st.error(f"❌ {target} not found in the list.")

# Reset
if st.button("🔄 Reset"):
    st.session_state.steps = []
    st.session_state.found = None
    st.session_state.index = -1
