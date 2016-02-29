# -*- coding: utf-8 -*-

from mpegdash import DASHModel


class AdaptationSet(DASHModel):

    TAG = 'AdaptationSet'

    def __init__(self, profile=None, period=None, adaptation_set_id=None):
        super(AdaptationSet, self).__init__(profile=profile)
        self.period = period
        self.adaptation_set_id = adaptation_set_id

    def __lxml__(self):
        super(AdaptationSet, self).__lxml__()
        if self.adaptation_set_id:
            self.element.attrib['id'] = str(self.adaptation_set_id)
        else:
            print '!!!!!!!!'
            print self.element.getparent()
            if self.element.getparent():
                print '1111123131'
                print self.element.getparent().index(self.element)
            else:
                self.element.attrib['id'] = 'x'
        return self

