import unittest
from plone.testing import IntegrationTesting
from pas.plugins.preauth import testing
from pas.plugins.preauth.plugin import PreauthHelper
from plone.app.testing import login, TEST_USER_NAME, TEST_USER_PASSWORD
from plone.app.testing import setRoles
from plone.testing.z2 import Browser
from zope.component import getUtility
from plone.app.testing import PLONE_FIXTURE 
from Products.CMFCore.utils import getToolByName

MY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_FIXTURE,),  
    name="MyIntegrationTestingLayer"
)

class TestPreauthPluginSetup(unittest.TestCase):
    """Test the PreauthHelper plugin installation and setup"""

    layer = MY_INTEGRATION_TESTING  

    def setUp(self):
        """Set up the necessary data and environment"""
        self.portal = self.layer['portal']
        self.acl_users_url = f"{self.portal.absolute_url()}/acl_users"
        self.browser = Browser(self.layer['app'])
        login(self.portal, TEST_USER_NAME)

    def test_plugin_is_installed(self):
        """Test that the PreauthHelper plugin is in the list of available plugins"""
        self.browser.open(f"{self.acl_users_url}/manage_main")
        
        # Find the form to add a new plugin
        form = self.browser.getForm(index=0)
        select = form.getControl(name=':action')

        # Check that 'Preauth Helper' is listed among installable plugins
        self.assertIn('Preauth Helper', select.displayOptions)

    def test_add_plugin(self):
        """Test that we can add the PreauthHelper plugin to acl_users"""
        self.browser.open(f"{self.acl_users_url}/manage_main")
        form = self.browser.getForm(index=0)
        select = form.getControl(name=':action')

        # Select the 'Preauth Helper' plugin
        select.getControl('Preauth Helper').click()
        self.assertEqual(select.displayValue, ['Preauth Helper'])
        self.assertEqual(select.value, ['manage_addProduct/pas.plugins.preauth/manage_add_preauth_helper_form'])

        # Add the 'Preauth Helper' plugin to acl_users
        self.browser.getForm(name='manage_add_preauth_helper_form').submit()

        # Ensure the plugin was added
        acl_users = getToolByName(self.portal, 'acl_users')
        self.assertIn('preauth_helper', acl_users.objectIds())  

    def test_preauth_helper_functionality(self):
        """Test that PreauthHelper works after installation"""
        # Manually add the PreauthHelper plugin instance
        myhelper = PreauthHelper('preauth_helper', 'Preauth Helper')
        self.portal.acl_users['preauth_helper'] = myhelper

        # Test the plugin functionality
        # Example test: Check if the plugin can handle credentials
        credentials = {'login': 'testuser', 'password': 'testpass'}
        result = myhelper.authenticateCredentials(credentials)

        # Check the expected behavior after authentication
        self.assertEqual(result, None)  

    def tearDown(self):
        """Cleanup after tests"""
        logout()

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromTestCase(TestPreauthPluginSetup)
