import streamlit as st
from PIL import Image
from pathlib import Path
from streamlit_option_menu import option_menu

# Import the necessary functions from your prediction.py and contact.py
from prediction import app as prediction_app
import contact

# Set the page configuration
st.set_page_config(page_title="Auto Insurance Fraud Detection", page_icon="🚗", layout="wide")

# Set up the current directory
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
logo_path = current_dir / "Photos" / "logo.png"
background_image_path = current_dir / "Photos" / "background_image.png"

# Load images
logo = Image.open(logo_path)
background_image = str(background_image_path)

# Apply the background image and custom fonts using custom CSS
page_bg_img = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@700&display=swap');

.stApp {{
    background-image: url({background_image});
    background-size: cover; /* Ensure the background image covers the entire screen */
    background-position: center; /* Centralize the background image */
    background-repeat: no-repeat;
}}
.sidebar .sidebar-content {{
    background-color: #000000; /* Set the sidebar background color to black */
    text-align: center;
}}
.sidebar .radio-group label {{
    font-size: 2em; /* Increase the font size of the navigation labels */
    color: white; /* Set the color to white for visibility */
}}
h1 {{
    font-family: 'Oswald', sans-serif;
    font-size: 5em;
    color: red;
    text-align: center;
}}
h2 {{
    font-family: 'Oswald', sans-serif;
    font-size: 3em;
    color: gold;
    text-align: center;
}}
h3 {{
    font-family: 'Arial', sans-serif;
    font-size: 2em;
    color: gray;
    text-align: center;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar with navigation
with st.sidebar:
    st.image(logo, width=150)  # Reduced the width of the logo image
    st.markdown("<h2 style='color: black;'>Auto Insurance Fraud Detection</h2>", unsafe_allow_html=True)
    page = option_menu(
        menu_title=None,
        options=['Dashboard', 'Fraud Prediction', 'Contact'],
        icons=["house", "person-check-fill", "file-person-fill"],
        menu_icon="cast",
        default_index=0,
        styles={
"container": {"padding": "5px", "background-color": "#1A1A2E"},  # Deep Blue
            "icon": {"color": "#E94560", "font-size": "25px"},  # Vibrant Red
            "nav-link": {"font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "#0F3460"},  # Dark Blue
            "nav-link-selected": {"background-color": "#16213E", "color": "#E94560"},  # Midnight Blue and Vibrant Red
        }
    )

# Header
st.markdown("<h1>Auto Insurance Fraud Detection</h1>", unsafe_allow_html=True)

# Dashboard page
if page == "Dashboard":
    st.markdown("<h2>Protecting You from Auto Insurance Fraud</h2>", unsafe_allow_html=True)
    st.markdown("<h3>Leveraging AI to detect and prevent fraudulent claims efficiently.</h3>", unsafe_allow_html=True)
    st.image(background_image, use_column_width=True)  # Adjust the width here as needed

# Detect Fraud page
elif page == "Fraud Prediction":
     prediction_app(st)

# Contact page
elif page == "Contact":
    contact.app(st, current_dir, Image)

# Footer or additional info
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
        font-size: 20px;
        color: black;
    }
    </style>
    <div class="footer">
        © 2024 Oluwadamilola Kolawole
    </div>
    """, unsafe_allow_html=True)

# Run the program
if __name__ == "__main__":
    # Since we are not using the MultiPage class, we simply run the script
    pass
