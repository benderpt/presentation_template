import streamlit as st

# Configuração inicial da página
st.set_page_config(page_title="Apresentação de Desenvolvimento de WebApps", layout="wide")

# Função principal para navegação entre secções
def main():
    st.sidebar.title("Navegação")
    pages = {
        "Página Inicial": homepage,
        "Oportunidade": oportunidade,
        "Proposta de Valor": proposta_valor,
        "Apresentação das Apps": apresentacao_apps,
        "Oferta para as Equipas": oferta_equipas,
        "Responsabilidades das Equipas": responsabilidades,
    }
    
    # Escolha da página
    selection = st.sidebar.radio("Seleciona uma secção", list(pages.keys()))
    pages[selection]()

# Secção: Página Inicial
def homepage():
    st.title("Apresentação de Desenvolvimento de WebApps")
    st.write("Bem-vindo(a) à apresentação! Explore as secções à esquerda para navegar pelos temas.")

# Secção: Oportunidade
def oportunidade():
    st.header("Oportunidade")
    st.write("Incubação de competências de desenvolvimento para complementar o portfólio de soluções de comunicação.")
    st.write("Projeção de um posicionamento inovador da marca.")

# Secção: Proposta de Valor
def proposta_valor():
    st.header("Proposta de Valor")
    st.write("- Data-driven")
    st.write("- Code-first")
    st.write("- Controlo da experiência do utilizador")
    st.write("- Modular")

# Secção: Apresentação das Apps
def apresentacao_apps():
    st.header("Apresentação das Apps")

    


# Secção: Oferta para as Equipas
def oferta_equipas():
    st.header("Oferta para as Equipas")
    st.write("Reutilização de módulos e desenvolvimento personalizado.")
    st.write("Transferência de competências com envolvimento das equipas no desenvolvimento.")

# Secção: Responsabilidades das Equipas
def responsabilidades():
    st.header("Responsabilidades das Equipas")
    st.write("#### Equipa de Desenvolvimento:")
    st.write("- UX: Experiência do Utilizador")
    st.write("- UI: Interface Digital")
    st.write("- DevOps: Desenvolvimento e Operações")
    st.write("#### Equipa de Colaboração:")
    st.write("- Domínio da área de negócio")

# Executar a aplicação
if __name__ == "__main__":
    main()
