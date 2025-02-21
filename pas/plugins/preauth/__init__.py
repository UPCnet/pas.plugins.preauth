import logging

from pas.plugins.preauth import install

logger = logging.getLogger(__name__)

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    try:
        install.register_preauth_plugin()  
        install.register_preauth_plugin_class(context) 
        logger.info("PreAuth plugin successfully initialized.")
    except Exception as e:
        logger.error(f"Error initializing PreAuth plugin: {e}")
        raise
