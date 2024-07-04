import streamlit as st
import pandas as pd
# Function to switch pages
def switch_page(page_name):
    st.session_state["current_page"] = page_name

# Check if the session state has a page set, otherwise default to 'home'
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "home"

# Sidebar for navigation
st.sidebar.title("Menu")
if st.sidebar.button("Introdução"):
    switch_page("home")
if st.sidebar.button("Dados"):
    switch_page("dados")
if st.sidebar.button("Análises de Celulares"):
    switch_page("analises")
if st.sidebar.button("Dashboard Interativo"):
    switch_page("dash_interativo")
if st.sidebar.button("Contato"):
    switch_page("contato")

# Display the current page
if st.session_state["current_page"] == "home":
    import home as Home
    Home.app()
elif st.session_state["current_page"] == "dados":
    import dados as Dados
    Dados.app()
elif st.session_state["current_page"] == "analises":
    import analises as Analises
    Analises.app()
elif st.session_state["current_page"] == "dash_interativo":
    # import dash_interativo as DashInterativo
    # DashInterativo.app()
    st.write("Redirecionando para o Dash Interativo...")

    # Código HTML/JavaScript para redirecionamento automático
    redirect_html = """
        <meta http-equiv="refresh" content="0; url=https://mecai.shinyapps.io/seg-publica/">
    """
    st.markdown(redirect_html, unsafe_allow_html=True)
elif st.session_state["current_page"] == "contato":
    import contato as Contato
    Contato.app()
