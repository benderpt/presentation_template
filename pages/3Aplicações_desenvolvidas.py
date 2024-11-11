import streamlit as st
from scripts.components import configure_page

# Chama a função para configurar a página e a sidebar
configure_page()

# Título centralizado e aumentado
st.markdown(
    """
    <h1 style="text-align: center; font-size: 4em;">
        Aplicações desenvolvidas
    </h1>
    """,
    unsafe_allow_html=True
)

# Adiciona CSS para centralizar o texto e expandir os botões
st.markdown(
    """
    <style>
    .stButton > button {
        width: 100%;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Criação de três colunas para os botões
col1, col2, col3 = st.columns(3)

# Variável para armazenar o botão selecionado
selected_option = None

# Botões nas colunas
with col1:
    if st.button("Micro-learning"):
        selected_option = "Micro-learning"

with col2:
    if st.button("Quizz"):
        selected_option = "Quizz"

with col3:
    if st.button("Portal"):
        selected_option = "Portal"

# Exibir conteúdo com base no botão selecionado
if selected_option == "Micro-learning":
    # URL da aplicação secundária
    app_url = "https://teoriadamudanca.streamlit.app?embed=true"  # Substitui pelo URL da tua segunda app

    # Embed da aplicação usando um iFrame, centralizado
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <iframe src="{app_url}" width="100%" height="1200" frameborder="0"></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )

elif selected_option == "Quizz":
    app_url = "https://quizzpoenmp.streamlit.app?embed=true"  # Substitui pelo URL da tua segunda app

    # Embed da aplicação usando um iFrame, centralizado
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <iframe src="{app_url}" width="100%" height="1200" frameborder="0"></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )


elif selected_option == "Portal":
    st.image("assets/portal.png")
