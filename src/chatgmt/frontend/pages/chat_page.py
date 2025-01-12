"""Chat page layout."""
import dash  # type: ignore
import dash_mantine_components as dmc  # type: ignore

from chatgmt.frontend.components.components_id_tree import ComponentIdTree
from chatgmt.frontend.pages.callbacks_chat_page import *  # noqa: F401, F403

dash.register_page(__name__)

layout = dmc.Box(
    children=[
        dmc.Card(
            shadow="md",
            h="500px",
            children=[
                dmc.Text(
                    id=ComponentIdTree.App.ChatIds.OUTPUT,
                    children=[
                        "This is where the output will appear"
                    ]
                )
            ]
        ),
        dmc.Textarea(
            id=ComponentIdTree.App.ChatIds.INPUT,
            label="Input",
            value="",
            placeholder="Type your message here",
            m="md"
        ),
        dmc.Button(
            id=ComponentIdTree.App.ChatIds.SEND_BUTTON,
            children=["Send"],
        )
    ]
)
