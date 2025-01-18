"""This module contains the service for the LLM chat."""
from openai import OpenAI
from openai.types.beta.threads.text_content_block import TextContentBlock

from chatgmt.settings import settings

client = OpenAI()
thread = client.beta.threads.create()
assistant_id = settings.ASSISTANT_ID


def handle_thread(
    input: str,
) -> str:
    """Handle the chat thread."""

    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=input
    )

    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )

    if run.status == 'completed':
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )

    if isinstance(messages.data[0].content[0], TextContentBlock):
        reply = messages.data[0].content[0].text.value
    else:
        reply = "Error getting reply from LLM."

    return reply
