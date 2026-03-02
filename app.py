import streamlit as st
from PIL import Image

# Set page configuration to wide mode
st.set_page_config(layout="wide", page_title="Salesforce Work Order Viewer")

# Custom CSS to force the image to fit the container width and handle scrolling
st.markdown(
    """
    <style>
    /* Remove padding from the main block */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    
    /* Ensure the image container is scrollable and image is responsive */
    .stImage > img {
        width: 100%;
        height: auto;
        display: block;
    }
    
    /* Disable user-agent zooming/pinching on mobile if desired 
       Note: Streamlit doesn't natively support disabling browser-level zoom, 
       but we can hint via viewport meta tags if this were a raw HTML app. */
    </style>
    """,
    unsafe_allow_html=True,
)

def main():
    # Load the image
    image_path = "Salesforce.png"
    
    try:
        img = Image.open(image_path)
        
        # Display the image
        # use_container_width=True ensures it fits the screen horizontally
        st.image(img, use_container_width=True)
        
    except FileNotFoundError:
        st.error(f"Error: {image_path} not found. Please ensure the image is in the same directory as this script.")

if __name__ == "__main__":
    main()