# app.py
import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="Salesforce",
    page_icon="salesforce-icon.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
    header[data-testid="stHeader"] { display: none; }
    footer { visibility: hidden; }
    .full-screen-wrapper {
        width: 100vw; height: 100vh; margin: 0; padding: 0;
        background: #000; display: flex; align-items: center; justify-content: center; overflow: hidden;
    }
    .full-screen-wrapper img {
        max-width: 100vw; max-height: 100vh; object-fit: contain; display: block;
    }
</style>
""", unsafe_allow_html=True)

IMAGE_PATH = "Salesforce.png"

def to_base64(p: Path) -> str:
    with open(p, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

p = Path(IMAGE_PATH)
if not p.exists():
    st.error(f"Image not found: '{IMAGE_PATH}'. Put the file in the app folder or change IMAGE_PATH.")
else:
    mime = "image/png" if p.suffix.lower() == ".png" else "image/jpeg"
    img_b64 = to_base64(p)
    st.markdown(
        f"""
        <div class="full-screen-wrapper">
            <img src="data:{mime};base64,{img_b64}" alt="static image" />
        </div>
        """,
        unsafe_allow_html=True
    )