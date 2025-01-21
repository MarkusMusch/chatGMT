"""This module contains the service for the LLM chat."""
from openai import OpenAI
from openai.pagination import SyncCursorPage
from openai.types.beta.threads.message import Message
from openai.types.beta.threads.text_content_block import TextContentBlock

client = OpenAI()


def extract_reply(messages: SyncCursorPage[Message]) -> str:
    """Extract the reply from the messages.

    Args:
        messages (list): The list of messages.

    Returns:
        str: The reply message.
    """
    if isinstance(messages.data[0].content[0], TextContentBlock):  # type: ignore
        reply = messages.data[0].content[0].text.value  # type: ignore
    else:
        reply = "Error getting reply from LLM."

    return reply


def handle_assistants(
    input: str,
    thread_id: str,
    assistant_id: str
) -> SyncCursorPage[Message]:
    """Handle the assistants.

    Args:
        input (str): The input message.
        thread_id (str): The thread id.
        assistant_id (str): The assistant id.

    Returns:
        SyncCursorPage[Message]: The messages.
    """
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=input
    )

    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )

    if run.status == 'completed':
        messages = client.beta.threads.messages.list(
            thread_id=thread_id
        )

    return messages


def handle_thread(
    input: str,
    thread_id: str,
    assistant_id: str
) -> str:
    """Handle the chat thread.

    Args:
        input (str): The input message.
        thread_id (str): The thread id.
        assistant_id (str): The assistant id.

    Returns:
        str: The reply message.
    """
    try:
        messages = handle_assistants(
            input,
            thread_id,
            assistant_id
        )
        reply = extract_reply(messages)

    except Exception as e:
        reply = f"An unexpected error occurred: {e}"

    return reply
