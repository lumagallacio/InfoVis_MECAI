import streamlit as st
import plotly.express as px
from pathlib import Path
import polars as pl
import pandas as pd
import folium
from folium import plugins
import streamlit.components.v1 as components
from geopy.geocoders import Nominatim
import plotly.graph_objects as go
import seaborn as sns
from folium.plugins import HeatMap, MarkerCluster, Fullscreen
from streamlit_folium import st_folium

caminho_bases = Path('data')
celulares_csv = caminho_bases.joinpath("CelularesSubtraidos_2023_2024_rp.csv")
valores_na = ["NULL", "NA", "N/A", "NaN"]
meses = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 
    5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 
    9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
}
df_cel = pd.read_csv(celulares_csv)
bairros = df_cel[df_cel['BAIRRO'].notna()]['BAIRRO'].unique().tolist()
tipos_in=['Furto (art. 155)', 'Roubo (art. 157)', 'Perda/Extravio']
df_cel['DATA_OCORRENCIA_BO'] = pd.to_datetime(df_cel['DATA_OCORRENCIA_BO'])
df_cel['mes_ocorrencia'] = df_cel['DATA_OCORRENCIA_BO'].dt.month
df_cel['mes'] = df_cel['mes_ocorrencia'].map(meses)

df_cel.loc[~df_cel['RUBRICA'].isin(tipos_in), 'RUBRICA'] = 'Outros'


rp_map_center = [-21.1775, -47.8103]


def bairros_incidencia(df_cel, col):
    # Filtrando e agrupando os dados usando pandas
    result = df_cel[df_cel['BAIRRO'].notna()]
    result = result.groupby('BAIRRO').size().reset_index(name='Ocorrências')
    result = result.sort_values(by='Ocorrências', ascending=False).head(5)

    # Gerando o gráfico de barras
    fig = px.bar(result, x='BAIRRO', y='Ocorrências', title="5 Maiores Ocorrências por Bairro")
    with col:
        st.plotly_chart(fig)


def gera_heatmap(data):
    valid_data = data.dropna(subset=['LATITUDE', 'LONGITUDE'])
    valid_data = valid_data[
        (valid_data['LATITUDE'] <= 5.27) & (valid_data['LATITUDE'] >= -33.75) & 
        (valid_data['LONGITUDE'] >= -73.99) & (valid_data['LONGITUDE'] <= -34.79)
    ]
    mode_location = valid_data.groupby(['LATITUDE', 'LONGITUDE']).size().idxmax()
    map_center = [mode_location[0], mode_location[1]]
    
    mapa = folium.Map(location=map_center, zoom_start=16)
    Fullscreen().add_to(mapa)

    # Adicionar os pontos de crimes como um mapa de calor
    heat_data = [[row['LATITUDE'], row['LONGITUDE']] for index, row in valid_data.iterrows() if not pd.isnull(row['LATITUDE']) and not pd.isnull(row['LONGITUDE'])]
    HeatMap(heat_data).add_to(mapa)

    # Adicionar os pontos de crimes usando clusters
    marker_cluster = MarkerCluster().add_to(mapa)
    for index, row in valid_data.iterrows():
        if not pd.isnull(row['LATITUDE']) and not pd.isnull(row['LONGITUDE']):
            folium.Marker(
                location=[row['LATITUDE'], row['LONGITUDE']],
                popup=(
                    f"Tipo de Local: {row['DESCR_TIPOLOCAL']}<br>"
                    f"Data: {row['DATA_OCORRENCIA_BO']}<br>"
                    f"Lat: {row['LATITUDE']}<br>"
                    f"Lng: {row['LONGITUDE']}"
                ),
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(marker_cluster)
            
    st.subheader("Mapa de Calor de Ocorrências")
    st_folium(mapa, width=800, height=200)
    # return mapa


def carrega_heatmap(ano):
    if ano=='Geral':
        html_file_path = f"results/heatmap_rp_celular_2023_e_2024.html"
        
    else:
        html_file_path = f"results/heatmap_rp_celular_{ano}.html"
    
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    st.subheader("Mapa de Calor de Ocorrências")
    components.html(html_content, height=600, width=800)


def tempo(dados_cp):
    # Agrupar dados_cp por mês e rubrica e contar ocorrências
    area_data = dados_cp.groupby(['mes_ocorrencia', 'RUBRICA']).size().unstack(fill_value=0)

    # Ordenar as colunas pelo total de ocorrências em ordem decrescente
    column_totals = area_data.sum(axis=0)
    area_data = area_data[column_totals.sort_values(ascending=False).index]

    palette = [f'rgb({int(c[0]*255)},{int(c[1]*255)},{int(c[2]*255)})' for c in sns.color_palette("rocket", len(area_data.columns))]

    # Criar o gráfico de área usando Plotly
    fig = go.Figure()

    for idx, rubrica in enumerate(area_data.columns):
        fig.add_trace(go.Scatter(
            x=area_data.index,
            y=area_data[rubrica],
            mode='lines',
            line=dict(width=0.5, color=palette[idx]),
            stackgroup='one',
            name=rubrica,
            fill='tonexty'
        ))

    # Configurações de layout para dark mode
    fig.update_layout(
        title='Tendência Acumulada de Ocorrências por Tipo e Mês',
        title_font=dict(size=24, color='white'),
        xaxis_title='Mês',
        yaxis_title='Contagem de Ocorrências',
        font=dict(color='white'),
        paper_bgcolor='#0E1117',
        plot_bgcolor='#0E1117',
        legend_title=dict(font=dict(color='white')),
        xaxis=dict(showgrid=True, gridcolor='gray', tickmode='linear', dtick=1),
        yaxis=dict(showgrid=True, gridcolor='gray'),
        width=800,
        height=600
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig)


   
def app():
    st.title("Dash Interativo")

    st.text(len(df_cel))
        
    ano = st.selectbox("Selecione o Ano:", ["Geral", "2024", "2023"])
    
    bairro = st.selectbox("Selecione o Bairro:", ["Todos"] + list(bairros))

    dados_cp= df_cel.copy()
    if ano != 'Geral':
        st.text('bairro '+ ano)
        dados_cp = dados_cp[dados_cp['ANO']==int(ano) ]
        if int(ano)==2024:
            dados_cp = dados_cp[dados_cp['DATA_OCORRENCIA_BO'].dt.month <= 4]
    if bairro != 'Todos':
        dados_cp = dados_cp[dados_cp['BAIRRO']== bairro]

        
    st.text('dados_cp '+ str(len(dados_cp)))
    st.text('ano '+ str(ano))
    st.text('bairro '+ bairro)
    if bairro=='Todos':
        carrega_heatmap(ano)
    else:
        gera_heatmap(dados_cp)

    st.subheader("Tabela de contagem de Ocorrências ao longo dos meses")
    contagem = dados_cp.groupby(['mes', 'RUBRICA']).size().unstack(fill_value=0)
    contagem['Total'] = contagem.sum(axis=1)
    contagem = contagem.reindex(meses.values()) 
    contagem = contagem.reindex(columns= ['Furto (art. 155)', 'Roubo (art. 157)', 'Perda/Extravio', 'Outros', 'Total']).dropna()
    linha_total = contagem.sum(numeric_only=True)
    linha_total.name = 'Total'
    contagem = pd.concat([contagem, pd.DataFrame(linha_total).T])
    st.write(contagem)
    
    tempo(dados_cp)
    
    
    # if bairro != "Todos":
    #     df_cel = df_cel[df_cel['BAIRRO'] == bairro]
    
    
    # col1, col2 = st.columns(2)
    # bairros_incidencia(df_cel, col1)
    # bairros_incidencia2(df_cel, col2)
    # mapa_calor2(ano)

if __name__ == "__main__":
    app()
