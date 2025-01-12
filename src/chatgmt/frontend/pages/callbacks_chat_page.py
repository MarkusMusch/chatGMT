"""This module contains the callbacks for the chat page."""
from dash import callback, Input, no_update, Output, State  # type: ignore
from typing import Any, Tuple

from chatgmt.frontend.components.components_id_tree import ComponentIdTree


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
        prevent_initial_call=True,
)
def send_message(
    _: int,
    input: str
) -> Tuple[str | Any, str | None, str]:
    """Send a message to the chat.

    Args:
        _: The number of clicks on the button.
        input: The message to send to the LLM.

    Returns:
        The message to send to the LLM.
    """
    if input:
        return input, None, ""
    else:
        return no_update, "Please enter a message", ""
