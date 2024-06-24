import polars as pl
from pathlib import Path
import plotly.express as px

def load_data():
    tips = px.data.tips()
    bill_rng = (min(tips.total_bill), max(tips.total_bill))

    caminho_bases = Path(r'/media/luma/hd1t3/Mestrado/Disciplinas/InfoVis/InfoVis_MECAI/data')
    caminho_base_veiculos_csv = caminho_bases.joinpath("VeiculosSubtraidos_2023_2024.csv")
    caminho_base_celulares_csv = caminho_bases.joinpath("CelularesSubtraidos_2023_2024_UTF8.csv")
    valores_na = ["NULL", "NA", "N/A", "NaN"]

    df_veiculos = pl.scan_csv(caminho_base_veiculos_csv, has_header=True, separator=";", low_memory=True, infer_schema_length=1000, null_values=valores_na)
    df_celulares = pl.scan_csv(caminho_base_celulares_csv, has_header=True, separator=";", low_memory=True, infer_schema_length=1000, null_values=valores_na)

    return df_veiculos, df_celulares, tips, bill_rng
