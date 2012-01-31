import unittest

from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
ptc.setupPloneSite()

import pas.plugins.preauth

class TestCase(ptc.PloneTestCase):
    class layer(PloneSite):
        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            zcml.load_config('configure.zcml',
                             pas.plugins.preauth)
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            pass


def test_suite():
    return unittest.TestSuite([

        ztc.FunctionalDocFileSuite(
            'README.txt', package='pas.plugins.preauth',
            test_class=TestCase),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')

