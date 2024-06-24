import polars as pl
from shiny import input

from InfoVis_MECAI.app.data_processing import df_veiculos, df_celulares

def df_filtro():
    flag = input.select_tipo_roubo()
    flag_ano = input.select_ano()
    cidade_key = input.select_cidade()
    cidade = {"cd1": "RIBEIRAO PRETO", "cd2": "S.CARLOS"}[cidade_key]

    df = df_veiculos if flag == "op1" else df_celulares

    if flag_ano == "an1":
        df = df.filter(pl.col('ANO') == 2024)
    elif flag_ano == "an2":
        df = df.filter(pl.col('ANO') == 2023)

    df_filtrado = df.filter(pl.col('CIDADE') == cidade)
    return df_filtrado

def bairros_mais_roubos():
    df_filtrado = df_filtro()
    result = (df_filtrado.filter(pl.col("BAIRRO").is_not_null())
              .group_by('BAIRRO')
              .agg(pl.count().alias("# Ocorrências"))
              .sort("# Ocorrências", descending=True)
              .limit(5))
    return result.collect()

def obter_bairros_unicos():
    df_filtrado = df_filtro()
    unique_values = df_filtrado.select('BAIRRO').unique().collect().to_series().drop_nans().to_list()
    unique_values = [value for value in unique_values if value and value.strip()]
    options = {value: value for value in unique_values}
    return options

def tips_data():
    from shiny import input
    tips = px.data.tips()
    bill = input.total_bill()
    idx1 = tips.total_bill.between(bill[0], bill[1])
    idx2 = tips.time.isin(input.time())
    return tips[idx1 & idx2]
