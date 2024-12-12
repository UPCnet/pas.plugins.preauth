Introduction
============

This Plone PAS plugin allows you to insert a custom method during the authentication flow. It is, in fact, a fake IAuthenticationPlugin that does no authentication at all. This is intentionally made to make user credentials available to your custom method. The plugin is pluggable itself through the ZCA (Zope Component Architecture).

Installation
============

You can install the plugin as any other Plone product via the "Add or remove products" configlet in the Plone Control Panel. This will create a new plugin in `acl_users` and it will set it as the most preferential authentication plugin.

Usage
=====

You can set a custom task in your own product by creating an adapter for the `IPreauthHelper` interface that adapts to the `IPreauthTask` interface. For example:

```python
from zope.interface import implementer
from zope.component import adapts
from pas.plugins.preauth.interfaces import IPreauthTask, IPreauthHelper

@implementer(IPreauthTask)  
@adapts(IPreauthHelper)    
class oauthTokenRetriever:
    """Custom task to retrieve a token in the authentication flow"""

    def __init__(self, context):
        self.context = context

    def execute(self, credentials):
        """Method to retrieve the token using the user's credentials"""
        # Implement your actual token retrieval logic here
        token = self.retrieve_token(credentials['login'], credentials['password'])
        return token

    def retrieve_token(self, username, password):
        """Logic to retrieve the token (can be an external API call or custom logic)"""
        # Example of simulating a token retrieval
        if username == 'testuser' and password == 'testpass':
            return 'fake-token-123456'  # Simulated token
        return None
