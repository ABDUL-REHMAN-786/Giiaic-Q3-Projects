import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import cv2
import numpy as np
from io import BytesIO

st.set_page_config(page_title="Photo Manipulation App", layout="centered")

st.title("🖼️ Photo Manipulation App")
st.markdown("Upload an image and apply basic manipulations using Python!")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

def get_image_download_link(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return buffered.getvalue()

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_container_width=True)

    st.sidebar.header("Edit Options")
    operation = st.sidebar.selectbox("Choose an Operation", [
        "None",
        "Convert to Grayscale",
        "Rotate",
        "Flip Horizontal",
        "Flip Vertical",
        "Adjust Brightness",
        "Apply Blur",
    ])

    edited_img = image.copy()

    if operation == "Convert to Grayscale":
        edited_img = image.convert("L")
    elif operation == "Rotate":
        angle = st.sidebar.slider("Rotation Angle", -180, 180, 90)
        edited_img = image.rotate(angle)
    elif operation == "Flip Horizontal":
        edited_img = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    elif operation == "Flip Vertical":
        edited_img = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    elif operation == "Adjust Brightness":
        factor = st.sidebar.slider("Brightness Factor", 0.1, 3.0, 1.0)
        enhancer = ImageEnhance.Brightness(image)
        edited_img = enhancer.enhance(factor)
    elif operation == "Apply Blur":
        blur_radius = st.sidebar.slider("Blur Radius", 1, 10, 2)
        edited_img = image.filter(ImageFilter.GaussianBlur(radius=blur_radius))

    st.image(edited_img, caption="Edited Image", use_container_width=True)

    st.download_button(
        label="📥 Download Edited Image",
        data=get_image_download_link(edited_img),
        file_name="edited_image.png",
        mime="image/png"
    )
else:
    st.info("Please upload an image to begin editing.")
