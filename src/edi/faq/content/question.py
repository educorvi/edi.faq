# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


from edi.faq import _


class IQuestion(model.Schema):
    """ Marker interface and Dexterity Python Schema for Question
    """

    details = RichText(title="Details zur Fragestellung", required=False)


@implementer(IQuestion)
class Question(Container):
    """
    """
