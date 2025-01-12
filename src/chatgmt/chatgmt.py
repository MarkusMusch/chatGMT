""" This module contains the main app """
import importlib.resources

from dash import (  # type: ignore
    Dash,
    _dash_renderer,
    page_container
)
import dash_mantine_components as dmc  # type: ignore

# This module is not used explicitly but is imported to register the callbacks
from chatgmt.settings import settings
from chatgmt.frontend.components.components_id_tree import ComponentIdTree

_dash_renderer._set_react_version("18.2.0")

asset_folder = importlib.resources.files('chatgmt') / settings.ASSET_FOLDER
pages_folder = importlib.resources.files('chatgmt') / settings.PAGES_FOLDER

app = Dash(
    name="chatGMT",
    title="chatGMT",
    assets_folder=asset_folder,
    pages_folder=pages_folder,
    use_pages=True
)


app.layout = dmc.MantineProvider(
    id=ComponentIdTree.App.AppIds.MANTINE_PROVIDER,
    theme={
        "colorScheme": "light",
    },
    children=[
        dmc.AppShell(
            header={"height": 70},
            p="md",
            m="md",
            children=[
                dmc.AppShellHeader(
                    children=[
                        dmc.Grid(
                            justify="flex-start",
                            children=[
                                dmc.Image(
                                    style={
                                        'maxHeight': '100%',
                                        'objectFit': 'contain',
                                        'height': '100%',
                                        'width': 'auto'
                                    },
                                    m="xs",
                                    p="xs",
                                    h=70,
                                    # src=app.get_asset_url(settings.LOGO_FILE),
                                )
                            ]
                        )
                    ]
                ),
                dmc.AppShellMain(
                    ml=200,
                    children=[
                        page_container
                    ]
                ),
                dmc.AppShellFooter(
                    p=4,
                    px=8,
                    children=[
                        dmc.Group(
                            justify="flex-end",
                            children=[
                                dmc.Text(
                                    size="xs",
                                    children=settings.FOOTER_TEXT
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)
