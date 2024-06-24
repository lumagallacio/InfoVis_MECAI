from shiny import ui
import faicons as fa

def create_ui(bill_rng):
    ICONS = {
        "user": fa.icon_svg("user", "regular"),
        "wallet": fa.icon_svg("wallet"),
        "currency-dollar": fa.icon_svg("dollar-sign"),
        "gear": fa.icon_svg("gear")
    }

    return ui.page_fluid(
        ui.panel_title("Segurança pública Roubos/Furtos na cidade de Ribeirão Preto"),
        ui.sidebar(
            ui.input_select("select_cidade", "Escolha uma opção:", {"cd1": "RIBEIRAO PRETO", "cd2": "S.CARLOS"}),
            ui.input_select("select_tipo_roubo", "Escolha uma opção:", {"op1": "Veículos", "op2": "Celulares"}),
            ui.input_select("select_ano", "Selecione o Ano:", {"an0": "Geral", "an1": "2024", "an2": "2023"}),
            ui.input_select("select_bairro", "Selecione o Bairro:", {}),
            ui.input_slider("total_bill", "Bill amount", min=bill_rng[0], max=bill_rng[1], value=bill_rng, pre="$"),
            ui.input_checkbox_group("time", "Food service", ["Lunch", "Dinner"], selected=["Lunch", "Dinner"], inline=True),
            ui.input_action_button("reset", "Reset filter")
        ),
        ui.layout_columns(
            fill=False,
            ui.value_box("Total tippers", showcase=ICONS["user"], value=ui.output_text("total_tippers")),
            ui.value_box("Average tip", showcase=ICONS["wallet"], value=ui.output_text("average_tip")),
            ui.value_box("Average bill", showcase=ICONS["currency-dollar"], value=ui.output_text("average_bill"))
        ),
        ui.layout_columns(
            col_widths=[6, 6, 12],
            ui.card(
                full_screen=True,
                ui.card_header("Bairros com maior incidência"),
                ui.output_data_frame("table")
            ),
            ui.card(
                full_screen=True,
                ui.card_header(
                    ui.div(
                        "Total bill vs tip",
                        ui.popover(
                            title="Add a color variable",
                            placement="top",
                            ICONS["gear"],
                            ui.input_radio_buttons(
                                "scatter_color", None,
                                ["none", "sex", "smoker", "day", "time"],
                                inline=True
                            )
                        )
                    )
                ),
                ui.output_plotly("scatterplot")
            ),
            ui.card(
                full_screen=True,
                min_height="500px",
                ui.card_header("Mapa de Calor"),
                ui.output_ui("plot_heatmap")
            )
        )
    )
