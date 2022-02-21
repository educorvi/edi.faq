# -*- coding: utf-8 -*-
from datetime import datetime
from plone import api as ploneapi
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer

from edi.faq import _

def create_title():
    now = datetime.now().strftime("%d.%m.%Y")
    user = ''
    if not ploneapi.user.is_anonymous():
        import pdb;pdb.set_trace()
        user = ploneapi.user.get_current().getProperty('fullname')
    title = f"Antwort von {user} vom {now}"
    return title
    

class IAnswer(model.Schema):
    """ Marker interface and Dexterity Python Schema for Answer
    """

    directives.mode(title='display')
    title = schema.TextLine(title="Kopfzeile der Antwort (Name und Datum)",
            defaultFactory = create_title)

    text = RichText(title="Antworttext zur Fragestellung", required=True)


@implementer(IAnswer)
class Answer(Container):
    """
    """
