from dash import no_update

from chatgmt.frontend.pages.callbacks_chat_page import send_message


def test_send_message_with_input():
    # Simulate a button click with non-empty input
    n_clicks = 1
    input_value = "Hello, World!"
    expected_output = (input_value, None, "")
    
    result = send_message(n_clicks, input_value)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_send_message_without_input():
    # Simulate a button click with empty input
    n_clicks = 1
    input_value = ""
    expected_output = (no_update, "Please enter a message", "")
    
    result = send_message(n_clicks, input_value)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
