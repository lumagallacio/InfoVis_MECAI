import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import analises_exploratoria
import analises_local
import analises_sazonalidade
from streamlit_option_menu import option_menu


def app():
    # st.title("Análises")



    selected = option_menu(
        menu_title=None,
        options=["Análise Exploratória",  "Locais com Alta Incidência", "Analise de Sazonalidade"],
        icons=["bar-chart", "exclamation-triangle", "calendar-date"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "5px", "background-color": "rgb(14, 17, 23)"},
            "icon": {"color": "white", "font-size": "18px"},
            "nav-link": {"font-size": "17px", "text-align": "left", "margin": "0px", "color": "white", "--hover-color": "#444444"},
            "nav-link-selected": {"background-color": "#333333", "color": "white", "border-radius": "5px"},
            # "nav-link-selected": {"background-color": "rgb(14, 17, 23)", "color": "white"},
        }
    )
    
    if selected == "Análise Exploratória":
        analises_exploratoria.app()
    elif selected == "Locais com Alta Incidência":
        analises_local.app()
    elif selected == "Analise de Sazonalidade":
        analises_sazonalidade.app()



    # if st.button("📋 Resumo", key="resumo"):
    #     st.session_state.current_page = "Resumo"
    # if st.button("📊 Análise exploratória", key="analises_exploratoria"):
    #     st.session_state.current_page = "Analise Exploratoria"
    # if st.button("👁 Visualização", key="visualizacao"):
    #     st.session_state.current_page = "Visualização"
    # if st.button("📈 Dashboard", key="dashboard"):
    #     st.session_state.current_page = "Dashboard"

    # if st.session_state.current_page == "Analise Exploratoria":
    #     analises_exploratoria.show()


    # col1, col2, col3 = st.columns([1, 1, 1])
    # with col3:
    #     if st.button("Ir para Dashboard"):
    #         st.session_state["current_page"] = "dash_interativo"
    #         st.rerun()

if __name__ == "__main__":
    app()

        
    # with st.expander("Sazonalidade dos Crimes"):
    #     st.write("Aqui está o conteúdo que foi expandido.")
        
    # with st.expander("Período do Dia"):
    #     st.write("Aqui está o conteúdo que foi expandido.")

    # with st.expander("Regiões com Maior Tráfego"):
    #     st.write("Aqui está o conteúdo que foi expandido.")
      
    # with st.expander("Locais com Alta Incidência de Crimes"):
    #     st.write("Aqui está o conteúdo que foi expandido.")
      
