"""
This module holds the id tree for the components in the Zugvogel dashboard.
"""
from enum import Enum


class ComponentIdTree():

    class App():

        class AppIds(str, Enum):
            """ This class contains the ids of the app """
            MANTINE_PROVIDER = 'mantine-provider'

        class ChatIds(str, Enum):
            """ This class contains the ids of the chat component """
            INPUT = 'chat-input'
            OUTPUT = 'chat-output'
            SEND_BUTTON = 'chat-button'
