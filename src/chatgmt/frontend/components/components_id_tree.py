"""
This module holds the id tree for the components in the Zugvogel dashboard.
"""
from enum import Enum


class ComponentIdTree():

    class App():

        class AppIds(str, Enum):
            """ This class contains the ids of the app """
            MANTINE_PROVIDER = 'mantine-provider'
