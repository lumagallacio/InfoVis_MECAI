import streamlit as st
import pandas as pd
from streamlit.components.v1 import html

def open_page(url):
    open_script = """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)


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
# if st.sidebar.button("Dashboard Interativo"):
if st.sidebar.button('Dashboard Interativo', on_click=open_page, args=("https://mecai.shinyapps.io/seg-publica/",)):
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

elif st.session_state["current_page"] == "contato":
    import contato as Contato
    Contato.app()
