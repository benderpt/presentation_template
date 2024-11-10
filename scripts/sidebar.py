# scripts/components.py
import streamlit as st

def sidebar():
    """
    Configures the sidebar of the Streamlit application.

    This function sets up the sidebar with a logo, title, objectives, links, and a reset button.
    It checks if the logo and icon files exist before displaying them.
    """
    logo_path = "frontend/app/assets/logo_alt.png"
    icon_path = "frontend/app/assets/logo_alt.png"


    st.logo(logo_path, icon_image=icon_path)
