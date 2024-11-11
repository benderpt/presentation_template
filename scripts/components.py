import streamlit as st


def sidebar():
    """
    Configures the sidebar of the Streamlit application.

    This function sets up the sidebar with a logo, title, objectives, links, and a reset button.
    It checks if the logo and icon files exist before displaying them.
    """
    logo_path = "assets/logo.png"
    icon_path = "assets/logo_p.png"


    st.logo(logo_path, icon_image=icon_path)

    st.sidebar.subheader("DESENVOLVIMENTO DE WEBAPPS")

    st.sidebar.image("assets/characters_robot_alt.png")




# Define a função para configurar a página e a sidebar
def configure_page():
    # Configurações iniciais da página
    st.set_page_config(
        page_title="Apresentação de Desenvolvimento de WebApp",
        page_icon="assets/logo_p.png",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    # Configurações da sidebar
    sidebar()