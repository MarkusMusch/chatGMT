"""Chat page layout."""
from typing import Any, Dict, Tuple

import dash  # type: ignore
from dash import callback, Input, no_update, Output, State  # type: ignore
import dash_mantine_components as dmc  # type: ignore

from chatgmt.frontend.components.components_id_tree import ComponentIdTree
from chatgmt.services.llm_service import handle_thread

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


@callback(
        Output(ComponentIdTree.App.ChatIds.OUTPUT, "children"),
        Output(
            ComponentIdTree.App.ChatIds.INPUT,
            "error",
            allow_duplicate=True
        ),
        Output(ComponentIdTree.App.ChatIds.INPUT, "value"),
        Input(ComponentIdTree.App.ChatIds.SEND_BUTTON, "n_clicks"),
        State(ComponentIdTree.App.ChatIds.INPUT, "value"),
        State(ComponentIdTree.App.AppIds.STORE, "data"),
        prevent_initial_call=True,
)
def send_message(
    _: int,
    input: str,
    store_data: Dict[str, str]
) -> Tuple[str | Any, str | None, str]:
    """Send a message to the chat.

    Args:
        _: The number of clicks on the button.
        input: The message to send to the LLM.

    Returns:
        The message to send to the LLM.
    """
    if input:
        output = handle_thread(
            input=input,
            thread_id=store_data["thread_id"],
            assistant_id=store_data["assistant_id"]
        )
        return output, None, ""
    else:
        return no_update, "Please enter a message", ""
