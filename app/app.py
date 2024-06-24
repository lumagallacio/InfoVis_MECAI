import faicons as fa
import plotly.express as px
from shinywidgets import render_plotly

from shiny import reactive, render, req
from shiny.express import input, ui

from pathlib import Path
from datetime import date

import polars as pl
import polars.selectors as cs
import pandas as pd
import folium
from folium import plugins
import matplotlib.pyplot as plt
import squarify
import plotly.express as px

# Load data and compute static values
tips = px.data.tips()
bill_rng = (min(tips.total_bill), max(tips.total_bill))

caminho_bases = Path(r'/media/luma/hd1t3/Mestrado/Disciplinas/InfoVis/InfoVis_MECAI/data')
caminho_base_veiculos_csv = caminho_bases.joinpath("VeiculosSubtraidos_2023_2024.csv")
caminho_base_celulares_csv = caminho_bases.joinpath("CelularesSubtraidos_2023_2024_UTF8.csv")
valores_na = ["NULL", "NA", "N/A", "NaN"]

df_veiculos = pl.scan_csv(caminho_base_veiculos_csv, has_header=True, separator=";", low_memory=True, infer_schema_length=1000, null_values=valores_na) #precisa coletar, pois é só uma representação
df_celulares = pl.scan_csv(caminho_base_celulares_csv, has_header=True, separator=";", low_memory=True, infer_schema_length=1000, null_values=valores_na) #precisa coletar, pois é só uma representação

# df = pl.scan_csv(caminho_base_veiculos_csv, has_header=True, separator=";", low_memory=True, infer_schema_length=1000, null_values=valores_na) #precisa coletar, pois é só uma representação
@reactive.Calc
def df_filtro():
    flag = input.select_tipo_roubo()
    flag_ano = input.select_ano()
    cidade_key = input.select_cidade()
    cidade = {"cd1": "RIBEIRAO PRETO", "cd2": "S.CARLOS"}[cidade_key]
    
    if flag == "op1":
        df = df_veiculos
    else:
        df = df_celulares

    if flag_ano == "an0":
        df = df
    elif flag_ano == "an1":
        df = df.filter(pl.col('ANO') == 2024)
    else:
        df = df.filter(pl.col('ANO') == 2023)
    
    df_filtrado = df.filter(pl.col('CIDADE') == cidade)
    return df_filtrado

def bairros_mais_roubos():
    flag = input.select_tipo_roubo()
    flag_ano = input.select_ano()
    cidade_key = input.select_cidade()
    cidade = {"cd1": "RIBEIRAO PRETO", "cd2": "S.CARLOS"}[cidade_key]
    
    if flag == "op1":
        df = df_veiculos
    else:
        df = df_celulares

    if flag_ano == "an0":
        df = df
    elif flag_ano == "an1":
        df = df.filter(pl.col('ANO') == 2024)
    else:
        df = df.filter(pl.col('ANO') == 2023)
    
    df_filtrado = df.filter(pl.col('CIDADE') == cidade)
    
    result = (df_filtrado.filter(pl.col("BAIRRO").is_not_null())
          .group_by('BAIRRO')
          .agg(pl.count().alias("# Ocorrências"))
          .sort("# Ocorrências",descending=True)
          .limit(5))

    # Coletando os resultados para um DataFrame
    top_bairros = result.collect()

    return top_bairros

# def df_filtro():
#     cidade_key = input.select_cidade()
#     cidade = {"cd1": "RIBEIRAO PRETO", "cd2": "S.CARLOS"}[cidade_key]
#     df_filtrado = df.filter(pl.col('CIDADE') == cidade)
#     return df_filtrado

@reactive.Calc
def obter_bairros_unicos():
    flag = input.select_tipo_roubo()
    cidade_key = input.select_cidade()
    cidade = {"cd1": "RIBEIRAO PRETO", "cd2": "S.CARLOS"}[cidade_key]

    if flag == "op1":
        df = df_veiculos
    else:
        df = df_celulares
    
    
    df_filtrado = df.filter(pl.col('CIDADE') == cidade)
    # Obter valores únicos da coluna 'category'
    unique_values = df_filtrado.select('BAIRRO').unique().collect().to_series().drop_nans().to_list()
    unique_values = [value for value in unique_values if value and value.strip()]

    # Criar um dicionário de opções para o select input
    options = {value: value for value in unique_values}
    return options

@reactive.effect
def update_bairros():
    bairros = obter_bairros_unicos()
    ui.update_select("select_bairro", choices=bairros)

# Add page title and sidebar
ui.page_opts(title="Segurança pública Roubos/Furtos na cidade de Ribeirão Preto", fillable=True)
with ui.sidebar(open="desktop"):
    ui.input_select("select_cidade", "Escolha uma opção:", {"cd1": "RIBEIRAO PRETO"}),
    ui.input_select("select_tipo_roubo", "Escolha uma opção:", {"op1": "Veículos", "op2": "Celulares"}),
    ui.input_select("select_ano", "Selecione o Ano:", {"an0": "Geral","an1": "2024", "an2": "2023"}),
    ui.input_select("select_bairro", "Selecione o Bairro:", {}),

    ui.input_slider("total_bill", "Bill amount", min=bill_rng[0], max=bill_rng[1], value=bill_rng, pre="$")
    ui.input_checkbox_group("time", "Food service", ["Lunch", "Dinner"], selected=["Lunch", "Dinner"], inline=True)
    ui.input_action_button("reset", "Reset filter")


with ui.layout_columns(col_widths=[6, 6, 12]):

    with ui.card(full_screen=True):
        ui.card_header("Bairros com maior incidência")
        @render.data_frame
        def table():
            return bairros_mais_roubos()

    with ui.card(full_screen=True,min_height="500px"):
        ui.card_header("Mapa de Calor")

        @render.ui
        def plot_heatmap():
            # Criar um mapa centrado em São Carlos (coordenadas fornecidas como exemplo)
            mapa = folium.Map(location=[-21.1767, -47.8208], zoom_start=13)

            df_filtro_map = df_filtro().select(['CIDADE','BAIRRO', 'LATITUDE', 'LONGITUDE']).collect().to_pandas().dropna(subset=['LATITUDE', 'LONGITUDE'])

            mapa.add_child(plugins.HeatMap(df_filtro_map.loc[:, ['LATITUDE', 'LONGITUDE']]))

            return mapa


# --------------------------------------------------------
# Reactive calculations and effects
# --------------------------------------------------------

@reactive.calc
def tips_data():
    bill = input.total_bill()
    idx1 = tips.total_bill.between(bill[0], bill[1])
    idx2 = tips.time.isin(input.time())
    return tips[idx1 & idx2]

@reactive.effect
@reactive.event(input.reset)
def _():
    ui.update_slider("total_bill", value=bill_rng)
    ui.update_checkbox_group("time", selected=["Lunch", "Dinner"])