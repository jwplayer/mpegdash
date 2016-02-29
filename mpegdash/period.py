# -*- coding: utf-8 -*-

import datetime

import isodate

import mpegdash
import mpegdash.adaptation_set


def set_id(period):
    if period.period_id is not None:
        period.element.attrib['id'] = period.period_id


def set_start(period):
    if period.start is not None:
        period.element.attrib['start'] = isodate.duration_isoformat(datetime.timedelta(seconds=period.start))


def set_duration(period):
    if period.duration is not None:
        period.element.attrib['duration'] = isodate.duration_isoformat(datetime.timedelta(seconds=period.duration))


class Period(mpegdash.DASHModel):

    TAG = 'Period'
    
    PROFILE_RULES = {
        None: [
            set_id,
            set_start,
            set_duration
        ]
    }

    def __init__(self, profile=None, mpd=None, period_id='0', start=None, duration=None):
        super(Period, self).__init__(profile=profile)
        self.period_id = period_id
        self.start = start or 0
        self.duration = duration
        # relationships
        self.mpd = mpd
        self._adaptation_sets = []

    def adaptation_sets(self):
        return self._adaptation_sets

    def add_adaptation_set(self, adaptation_set):
        if not isinstance(adaptation_set, mpegdash.adaptation_set.AdaptationSet):
            raise TypeError('Period.add_adaptation_set: invalid adaptation set')
        self._adaptation_sets.append(adaptation_set)
        self.__lxml__()

    def __lxml__(self):
        super(Period, self).__lxml__()
        # print 'PERIODLXMLX'
        # print self.adaptation_sets()[0].__lxml__().element
        [self.element.append(adaptation_set.__lxml__().element) for adaptation_set in self.adaptation_sets()]
        return self
