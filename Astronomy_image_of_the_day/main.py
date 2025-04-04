import streamlit as st
import requests as req
import os
from dotenv import load_dotenv

load_dotenv()

# Fetching API_KEY from .env
api_key = os.getenv("API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Fetching Datas from the API
res = req.get(url)

# Converting the received response into JSON Format
content = res.json()

# Displaying Above Data in a Web App
st.set_page_config("APOD")
st.title(content['title'])
st.image(content['hdurl'])
st.write(content['explanation'])