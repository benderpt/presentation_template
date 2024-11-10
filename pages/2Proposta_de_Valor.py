import streamlit as st
from scripts.components import configure_page

# Chama a função para configurar a página e a sidebar
configure_page()

# Título centralizado e aumentado
st.markdown(
    """
    <h1 style="text-align: center; font-size: 4em;">
        Proposta de Valor
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
    if st.button("Data driven"):
        selected_option = "Data driven"

with col2:
    if st.button("Code first"):
        selected_option = "Code first"

with col3:
    if st.button("Modular"):
        selected_option = "Modular"

# Exibir conteúdo com base no botão selecionado
if selected_option == "Data driven":
    st.divider()
    # Espaço em branco acima do título
    st.markdown("<br>", unsafe_allow_html=True)

    # Título centralizado e aumentado
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 3em;">
            Experiência guiada por dados 
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.divider()
    # Título centralizado e aumentado
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 5em;">
            Controlo da experiência do utilizador
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)

elif selected_option == "Code first":
    st.divider()
    # Espaço em branco acima do título
    st.markdown("<br>", unsafe_allow_html=True)

    # Título centralizado e aumentado
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 3em;">
            Controlo preciso da experiência através de programação.
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()
    # Título centralizado e aumentado
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 5em;">
            Controlo da experiência do utilizador
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)

elif selected_option == "Modular":
    st.divider()
    # Espaço em branco acima do título
    st.markdown("<br>", unsafe_allow_html=True)

    # Título centralizado e aumentado
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 3em;">
            Desenvolvimento modular para reutilização rápido das soluções
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()

    # Título centralizado e aumentado
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 5em;">
            Controlo da experiência do utilizador
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
