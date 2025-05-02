import streamlit as st
import qrcode
from PIL import Image
import io
import cv2
import numpy as np

st.set_page_config(page_title="QR Code Encoder/Decoder", page_icon="🔳", layout="centered")
st.title("🔳 QR Code Encoder & Decoder")
st.markdown("Generate or decode QR codes easily!")

tabs = st.tabs(["📤 QR Code Encoder", "📥 QR Code Decoder"])

# ------------------ ENCODER ------------------ #
with tabs[0]:
    st.subheader("📤 Generate QR Code")
    qr_input = st.text_input("Enter text or URL to encode:", placeholder="e.g. https://example.com")

    if st.button("Generate QR"):
        if qr_input.strip() == "":
            st.warning("Please enter some text or URL to generate a QR.")
        else:
            # Generate QR code
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(qr_input)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

            # Convert to bytes for download
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            byte_im = buf.getvalue()

            # Display QR code using correct format
            st.image(byte_im, caption="Generated QR Code", use_container_width=True)

            # Download button
            st.download_button("⬇️ Download QR Code", data=byte_im, file_name="qr_code.png", mime="image/png")

# ------------------ DECODER ------------------ #
with tabs[1]:
    st.subheader("📥 Decode QR Code from Image")
    uploaded_file = st.file_uploader("Upload QR Code Image (PNG, JPG)", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(image)

        # Convert for displaying via Streamlit (BGR to RGB)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        st.image(image_rgb, caption="Uploaded QR Image", use_container_width=True)

        if data:
            st.success(f"✅ Decoded Data:\n\n**{data}**")
        else:
            st.error("❌ No QR code found or could not decode the image.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit, OpenCV, Pillow, and qrcode")
