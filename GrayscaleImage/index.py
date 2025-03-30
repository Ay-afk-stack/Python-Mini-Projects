import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

upload_image = st.file_uploader("Upload Image")


with st.expander("Start Camera"):
    #Start The Camera
    camera_image = st.camera_input("Camera")

    if camera_image:
        #Create a pillow image instance
        img = Image.open(camera_image)

        #Convert image to grayscale
        gray_img = img.convert("L")

        #Render the grayscale image on the webpage
        st.image(gray_img)

if upload_image:
        #Create a pillow image instance
        img = Image.open(upload_image)

        #Convert image to grayscale
        gray_img = img.convert("L")

        #Render the grayscale image on the webpage
        st.image(gray_img)
        