# -*- coding: utf-8 -*-

import mpegdash
import mpegdash.adaptation_set


class Period(mpegdash.DASHModel):

    TAG = 'Period'
    
    def __init__(self, id='0', start=None, duration=None):
        super(Period, self).__init__()
        self.set_attribute('id', id)
        self.set_attribute('start', start or 0)
        self.set_attribute('duration', duration)
        self._adaptation_sets = []

    def adaptation_sets(self):
        return self._adaptation_sets

    def append_adaptation_set(self, adaptation_set):
        if not isinstance(adaptation_set, mpegdash.adaptation_set.AdaptationSet):
            raise TypeError('Period: add_adaptation_set(): invalid adaptation set')
        self._adaptation_sets.append(adaptation_set)
        self._xml_append_element(adaptation_set._xml_element)
