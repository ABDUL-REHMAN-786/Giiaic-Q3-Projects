# import streamlit as st
# import qrcode
# import numpy as np
# from PIL import Image
# import cv2
# import io

# # Set page configuration
# st.set_page_config(page_title="QR Code Encoder/Decoder", page_icon="🔳", layout="centered")

# # Function to generate QR Code
# def generate_qr_code(data, color="black", bg_color="white", size=10):
#     qr = qrcode.QRCode(version=1, box_size=size, border=2)
#     qr.add_data(data)
#     qr.make(fit=True)

#     # Create an image with custom colors
#     img = qr.make_image(fill_color=color, back_color=bg_color)
    
#     # Convert PIL image to bytes
#     img_bytes = io.BytesIO()
#     img.save(img_bytes, format="PNG")
#     img_bytes.seek(0)  # Reset pointer
    
#     return img_bytes

# # Function to decode QR Code
# def decode_qr_code(uploaded_image):
#     image = Image.open(uploaded_image)
#     image = np.array(image)  # Convert to NumPy array for OpenCV
#     detector = cv2.QRCodeDetector()
#     data, _, _ = detector.detectAndDecode(image)
#     return data if data else "No QR Code found!"

# # Streamlit UI
# st.title("🔳 QR Code Encoder & Decoder")

# # Sidebar Navigation
# option = st.sidebar.radio("Select an Option:", ["Generate QR Code", "Decode QR Code"])

# if option == "Generate QR Code":
#     st.subheader("📌 Generate QR Code")
#     text = st.text_area("Enter text or URL:", "https://example.com")

#     # Customization Options
#     col1, col2 = st.columns(2)
#     with col1:
#         qr_color = st.color_picker("QR Code Color", "#000000")
#     with col2:
#         bg_color = st.color_picker("Background Color", "#FFFFFF")

#     size = st.slider("QR Code Size", 5, 20, 10)

#     if st.button("Generate QR Code"):
#         qr_bytes = generate_qr_code(text, qr_color, bg_color, size)
        
#         # Display QR Code
#         st.image(qr_bytes, caption="Generated QR Code", use_container_width=True)
        
#         # Download Button
#         st.download_button(label="📥 Download QR Code", data=qr_bytes, file_name="qr_code.png", mime="image/png")

# elif option == "Decode QR Code":
#     st.subheader("📌 Decode QR Code")
#     uploaded_file = st.file_uploader("Upload a QR Code Image", type=["png", "jpg", "jpeg"])

#     if uploaded_file:
#         st.image(uploaded_file, caption="Uploaded QR Code", use_container_width=True)
#         decoded_text = decode_qr_code(uploaded_file)
#         st.success(f"Decoded Text: {decoded_text}")





import streamlit as st
import qrcode
import numpy as np
from PIL import Image
import cv2
import io

# Set page configuration
st.set_page_config(page_title="QR Code Encoder/Decoder", page_icon="🔳", layout="centered")

# Header
st.markdown("<h1 style='text-align: center;'>🔳 QR Code Encoder & Decoder</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Developed by Abdul Rehman</h4>", unsafe_allow_html=True)
st.markdown("---")

# Function to generate QR Code
def generate_qr_code(data, color="black", bg_color="white", size=10):
    qr = qrcode.QRCode(version=1, box_size=size, border=2)
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image with custom colors
    img = qr.make_image(fill_color=color, back_color=bg_color)
    
    # Convert PIL image to bytes
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)  # Reset pointer
    
    return img_bytes

# Function to decode QR Code
def decode_qr_code(uploaded_image):
    image = Image.open(uploaded_image)
    image = np.array(image)  # Convert to NumPy array for OpenCV
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(image)
    return data if data else "No QR Code found!"

# Sidebar Navigation
option = st.sidebar.radio("Select an Option:", ["Generate QR Code", "Decode QR Code"])

if option == "Generate QR Code":
    st.subheader("📌 Generate QR Code")
    text = st.text_area("Enter text or URL:", "https://example.com")

    # Customization Options
    col1, col2 = st.columns(2)
    with col1:
        qr_color = st.color_picker("QR Code Color", "#000000")
    with col2:
        bg_color = st.color_picker("Background Color", "#FFFFFF")

    size = st.slider("QR Code Size", 5, 20, 10)

    if st.button("Generate QR Code"):
        qr_bytes = generate_qr_code(text, qr_color, bg_color, size)
        
        # Display QR Code
        st.image(qr_bytes, caption="Generated QR Code", use_container_width=True)
        
        # Download Button
        st.download_button(label="📥 Download QR Code", data=qr_bytes, file_name="qr_code.png", mime="image/png")

elif option == "Decode QR Code":
    st.subheader("📌 Decode QR Code")
    uploaded_file = st.file_uploader("Upload a QR Code Image", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded QR Code", use_container_width=True)
        decoded_text = decode_qr_code(uploaded_file)
        st.success(f"Decoded Text: {decoded_text}")

# Footer
st.markdown("---")
st.markdown("<h5 style='text-align: center;'>© 2025 Developed by Abdul Rehman</h5>", unsafe_allow_html=True)
