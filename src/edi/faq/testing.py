# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import edi.faq


class EdiFaqLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=edi.faq)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'edi.faq:default')


EDI_FAQ_FIXTURE = EdiFaqLayer()


EDI_FAQ_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDI_FAQ_FIXTURE,),
    name='EdiFaqLayer:IntegrationTesting',
)


EDI_FAQ_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDI_FAQ_FIXTURE,),
    name='EdiFaqLayer:FunctionalTesting',
)


EDI_FAQ_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EDI_FAQ_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='EdiFaqLayer:AcceptanceTesting',
)
