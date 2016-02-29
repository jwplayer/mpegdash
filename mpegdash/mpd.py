# -*- coding: utf-8 -*-

from datetime import timedelta

from lxml import etree
import isodate

import mpegdash
import mpegdash.period


def set_duration(self):
    if self.duration:
        duration = isodate.duration_isoformat(timedelta(seconds=self.duration))
        self.element.attrib['mediaPresentationDuration'] = duration


def force_static_type(self):
    self.element.attrib['type'] = 'static'


def force_dynamic_type(self):
    self.element.attrib['type'] = 'dynamic'


class MPD(mpegdash.DASHModel):

    TAG = 'MPD'

    MPD_XML_NAMESPACE = 'urn:mpeg:DASH:schema:MPD:2011'
    XML_SCHEMA_INSTANCE = 'http://www.w3.org/2001/XMLSchema-instance'
    XML_SCHEMA_INSTANCE_SCHEMA_LOCATION = 'urn:mpeg:DASH:schema:MPD:2011 DASH-MPD.xsd'

    PROFILE_RULES = {
        None: [
            set_duration
        ],
        'urn:mpeg:dash:profile:isoff-on-demand:2011': [
            force_static_type
        ],
        'urn:mpeg:dash:profile:isoff-live:2011': [
            force_dynamic_type
        ]
    }

    def __init__(self, profile=None, minimum_buffer_time=None, duration=None):
        super(MPD, self).__init__(profile=profile)
        if minimum_buffer_time is None or not isinstance(minimum_buffer_time, int):
            raise TypeError('MPD: minimum buffer time should be an integer')
        self.minimum_buffer_time = minimum_buffer_time
        self.duration = duration
        self._periods = []

    def periods(self):
        return self._periods

    def set_duration(self, seconds=None):
        if seconds is None:
            raise TypeError('MPD.set_duration: invalid seconds value')
        self.duration = seconds

    def add_period(self, period):
        if not isinstance(period, mpegdash.period.Period):
            raise TypeError('MPD.add_period: invalid period')
        self._periods.append(period)

    def __lxml__(self):
        if self.element is None:
            min_buffer_duration = timedelta(seconds=self.minimum_buffer_time)
            schema_location_attrib = '{{{}}}schemaLocation'.format(MPD.XML_SCHEMA_INSTANCE)
            attributes = {
                schema_location_attrib: MPD.XML_SCHEMA_INSTANCE_SCHEMA_LOCATION,
                'profiles': self.profile,
                'minBufferTime': isodate.duration_isoformat(min_buffer_duration)
            }
            nsmap = {
                None: MPD.MPD_XML_NAMESPACE,
                'xsi': MPD.XML_SCHEMA_INSTANCE
            }
            self.element = etree.Element(self.__class__.TAG, nsmap=nsmap, attrib=attributes)
            [self.element.append(period.__lxml__().element) for period in self.periods()]
        return super(MPD, self).__lxml__()
