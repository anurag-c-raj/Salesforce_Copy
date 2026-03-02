import streamlit as st
from PIL import Image

# 1. Set page config with your cloud icon and title
st.set_page_config(
    layout="wide", 
    page_title="Salesforce",
    page_icon="salesforce-icon.png" 
)

# 2. Inject CSS to hide all Streamlit UI elements (Header, Footer, Menu)
st.markdown(
    """
    <style>
    /* Hide the top header bar and the "Made with Streamlit" footer */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    
    /* Remove default padding so image fills the screen */
    .block-container {
        padding: 0rem !important;
    }

    /* Force the image to stretch horizontally and allow vertical scroll */
    .stImage > img {
        width: 100% !important;
        height: auto !important;
        display: block;
    }

    /* Target the specific container to remove top white space */
    .stAppViewMain {
        margin-top: -50px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def main():
    image_path = "Salesforce.png"
    
    try:
        img = Image.open(image_path)
        # Using the 2026 syntax you confirmed earlier
        st.image(img, width="stretch")
        
    except FileNotFoundError:
        st.error(f"Error: {image_path} not found.")

if __name__ == "__main__":
    main()