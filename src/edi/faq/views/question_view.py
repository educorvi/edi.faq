# -*- coding: utf-8 -*-

from edi.faq import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class QuestionView(BrowserView):

    def __call__(self):
        brains = self.context.getFolderContents()
        contents = []
        for i in brains:
            entry = {}
            obj = i.getObject()
            entry['title'] = obj.title
            entry['text'] = ''
            if obj.text:
                entry['text'] = obj.text.output
            contents.append(entry)
        self.contents = contents    
        return self.index()
