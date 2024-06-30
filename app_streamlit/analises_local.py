import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

data = {
    'Bairro': ['JD JÓQUEI CLUBE', 'CENTRO', 'CAMPOS ELISEOS', 'RIBEIRÂNIA', 'PQ RIBEIRAO PRETO', 'VILA TIBERIO', 'IPIRANGA'],
    'Incidentes': [522, 446, 341, 124, 115, 107, 102]
}

df_bairros = pd.DataFrame(data)

def analise_bairro_centro():
    st.markdown("###  Hotspots no Centro")
    st.image("results/centro.png", width=600)
    st.markdown("""- **Rodoviaria**: Observamos 46 ocorrências, é um local de grande movimento e concentração de pessoas, o que torna o ambiente propício para a ocorrência de roubos/furtos de celulares. Normalmente tem aglomeração de passageiros que estão muitas vezes distraídos, carregando bagagens e preocupados com horários. 
        """)

    left_co, cent_co,_ = st.columns((1, 5, 3))
    with cent_co:
        st.image("results/rodoviaria_street.png", width=600)

    st.markdown("""
        - **Região próxima à Cerqueira cesar**: É uma regiões com pontos de ônibus e grande tráfego de pessoas em horário de pico.
        """)
    left_co, cent_co,_ = st.columns((1, 5, 3))
    with cent_co:
        st.image("results/cerqueira_onibus.png", width=600)

    st.markdown("""
        - Além disso, notamos um hotspot com 18 ocorrências na região em frente ao prédio que antes abrigava a prefeitura da cidade e agora sedia a Secretaria Municipal de Cultura e Turismo de Ribeirão Preto. O local fica pouco iluminado à noite.
        """)
    left_co, cent_co,_ = st.columns((1, 5, 3))
    with cent_co:
        st.image("results/cerqueria_praca.png", width=600)

    st.markdown("""
        - **Praça XV de Novembro e Catedral**: Na região das praças, com em torno de 20 ocorrências, existem muitos pontos de ônibus e grande tráfego de pessoas.
        """)
    left_co, cent_co,_ = st.columns((1, 5, 3))
    with cent_co:
        st.image("results/catedral.png", width=600)

    st.markdown("""
        - **Avenida Jerônimo Gonçalves com Francisco Junqueira**: São avenidas muito movimentadas na cidade, notamos 63 ocorrência nessa esquina.
        """)
    left_co, cent_co,_ = st.columns((1, 5, 3))
    with cent_co:
        st.image("results/jeronimo.png", width=600)

def analise_bairro_joquei():
    st.markdown("###  Grande Hotspot no JD JÓQUEI CLUBE")
    st.markdown("""- **Parque Permanente de Exposições**: É um ponto central para grandes eventos, como o JOÃO ROCK 2023 e o Ribeirão Rodeio Music, atraindo milhares de pessoas. Além disso, a proximidade com o Aeroporto "Dr. Leite Lopes" e a localização próxima à Rodovia Anhanguera facilitam o acesso e a fuga rápida, tornando a área ainda mais atrativa para roubos/furtos. A movimentação intensa de pessoas e veículos nesses períodos sobrecarrega a capacidade de monitoramento e segurança, contribuindo para o aumento dos índices de criminalidade.
        """)

    left_co, cent_co,_ = st.columns((1, 5, 3))
    with cent_co:
        st.image("results/joquei.png", width=600)
    left_co, cent_co,_ = st.columns((1, 5, 3))
    with cent_co:
        st.image("results/parque_exp.png", width=600)

def app():

    st.header("Análise de Locais com Alta Incidência")

    st.markdown("""
        ####  Tipos de Locais com mais ocorrências 
         Observamos que a grande maioria dos furtos e roubos ocorre em vias públicas, representando 83,97% dos casos (4014 ocorrências). Locais residenciais ocupam a segunda posição, mas com uma proporção significativamente menor, contabilizando apenas 4,10% (196 ocorrências). Isso mostra que a segurança em vias públicas é uma área crítica que necessita de atenção, pois concentra a maior parte dos crimes. 
                """)
    html_file_path = "results/tipo_local.html"
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        components.html(html_content, height=400, width=600)
    
    st.markdown("""
    ####  Bairros com maior incidência
    Observamos que JD JOQUEI CLUBE tem a maior incidência de ocorrências, com 522 casos, seguido pelo CENTRO, com 446 casos. CAMPOS ELISEOS e RIBEIRANIA também se destacam, com 341 e 124 casos, respectivamente. Nas próximas análises, buscamos aprofundar o entendimento dos fatores que contribuem para a alta incidência de ocorrências nos bairros CENTRO e JD JOQUEI CLUBE.
    """)
    # st.dataframe(df_bairros.set_index(df_bairros.columns[0]))

    html_file_path = "results/treemap.html"
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        components.html(html_content, height=400, width=800)

    st.markdown("""
        ####  Mapa de Calor com Clusters
        O objetivo foi gerar um mapa interativo que visualiza a distribuição espacial dos crimes de roubo de celulares registrados em 2023, utilizando as técnicas de heatmap e cluster.
                """)
    
    html_file_path = "results/heatmap_rp_celular_2023.html"
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        components.html(html_content, height=550, width=800)

    analise_bairro_centro()
    analise_bairro_joquei()

    st.subheader('Análise de Densidade de Kernel (KDE)')

    # Texto explicativo
    st.write("""
    A Análise de Densidade de Kernel (KDE) é uma técnica estatística utilizada para estimar a densidade de uma variável contínua. No contexto de dados geolocalizados a KDE é aplicada para identificar áreas de alta concentração ("hotspots") permitindo a visualização e análise de padrões espaciais. 

    - Utilizamos a função kernel gaussiana, uma função de densidade de probabilidade que suaviza a influência dos pontos de dados ao redor de cada ponto.
    - Para cada ponto de dado, aplicamos a função kernel, criando uma superfície contínua que representa a densidade dos incidentes.
    """)
    st.write("Fórmula da Estimativa da Densidade Kernel")
    st.latex(r'''
    \hat{f}(x) = \frac{1}{n h} \sum_{i=1}^{n} K \left( \frac{x - x_i}{h} \right)
    ''')
    
    st.markdown("""
    onde:
    - $\hat{f}(x)$ é a estimativa da densidade no ponto $x$,
    - $n$ é o número total de pontos de dados,
    - $h$ é a largura de banda (bandwidth),
    - $K$ é a função kernel,
    - $x_i$ são os pontos de dados.
    """)

    st.write("Fórmula da Função Kernel Gaussiana")
    
    st.latex(r'''
    K(u) = \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}u^2}
    ''')

    st.markdown("""
    O HeatMap gerado pela KDE revelou duas áreas de alta densidade de incidentes de crimes, identificando os hotspots. 
    """)

    html_file_path = "results/kde_plot.html"
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        components.html(html_content, height=550, width=800)
        
    st.markdown("""
    Para identificar as regiões correspondentes no mapa, criamos polígonos para representar os hotspots de maior concentração de incidentes. O hotspot maior, indicado por um polígono roxo, abrange a região de latitude -21.19 a -21.16 e longitude -47.82 a -47.80. O hotspot menor, representado por um polígono verde, cobre as coordenadas de latitude -21.16 a -21.13 e longitude -47.76 a -47.78. O polígono roco corresponde ao bairro CENTRO e um pouco de CAMPOS ELISEOS e o verde corresponde ao JD JOQUEI CLUBE.
    """)
    left_co, cent_co,_ = st.columns((1, 5, 3))
    with cent_co:
        st.image("results/hot_spot_kde.png", width=600)


if __name__ == "__main__":
    app()
