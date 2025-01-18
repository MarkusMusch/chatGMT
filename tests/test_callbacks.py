from dash import no_update  # type: ignore
import pytest
from unittest.mock import patch

from chatgmt.frontend.pages.callbacks_chat_page import send_message


@pytest.mark.parametrize(
    "n_clicks, input_value, expected_output, mock_return",
    [
        (1, "Hello, World!", ("Hello, World!", None, ""), "Hello, World!"),
        (1, "", (no_update, "Please enter a message", ""), None)
    ]
)
def test_send_message(n_clicks, input_value, expected_output, mock_return):
    if mock_return is not None:
        with patch("chatgmt.frontend.pages.callbacks_chat_page.handle_thread")\
                as handle_thread:

            handle_thread.return_value = mock_return
            result = send_message(n_clicks, input_value)
    else:
        result = send_message(n_clicks, input_value)

    assert result == expected_output, \
        f"Expected {expected_output}, but got {result}"
