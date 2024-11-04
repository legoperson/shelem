# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 21:07:59 2024

@author: 142397
"""

import streamlit as st
import folium
from streamlit_folium import st_folium
import numpy as np
import os
import base64

# Set coordinates for Fuzhou
latitude = 26.0745
longitude = 119.2965

# Function to retrieve a random image from the images directory
def get_random_image_from_directory(directory="images"):
    # List all image files
    files = os.listdir(directory)
    image_files = [f for f in files if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    if not image_files:
        return None  # Return None if no images found
    # Select a random image
    random_image = np.random.choice(image_files)
    # Return the full path to the random image
    return os.path.join(directory, random_image)

# Create Streamlit app
st.title("Random Image Map in Fuzhou")
st.write("This map displays 5 random markers around Fuzhou. Click a marker to see an image from the images directory.")

# Initialize map centered on Fuzhou
m = folium.Map(location=[latitude, longitude], zoom_start=12)

# Add 5 random markers around the Fuzhou location
num_markers = 5  # Number of markers to add
for _ in range(num_markers):
    # Generate random coordinates close to Fuzhou using numpy
    random_lat = latitude + np.random.uniform(-0.01, 0.01)
    random_lon = longitude + np.random.uniform(-0.01, 0.01)
    
    # Get a random image from the directory
    image_path = get_random_image_from_directory()
    
    if image_path:
        # Convert image to base64 for embedding in HTML
        with open(image_path, "rb") as img_file:
            img_base64 = base64.b64encode(img_file.read()).decode('utf-8')
        
        # HTML code for image to display in popup
        img_html = f'<img src="data:image/jpeg;base64,{img_base64}" width="150" height="150">'
        iframe = folium.IFrame(html=img_html, width=160, height=160)
        popup = folium.Popup(iframe, max_width=160)
        
        # Add marker with popup that shows the image
        folium.Marker(location=[random_lat, random_lon], popup=popup).add_to(m)

# Display the map with Streamlit
st_folium(m, width=700, height=500)
