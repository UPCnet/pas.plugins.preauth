from zope.interface import Interface


class IPreauthHelper(Interface):
    """Interface for PreauthHelper."""


class IPreauthTask(Interface):
    """Interface for pre auth tasks"""

    def execute(credentials):
        """The method to execute before the user gets authenticated"""
