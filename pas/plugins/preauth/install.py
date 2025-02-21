from AccessControl.Permissions import manage_users
from pas.plugins.preauth import plugin
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.PluggableAuthService import registerMultiPlugin

manage_add_preauth_form = PageTemplateFile('browser/add_plugin',
                                           globals(), __name__='manage_add_preauth_form')


def manage_add_preauth_helper(dispatcher, id, title=None, REQUEST=None):
    """Add a preauth Helper to the PluggableAuthentication Service."""

    sp = plugin.PreauthHelper(id, title)
    dispatcher._setObject(sp.getId(), sp)

    if REQUEST is not None:
        REQUEST['RESPONSE'].redirect(
            '%s/manage_workspace?manage_tabs_message=preauthHelper+added.' % dispatcher.absolute_url()
        )


def register_preauth_plugin():
    try:
        registerMultiPlugin(plugin.PreauthHelper.meta_type)
    except RuntimeError:
        pass


def register_preauth_plugin_class(context):
    context.registerClass(
        plugin.PreauthHelper,
        permission=manage_users,
        constructors=(manage_add_preauth_form, manage_add_preauth_helper),
        visibility=None,
        icon='browser/icon.gif'
    )
