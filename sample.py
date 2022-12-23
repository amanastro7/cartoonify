# Import necessary libraries
import streamlit as st
import cv2
from PIL import Image

# Set the app title and header
st.title("Image to Cartoon Converter App")
st.header("Upload an image to convert it to a cartoon-like image")

# Create a file uploader widget
uploaded_file = st.file_uploader("Choose an image to convert:")

# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the image and convert it to grayscale
    image = cv2.imread(uploaded_file)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a median blur to the grayscale image
    median_image = cv2.medianBlur(gray_image, 7)

    # Color the median-blurred grayscale image
    color_image = cv2.cvtColor(median_image, cv2.COLOR_GRAY2BGR)

    # Display the original image and the cartoon-like image side by side
    st.image(Image.fromarray(uploaded_file), width=400)
    st.image(Image.fromarray(color_image), width=400)
