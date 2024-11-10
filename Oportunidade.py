import streamlit as st
from scripts.components import configure_page

# Chama a função para configurar a página e a sidebar
configure_page()

# Título centralizado e aumentado
st.markdown(
    """
    <h1 style="text-align: center; font-size: 4em;">
        Oportunidades
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
    if st.button("Competências"):
        selected_option = "Competências"

with col2:
    if st.button("Portfólio"):
        selected_option = "Portfólio"

with col3:
    if st.button("Posicionamento"):
        selected_option = "Posicionamento"

# Exibir conteúdo com base no botão selecionado
if selected_option == "Competências":
    st.divider()
    # Espaço em branco acima do título
    st.markdown("<br>", unsafe_allow_html=True)

    # Título centralizado e aumentado
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 5em;">
            Incubação de competências de desenvolvimento de aplicações
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.divider()

elif selected_option == "Portfólio":
    st.divider()
    # Espaço em branco acima do título
    st.markdown("<br>", unsafe_allow_html=True)

    # Título centralizado e aumentado
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 5em;">
            Complementar portfólio de soluções de comunicação
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()

elif selected_option == "Posicionamento":
    st.divider()
    # Espaço em branco acima do título
    st.markdown("<br>", unsafe_allow_html=True)

    # Título centralizado e aumentado
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 5em;">
            Projeção de posicionamento inovador de marca
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()

