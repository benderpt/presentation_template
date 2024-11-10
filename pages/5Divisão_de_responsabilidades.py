import streamlit as st
from scripts.components import configure_page

# Chama a função para configurar a página e a sidebar
configure_page()

# Título centralizado e aumentado
st.markdown(
    """
    <h1 style="text-align: center; font-size: 4em;">
        Responsabilidades da Equipa
    </h1>
    """,
    unsafe_allow_html=True
)

# CSS para centralizar os botões e ajustar o layout
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
col1, col2 = st.columns(2)

# Variável para armazenar o botão selecionado
selected_option = None

# Botões nas colunas com os textos corretos
with col1:
    if st.button("Equipa de Desenvolvimento"):
        selected_option = "Equipa de Desenvolvimento"

with col2:
    if st.button("Equipa em Colaboração"):
        selected_option = "Equipa em Colaboração"

# Exibir conteúdo com base no botão selecionado
if selected_option == "Equipa de Desenvolvimento":
    st.divider()
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <h2 style="text-align: center; font-size: 4em;">
            Equipa de Desenvolvimento
        </h2>
        <p style="text-align: center; font-size: 3em;">
            UX (experiência do utilizador) <br>
            UI (Interface digital) <br>
            DevOps (desenvolvimento programático da solução)
        </p>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()

elif selected_option == "Equipa em Colaboração":
    st.divider()
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <h2 style="text-align: center; font-size: 4em;">
            Equipa em Colaboração
        </h2>
        <p style="text-align: center; font-size: 3em;">
            Domínio da área de negócio
        </p>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()
