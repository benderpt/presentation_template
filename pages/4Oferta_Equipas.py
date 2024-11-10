import streamlit as st
from scripts.components import configure_page

# Chama a função para configurar a página e a sidebar
configure_page()

# Título centralizado e aumentado
st.markdown(
    """
    <h1 style="text-align: center; font-size: 4em;">
        Oferta para as Equipas
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
col1, col2, col3 = st.columns(3)

# Variável para armazenar o botão selecionado
selected_option = None

# Botões nas colunas com os textos corretos
with col1:
    if st.button("Reutilização de Módulos"):
        selected_option = "Reutilização de Módulos"

with col2:
    if st.button("Desenvolvimento Personalizado"):
        selected_option = "Desenvolvimento Personalizado"

with col3:
    if st.button("Transferência de Competências"):
        selected_option = "Transferência de Competências"

# Exibir conteúdo com base no botão selecionado
if selected_option == "Reutilização de Módulos":
    st.divider()
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <h2 style="text-align: center; font-size: 5em;">
            Reutilização de Módulos
        </h2>
        <p style="text-align: center; font-size: 3em;">
            Utilização de módulos já desenvolvidos com outros conteúdos.
        </p>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()

elif selected_option == "Desenvolvimento Personalizado":
    st.divider()
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <h2 style="text-align: center; font-size: 5em;">
            Desenvolvimento Personalizado
        </h2>
        <p style="text-align: center; font-size: 3em;">
            Soluções desenvolvidas à medida para atender a necessidades específicas.
        </p>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()

elif selected_option == "Transferência de Competências":
    st.divider()
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <h2 style="text-align: center; font-size: 5em;">
            Transferência de Competências
        </h2>
        <p style="text-align: center; font-size: 3em;">
            Através de envolvimento direto no processo de desenvolvimento, 
            onde alguém da equipa também escreve código.
        </p>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()