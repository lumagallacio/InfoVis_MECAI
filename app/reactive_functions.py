import polars as pl
import plotly.express as px
from shiny import reactive, render, ui
from shinywidgets import render_plotly
import folium
from folium import plugins

def setup_reactive_functions(input, output, session, df_veiculos, df_celulares, tips, bill_rng):

    @reactive.Calc
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

        return df.filter(pl.col('CIDADE') == cidade)

    @reactive.Calc
    def obter_bairros_unicos():
        df = df_filtro()
        unique_values = df.select('BAIRRO').unique().collect().to_series().drop_nans().to_list()
        options = {value: value for value in unique_values if value and value.strip()}
        return options

    @reactive.effect
    def update_bairros():
        bairros = obter_bairros_unicos()
        ui.update_select("select_bairro", choices=bairros)

    def bairros_mais_roubos():
        df_filtrado = df_filtro()
        result = (df_filtrado.filter(pl.col("BAIRRO").is_not_null())
                  .group_by('BAIRRO')
                  .agg(pl.count().alias("# Ocorrências"))
                  .sort("# Ocorrências", descending=True)
                  .limit(5))
        return result.collect()

    @render.data_frame
    def table():
        return bairros_mais_roubos()

    @render_plotly
    def scatterplot():
        color = input.scatter_color()
        return px.scatter(
            tips_data(),
            x="total_bill",
            y="tip",
            color=None if color == "none" else color,
            trendline="lowess"
        )

    @render.ui
    def plot_heatmap():
        mapa = folium.Map(location=[-21.1767, -47.8208], zoom_start=13)
        df_filtro_map = df_filtro().select(['CIDADE', 'BAIRRO', 'LATITUDE', 'LONGITUDE']).collect().to_pandas().dropna(subset=['LATITUDE', 'LONGITUDE'])
        mapa.add_child(plugins.HeatMap(df_filtro_map.loc[:, ['LATITUDE', 'LONGITUDE']]))
        return mapa

    @reactive.calc
    def tips_data():
        bill = input.total_bill()
        idx1 = tips.total_bill.between(bill[0], bill[1])
        idx2 = tips.time.isin(input.time())
        return tips[idx1 & idx2]

    @render.text
    def total_tippers():
        return tips_data().shape[0]

    @render.text
    def average_tip():
        d = tips_data()
        if d.shape[0] > 0:
            perc = d.tip / d.total_bill
            return f"{perc.mean():.1%}"

    @render.text
    def average_bill():
        d = tips_data()
        if d.shape[0] > 0:
            bill = d.total_bill.mean()
            return f"${bill:.2f}"

    @reactive.effect
    @reactive.event(input.reset)
    def _():
        ui.update_slider("total_bill", value=bill_rng)
        ui.update_checkbox_group("time", selected=["Lunch", "Dinner"])

    # Assign output functions
    output.table = table
    output.scatterplot = scatterplot
    output.plot_heatmap = plot_heatmap
    output.total_tippers = total_tippers
    output.average_tip = average_tip
    output.average_bill = average_bill
