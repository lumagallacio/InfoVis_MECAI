import streamlit as st

def app():

    # Introduction and Objectives
    st.title("Análise de Roubos e Furtos de Celular em Ribeirão Preto")

    st.subheader("Apresentação")
    # URL do vídeo do YouTube
    video_url = "https://youtu.be/YvU15o5V15w"

    # Exibe o vídeo no Streamlit
    st.video(video_url)
    st.write("""
    ## Introdução
    A segurança pública é uma preocupação fundamental para qualquer sociedade. No presente trabalho estudamos a cidade de Ribeirão Preto, nos anos de 2023 e 2024.

    De acordo com a [Tribuna de Ribeirão](https://www.tribunaribeirao.com.br/ribeirao-e-a-8a-de-sp-com-mais-furtos-e-roubos-de-celular/), em 2024 Ribeirão Preto foi considerada a 8ª cidade do estado de São Paulo com mais furtos e roubos de celular, destacando a urgência em compreender este tipo de crime. Este projeto visa fornecer insights para auxiliar gestores de políticas públicas na implementação de estratégias para melhorar a segurança na cidade.

    ## Objetivos do Projeto
    O objetivo principal deste projeto é desenvolver uma ferramenta de análise de dados que possa ajudar a melhorar a segurança pública. Especificamente, os objetivos incluem:

    1. **Analisar da Sazonalidade**:
    - Identificar padrões sazonais nas ocorrências de roubos de celulares ao longo do ano.

    2. **Analisar por Período do Dia**:
    - Examinar a distribuição dos roubos de celulares em diferentes períodos do dia.
    - Determinar os horários de pico para esses crimes.

    3. **Identificar de Regiões com Maior ocorrências**:
    - Localizar áreas com alta incidência de roubos de celulares.
    - Facilitar a identificação de hotspots de criminalidade.

    4. **Construir um DashBoard interativo**:
    - Tornar o projeto uma ferramenta útil no entendimento de ocorrências de roubos e furtos de celulares na cidade de Ribeirão Preto.
    """)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col3:
        if st.button("Ir para Dados"):
            st.session_state["current_page"] = "dados"
            st.rerun()
    # Citation sources
    # st.write("""
    # ## Fontes
    # 1. [Tribuna de Ribeirão - Ribeirão Preto é a 8ª de SP com mais furtos e roubos de celular](https://www.tribunaribeirao.com.br/ribeirao-e-a-8a-de-sp-com-mais-furtos-e-roubos-de-celular/)
    # 2. [Secretaria de Segurança Pública do Estado de São Paulo - Dados de 2023 a 2024](http://www.ssp.sp.gov.br)
    # 3. [Portal de Dados Abertos do Estado de São Paulo](http://www.dados.gov.br)
    # """)
    
if __name__ == "__main__":
    app()
