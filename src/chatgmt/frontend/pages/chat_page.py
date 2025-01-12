import dash  # type: ignore
import dash_mantine_components as dmc  # type: ignore

dash.register_page(__name__, path="/")


layout = dmc.Box(
    dmc.Text("Here you can chat with large language models")
)
