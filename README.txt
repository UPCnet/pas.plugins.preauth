Introduction
============

This Plone PAS plugin allows to insert a custom method during the authentication flow is happening. It's in fact a fake IAuthenticationPlugin that does no authentication at all. This is intentionally made to make available the user credentials to our custom method. The pluggin is pluggable itself through the ZCA.

Installation
============

You can install the plugin as any other Plone product via "Add or remove products" configlet in Plone Control Panel. This will create a new plugin in acl_users and it will set it as the most preferential authentication plugin.

Usage
=====

You can set a custom task in your own product by creating an adapter of IPreauthHelper for the IPreauthTask interface, for example::

    class oauthTokenRetriever(object):
        implements(IPreauthTask)
        adapts(IPreauthHelper)

        def __init__(self, context):
            self.context = context

        def execute(self, credentials):
            ## Actually retrieve the token

The execute method should contain your custom code.

Don't forget to register it in zcml::

    <adapter
      name="oauthtokenretriever"
      factory=".oauth2.oauthTokenRetriever" />
