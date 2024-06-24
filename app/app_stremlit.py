import streamlit as st
import plotly.express as px
from pathlib import Path
import polars as pl
import pandas as pd
import folium
from folium import plugins
import streamlit_folium

# Load data and compute static values
tips = px.data.tips()
bill_rng = (min(tips.total_bill), max(tips.total_bill))

caminho_bases = Path(r'/media/luma/hd1t3/Mestrado/Disciplinas/InfoVis/InfoVis_MECAI/data')
caminho_base_veiculos_csv = caminho_bases.joinpath("VeiculosSubtraidos_2023_2024.csv")
caminho_base_celulares_csv = caminho_bases.joinpath("CelularesSubtraidos_2023_2024_UTF8.csv")
valores_na = ["NULL", "NA", "N/A", "NaN"]

df_veiculos = pl.scan_csv(caminho_base_veiculos_csv, has_header=True, separator=";", low_memory=True, infer_schema_length=1000, null_values=valores_na).collect()
df_celulares = pl.scan_csv(caminho_base_celulares_csv, has_header=True, separator=";", low_memory=True, infer_schema_length=1000, null_values=valores_na).collect()

# Sidebar Menu
menu = st.sidebar.radio("Menu", ["Introdução", "Dados", "Análises", "Dash Iterativo", "Grupo"])

if menu == "Dash Iterativo":
    # Inputs in Sidebar
    cidade_key = st.sidebar.selectbox("Escolha uma opção:", {"cd1": "RIBEIRAO PRETO", "cd2": "S.CARLOS"})
    tipo_roubo = st.sidebar.selectbox("Escolha uma opção:", {"op1": "Veículos", "op2": "Celulares"})
    ano = st.sidebar.selectbox("Selecione o Ano:", {"an0": "Geral", "an1": "2024", "an2": "2023"})

    cidade = {"cd1": "RIBEIRAO PRETO", "cd2": "S.CARLOS"}[cidade_key]

    if tipo_roubo == "op1":
        df = df_veiculos
    else:
        df = df_celulares

    if ano == "an1":
        df = df.filter(pl.col('ANO') == 2024)
    elif ano == "an2":
        df = df.filter(pl.col('ANO') == 2023)

    df_filtrado = df.filter(pl.col('CIDADE') == cidade)

    unique_bairros = df_filtrado.select('BAIRRO').unique().to_series().drop_nans().to_list()
    unique_bairros = [value for value in unique_bairros if value and value.strip()]
    bairro = st.sidebar.selectbox("Selecione o Bairro:", unique_bairros)

    if bairro:
        df_filtrado = df_filtrado.filter(pl.col('BAIRRO') == bairro)

    # Display Data
    st.header("Bairros com maior incidência")
    
    result = (df_filtrado.filter(pl.col("BAIRRO").is_not_null())
              .group_by('BAIRRO')
              .agg(pl.count().alias("# Ocorrências"))
              .sort("# Ocorrências", descending=True)
              .limit(5))
    st.write(result.collect().to_pandas())

    st.header("Mapa de Calor")
    mapa = folium.Map(location=[-21.1767, -47.8208], zoom_start=13)
    df_filtro_map = df_filtrado.select(['LATITUDE', 'LONGITUDE']).to_pandas().dropna()
    mapa.add_child(plugins.HeatMap(df_filtro_map[['LATITUDE', 'LONGITUDE']]))
    streamlit_folium.folium_static(mapa)

elif menu == "Home":
    st.header("Bem-vindo ao sistema de análise de dados de segurança pública")
elif menu == "Contact":
    st.header("Contato: contato@example.com")
