import cv2
import numpy as np
import streamlit as st
from PIL import Image

def adjust_contrast(image, contrast_level):
    # Apply contrast adjustment
    image = np.array(image)
    adjusted_image = cv2.convertScaleAbs(image, alpha=contrast_level, beta=0)
    return adjusted_image

# Streamlit UI
st.title("Image Contrast Adjustment")

# Upload Image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Slider for adjusting contrast
contrast_level = st.slider("Adjust Contrast", min_value=1, max_value=5, value=1)

if uploaded_image is not None:
    # Convert to PIL Image
    image = Image.open(uploaded_image)

    # Show the original image
    st.image(image, caption="Original Image", use_column_width=True)

    # Adjust contrast
    adjusted_image = adjust_contrast(image, contrast_level)

    # Convert adjusted image to display in Streamlit
    adjusted_image_pil = Image.fromarray(adjusted_image)
    
    # Show adjusted image
    st.image(adjusted_image_pil, caption=f"Adjusted Image (Contrast Level: {contrast_level})", use_column_width=True)
