import streamlit as st

# Informações dos integrantes
integrantes = [
    {
        "nome": "Luma Gallacio Gomes Ferreira",
        "email": "lumagallacio@gmail.com",
        "responsabilidade": "Análises de localidade, Site, Relatório",
        "foto": "integrantes/luma.jpeg"
    },
    {
        "nome": "Michelangelo Redondo dos Anjos",
        "email": "mranjos@usp.br",
        "responsabilidade": "Análises Exploratória, Dashboard interativo, Relatório",
        "foto": "integrantes/mika.jpeg"
    },
    {
        "nome": "Armando Augusto Dias Neto",
        "email": "armandoneto.dias@usp.br",
        "responsabilidade": "Análises de Sazonalidade, Apresentação, Vídeo",
        "foto": "integrantes/armando.jpeg"
    }
]

def app():
    st.title("Contato")
    # Exibir informações dos integrantes
    for integrante in integrantes:
        st.header(integrante["nome"])
        st.image(integrante["foto"], width=150)
        st.write(f"Email: {integrante['email']}")
        st.write(f"Atribuições: {integrante['responsabilidade']}")
        st.markdown("---")

if __name__ == "__main__":
    app()





