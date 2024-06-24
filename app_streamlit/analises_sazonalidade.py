import streamlit as st
import streamlit.components.v1 as components
import pandas as pd


def app():
    # st.title("Análises")
    st.header("Análise de Sazonalidade")
    st.markdown("""O objetivo é identificar padrões sazonais nas ocorrências de roubos de celulares ao longo do tempo.""")
    st.markdown("""
                ### Coordenadas Paralelas
                A análise do gráfico de categorias paralelas mostra a relação entre os bairros, tipos de ocorrência e bimestres em Ribeirão Preto. 
                """)

         
    html_file_path = "/media/luma/hd1t3/Mestrado/Disciplinas/InfoVis/InfoVis_MECAI/results/parallel_categories_rp_celular_2023.html"

    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        components.html(html_content, height=600, width=800)

    st.markdown("""
                Observamos que o primeiro bimestre tem menos ocorrências, com a maioria dos incidentes concentrados no CENTRO. No entanto, o CENTRO também se destaca no segundo e sexto bimestres.
                
                ##### Análise dos Eventos no JD Joquei Clube
                No JD Joquei Clube, analisamos os eventos ocorridos em 2023, conforme [dados da prefeitura](https://www.ribeiraopreto.sp.gov.br/portal/inovacao-desenvolvimento/parque-permanente-de-exposicoes):
                
                - "Ribeirão Rodeo Music" e "Queima do Alho" ocorreram em abril (bimestre 2), período em que houve um aumento significativo de ocorrências, totalizando 125 furtos/roubos.
                - "João Rock" aconteceu em junho (bimestre 3), correspondendo ao pico de 201 furtos/roubos no JD Joquei Clube.
                - "Buteco do Gustavo Lima" ocorreu em agosto (bimestre 4), um período que registrou 95 furtos/roubos.
                - Ocorream outros eventos como "LUP - Liga Universitária Paulista" em setembro (bimestre 5) e "Encontro das Tribos" em outubro (bimestre 5), porém não identificamos um aumento significativo nesse período, uma possível causa é pelo eventos terem menor porte que os anteriores.
                                
                Essa relação sugere que grandes eventos no JD Joquei Clube estão associados a picos de criminalidade, especialmente furtos e roubos. Esses eventos atraem grandes multidões, o que pode facilitar a ação de criminosos. Portanto, medidas de segurança durante esses eventos são essenciais para reduzir a incidência de crimes.
                """)

    st.markdown("""
                ### Tendência Acumulada de Ocorrências por Tipo e Mês
                """)
    html_file_path = "/media/luma/hd1t3/Mestrado/Disciplinas/InfoVis/InfoVis_MECAI/results/plot_trends.html"
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        components.html(html_content, height=600, width=900)

    st.markdown("""
    O gráfico de área mostra a distribuição mensal dos tipos de ocorrências em toda a cidade ao longo de 2023. Notamos picos nos meses de abril (mês 4), junho (mês 6) e agosto (mês 8), que coincidem com grandes eventos e possivelmente outras atividades na cidade. Em abril, o aumento nas ocorrências pode estar associado a eventos como o Ribeirão Rodeo Music e a Queima do Alho. Em junho, o pico é observado durante o período do João Rock. Em agosto, vemos outro aumento significativo, possivelmente relacionado ao Buteco do Gustavo Lima. Esses meses mostram um aumento tanto em furtos (art. 155) quanto em roubos (art. 157), sugerindo que eventos de grande porte e períodos de maior atividade estão diretamente relacionados ao aumento das atividades criminais na cidade. 
                """)


    st.subheader("Análise de Horário do Dia")
    
    st.markdown("""
    Para está análise usamo uma coluna que continha 52% de valores ausentes.
    Para a análise da distribuição de ocorrências de crimes por período do dia, utilizamos a coluna HORA_OCORRENCIA que contém 52% de valores nulos. Optamos por remover esses valores nulos e observar com os dados disponíveis.
                """)

    st.markdown("""
                #### Distribuição de Crimes por Hora do Dia (Polar Bar Chart)
        O Polar Bar Chart mostra a distribuição das ocorrências de crimes por hora do dia em toda a cidade. A análise revela que as ocorrências de crimes são significativamente mais altas entre as 18:00 e 22:00 horas, com um pico por volta das 20:00 horas.
                """)
    html_file_path = "/media/luma/hd1t3/Mestrado/Disciplinas/InfoVis/InfoVis_MECAI/results/polar_bar.html"
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        components.html(html_content, height=600, width=700)
        
        st.markdown("""
    O Polar Bar Chart mostra a distribuição das ocorrências de crimes por hora do dia em toda a cidade. A análise revela que as ocorrências de crimes são significativamente mais altas entre as 18:00 e 22:00 horas, com um pico por volta das 20:00 horas. Esse período coincide com o final do expediente e a hora em que muitas pessoas estão retornando para casa ou saindo para atividades de lazer, aumentando a exposição.
            """)
        
    st.markdown("""
            #### Ocorrências por Bairro e Período
            """)
    html_file_path = "/media/luma/hd1t3/Mestrado/Disciplinas/InfoVis/InfoVis_MECAI/results/bairro_periodo.html"
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        components.html(html_content, height=400, width=700)

    st.markdown("""
                
        O heatmap mostra a distribuição das ocorrências de crimes por período do dia e bairros com maior incidência. Observamos que o bairro CENTRO tem a maior concentração de incidentes, especialmente à noite (91 ocorrências) e à tarde (90 ocorrências). CAMPOS ELISEOS também apresenta uma alta incidência de crimes, principalmente à noite (90 ocorrências) e à tarde (74 ocorrências). No JD JOQUEI CLUBE, as ocorrências são mais frequentes durante a madrugada (37 ocorrências). 
                """)
    
if __name__ == "__main__":
    app()
