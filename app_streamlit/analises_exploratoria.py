import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

missing_percentage_df = pd.DataFrame(
data = {
    'Coluna': [
        'TIPO_INTOLERANCIA', 'DESDOBRAMENTO', 'CIRCUNSTANCIA', 'DESCR_UNIDADE', 
        'HORA_OCORRENCIA', 'DESCR_PERIODO', 'DESCR_CONDUTA', 'DESCR_TIPOLOCAL', 
        'DESCR_SUBTIPOLOCAL', 'LONGITUDE', 'LATITUDE', 'CEP', 
        'FLAG_BLOQUEIO', 'FLAG_DESBLOQUEIO', 'NUMERO_LOGRADOURO', 'BAIRRO'
    ],
    'Percentual de Valores Ausentes (%)': [
        100.00, 98.38, 88.68, 70.47, 
        52.57, 47.43, 22.93, 18.74, 
        17.63, 12.19, 12.19, 10.40, 
        6.92, 6.92, 5.66, 0.56
    ]
}
)

def valores_nulos():
    st.header("Análise Exploratória")
    st.write("O objetivo é entender os dados, identificando padrões, relações e anomalias para insights e direcionamento de análises mais aprofundadas.")

    
    st.markdown("#### Colunas com Valores Ausentes")
    st.write("Durante a análise exploratória dos dados, foi identificado o percentual de valores ausentes em cada coluna. A tabela a seguir resume esses percentuais das colunas que contém valores ausentes:")
    st.dataframe(missing_percentage_df.set_index(missing_percentage_df.columns[0]))
    st.markdown("""
    Apesar da presença de valores ausentes em diversas colunas, algumas colunas foram utilizadas na análise devido à sua importância:

    - **LATITUDE e LONGITUDE** foram usadas para identificar a localização dos crimes. Apesar de perdermos 12% dos dados devido aos valores ausentes, a geolocalização foi importante para análise espacial e identificação de padrões geográficos dos crimes.

    - **BAIRRO** teve baixo percentual de valores ausentes (0.56%), logo foi usado para categorizar os dados.

    - **HORA_OCORRENCIA** Devido ao alto percentual de valores ausentes (52.57%) a coluna com a hora da ocorrência foi gerada a partir da coluna DATA_COMUNICACAO_BO, que não possui valores ausentes. Isso garantiu que a análise temporal fosse realizada.

    Portanto, a análise exploratória revelou uma quantidade significativa de valores ausentes em diversas colunas. No entanto, com o uso estratégico de colunas alternativas e essenciais como LATITUDE, LONGITUDE, BAIRRO e DATA_COMUNICACAO_BO, foi possível realizar as análises.
    """)
    
    st.markdown("#### Percentual de Valores Ausentes por Coluna")

    html_file_path = "/media/luma/hd1t3/Mestrado/Disciplinas/InfoVis/InfoVis_MECAI/results/percentual_valores_ausentes.html"
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        components.html(html_content, height=400, width=800)



def app():
    # st.title("Análises")


    # with st.expander("Análise Exploratória"):
    valores_nulos()
    
             
    html_file_path = "/media/luma/hd1t3/Mestrado/Disciplinas/InfoVis/InfoVis_MECAI/results/tipo.html"
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        components.html(html_content, height=400, width=600)
         
         
    st.markdown("### Análise de Correlação")
    st.markdown("""
    Para a análise de correlação, foram selecionadas colunas numéricas essenciais: LATITUDE, LONGITUDE, MES_COMUNICACAO, DIA_COMUNICACAO, MES_OCORRENCIA e DIA_OCORRENCIA. A matriz de correlação foi calculada com o método de correlação de Pearson com objetivo de investigar possíveis relações entre essas variáveis. A escala de correlação varia de -1 a 1, onde valores próximos a 1 indicam uma correlação positiva forte, valores próximos a -1 indicam uma correlação negativa forte, e valores próximos a 0 indicam pouca ou nenhuma correlação significativa.
    """)
    
    html_file_path = "/media/luma/hd1t3/Mestrado/Disciplinas/InfoVis/InfoVis_MECAI/results/matriz_correlacao.html"
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        components.html(html_content, height=500, width=800)
        
    st.markdown("""

    A correlação entre LATITUDE e LONGITUDE é perfeita (1), o que é esperado, dado que essas variáveis representam coordenadas geográficas.    
    
    Destaca-se uma forte correlação (0.94) entre MES_COMUNICACAO e MES_OCORRENCIA indicando que o mês de comunicação frequentemente coincide com o mês de ocorrência dos incidentes.
    
    Analogamente, a correlação de 0.75 entre DIA_COMUNICACAO e DIA_OCORRENCIA indica que muitas vezes o dia de comunicação está alinhado com o dia em que o incidente ocorreu.  
      
    Observa-se que que as correlações entre LATITUDE, LONGITUDE e as variáveis de data são baixas, o que sugere que não há uma relação linear forte entre a localização geográfica e as datas específicas dos incidentes.  
    """)
    
    st.markdown("""
    ### Marcas com mais ocorrências
    Vimos que no contexto de furto e roubo de celulares as marcas Samsung e Apple tem mais ocorrências, com aproximadamente 40% e 25% dos casos, respectivamente. Sabemos que há predominância das marcas Samsung e Apple na população dado sua popularidade. 
    """)
    html_file_path = "/media/luma/hd1t3/Mestrado/Disciplinas/InfoVis/InfoVis_MECAI/results/marca.html"
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        components.html(html_content, height=500, width=600)
    # with st.expander("Sazonalidade dos Crimes"):
    #     st.write("Aqui está o conteúdo que foi expandido.")
        
    # with st.expander("Período do Dia"):
    #     st.write("Aqui está o conteúdo que foi expandido.")

    # with st.expander("Regiões com Maior Tráfego"):
    #     st.write("Aqui está o conteúdo que foi expandido.")
      
    # with st.expander("Locais com Alta Incidência de Crimes"):
    #     st.write("Aqui está o conteúdo que foi expandido.")
      
        
    
    
    
    
    # col1, col2, col3 = st.columns([1, 1, 1])
    # with col3:
    #     if st.button("Ir para Dashboard"):
    #         st.session_state["current_page"] = "dash_interativo"
    #         st.rerun()

if __name__ == "__main__":
    app()
