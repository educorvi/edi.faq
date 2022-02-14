# -*- coding: utf-8 -*-
from edi.faq.content.answer import IAnswer  # NOQA E501
from edi.faq.testing import EDI_FAQ_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class AnswerIntegrationTest(unittest.TestCase):

    layer = EDI_FAQ_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Question',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_answer_schema(self):
        fti = queryUtility(IDexterityFTI, name='Answer')
        schema = fti.lookupSchema()
        self.assertEqual(IAnswer, schema)

    def test_ct_answer_fti(self):
        fti = queryUtility(IDexterityFTI, name='Answer')
        self.assertTrue(fti)

    def test_ct_answer_factory(self):
        fti = queryUtility(IDexterityFTI, name='Answer')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IAnswer.providedBy(obj),
            u'IAnswer not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_answer_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Answer',
            id='answer',
        )

        self.assertTrue(
            IAnswer.providedBy(obj),
            u'IAnswer not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('answer', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('answer', parent.objectIds())

    def test_ct_answer_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Answer')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
