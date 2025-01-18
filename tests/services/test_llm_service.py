from unittest.mock import MagicMock, patch

from chatgmt.services.llm_service import handle_thread


def test_handle_thread():
    with patch("chatgmt.services.llm_service.handle_assistants") \
            as mock_handle_assistants:
        with patch("chatgmt.services.llm_service.extract_reply") \
                as mock_extract_reply:
            mock_reply_handle_assistants = MagicMock()
            mock_reply_extract_reply = MagicMock()

            mock_handle_assistants.return_value = mock_reply_handle_assistants
            mock_extract_reply.return_value = mock_reply_extract_reply

            reply = handle_thread("Hello, World!")

            mock_handle_assistants.assert_called_once_with("Hello, World!")
            mock_extract_reply.assert_called_once_with(
                mock_reply_handle_assistants
            )
            assert reply == mock_reply_extract_reply
