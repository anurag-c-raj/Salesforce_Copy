import streamlit as st
from PIL import Image

# Set page configuration with a Page Icon
# You can use an emoji like "☁️" or a path to a local file like "favicon.ico"
st.set_page_config(
    layout="wide", 
    page_title="Salesforce",
    page_icon="salesforce-icon.png" 
)

# Custom CSS for the full-width, scrollable experience
st.markdown(
    """
    <style>
    /* Remove padding to make it look like a real browser window */
    .block-container {
        padding: 0rem;
    }
    
    /* Ensure the image stretches horizontally and scrolls vertically */
    .stImage > img {
        width: 100% !important;
        height: auto !important;
        display: block;
    }

    /* Hide the Streamlit header/footer for a cleaner 'full page' look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

def main():
    image_path = "Salesforce.png"
    
    try:
        # Open the work order image
        img = Image.open(image_path)
        
        # Display using the 2026 'stretch' parameter
        st.image(img, width="stretch")
        
    except FileNotFoundError:
        st.error(f"Error: {image_path} not found. Ensure the image is in the same folder.")

if __name__ == "__main__":
    main()