import install

install.register_preauth_plugin()

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    install.register_preauth_plugin_class(context)
