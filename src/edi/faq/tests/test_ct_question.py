# -*- coding: utf-8 -*-
from edi.faq.content.question import IQuestion  # NOQA E501
from edi.faq.testing import EDI_FAQ_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class QuestionIntegrationTest(unittest.TestCase):

    layer = EDI_FAQ_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_question_schema(self):
        fti = queryUtility(IDexterityFTI, name='Question')
        schema = fti.lookupSchema()
        self.assertEqual(IQuestion, schema)

    def test_ct_question_fti(self):
        fti = queryUtility(IDexterityFTI, name='Question')
        self.assertTrue(fti)

    def test_ct_question_factory(self):
        fti = queryUtility(IDexterityFTI, name='Question')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IQuestion.providedBy(obj),
            u'IQuestion not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_question_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Question',
            id='question',
        )

        self.assertTrue(
            IQuestion.providedBy(obj),
            u'IQuestion not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('question', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('question', parent.objectIds())

    def test_ct_question_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Question')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_question_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Question')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'question_id',
            title='Question container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
