from time import sleep

import pandas as pd
from shiny import App, Inputs, Outputs, Session, render, ui

app_ui = ui.page_fluid(ui.p("Hello world"), ui.output_data_frame("my_data"))


def load_data() -> pd.DataFrame:
    sleep(6)
    return pd.DataFrame({"x": [1, 2, 3], "y": ["a", "b", "c"]})


def server(input: Inputs, output: Outputs, session: Session):
    print("Loading data...")
    notification_id = ui.notification_show("Loading data", duration=None)
    df = load_data()
    print("Loading data complete!")
    ui.notification_remove(notification_id)

    @output
    @render.data_frame
    def my_data():
        return render.DataGrid(df)


app = App(app_ui, server)
