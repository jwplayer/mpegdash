# -*- coding: utf-8 -*-

from datetime import timedelta
import datetime

from lxml import etree
import isodate


class MediaPresentationDescription(object):

    TAG = 'MPD'

    MPD_XML_NAMESPACE = 'urn:mpeg:DASH:schema:MPD:2011'
    XML_SCHEMA_INSTANCE = 'http://www.w3.org/2001/XMLSchema-instance'
    XML_SCHEMA_INSTANCE_SCHEMA_LOCATION = 'urn:mpeg:DASH:schema:MPD:2011 DASH-MPD.xsd'

    AVAILABLE_DASH_PROFILES = [
        'urn:mpeg:dash:profile:full:2011',
        'urn:mpeg:dash:profile:isoff-on-demand:2011',
        'urn:mpeg:dash:profile:isoff-live:2011',
        'urn:mpeg:dash:profile:isoff-main:2011',
        'urn:mpeg:dash:profile:mp2t-main:2011',
        'urn:mpeg:dash:profile:mp2t-simple:2011',
        'urn:3GPP:PSS:profile:DASH10'
    ]

    def __init__(self, profile=None, minimum_buffer_time=None):
        if profile is None or not isinstance(profile, basestring) or \
                        profile not in MediaPresentationDescription.AVAILABLE_DASH_PROFILES:
            raise TypeError("MediaPresentationDescription: the '{}' DASH profile is not available".format(profile))
        if minimum_buffer_time is None or not isinstance(minimum_buffer_time, int):
            raise TypeError('MediaPresentationDescription: minimum buffer time should be an integer')
        self.profile = profile
        self.minimum_buffer_time = minimum_buffer_time
        self.duration = None
        self._periods = []
        self.__init_element()

    def periods(self):
        return self._periods

    def is_live_profile(self):
        return self.profile == 'urn:mpeg:dash:profile:isoff-live:2011'

    def is_on_demand_profile(self):
        return self.profile == 'urn:mpeg:dash:profile:isoff-on-demand:2011'

    def set_duration(self, seconds=None):
        if seconds is None:
            raise TypeError('MediaPresentationDescription.set_duration: invalid seconds value')
        self.duration = seconds

    def add_period(self, period):
        if not isinstance(period, Period):
            raise TypeError('MediaPresentationDescription.add_period: invalid period')
        self._periods.append(period)

    def to_xml(self, encoding='UTF-8'):
        return unicode(self.__str__(encoding))

    def __init_element(self):
        min_buffer_duration = timedelta(seconds=self.minimum_buffer_time)
        schema_location_attrib = '{{{}}}schemaLocation'.format(MediaPresentationDescription.XML_SCHEMA_INSTANCE)
        attributes = {
            schema_location_attrib: MediaPresentationDescription.XML_SCHEMA_INSTANCE_SCHEMA_LOCATION,
            'profiles': self.profile,
            'minBufferTime': isodate.duration_isoformat(min_buffer_duration)
        }
        self.__element = etree.Element(self.__class__.TAG,
                                       nsmap={
                                           None: MediaPresentationDescription.MPD_XML_NAMESPACE,
                                           'xsi': MediaPresentationDescription.XML_SCHEMA_INSTANCE
                                       },
                                       attrib=attributes)
        [self.__element.append(period.element()) for period in self.periods()]

    def element(self):
        self.__update_element()
        return self.__element

    def __update_element(self):
        if self.is_on_demand_profile() and self.__element.attrib.get('type') != 'static':
            self.__element.attrib['type'] = 'static'
        if self.is_live_profile() and self.__element.attrib.get('type') != 'dynamic':
            self.__element.attrib['type'] = 'dynamic'
        if self.duration:
            duration = isodate.duration_isoformat(timedelta(seconds=self.duration))
            self.__element.attrib['mediaPresentationDuration'] = duration
        [self.__element.append(period.element()) for period in self.periods()]

    def __str__(self, encoding='UTF-8'):
        return etree.tostring(self.element(), xml_declaration=True, encoding=encoding)


class Period(object):

    TAG = 'Period'

    def __init__(self, period_id='0', start=None, duration=None):
        self.__init_element()
        self.period_id = period_id
        self.start = start or 0
        self.duration = duration

    def element(self):
        self.__update_element()
        return self.__element

    def __init_element(self):
        self.__element = etree.Element(self.__class__.TAG)

    def __update_element(self):
        self.__element.attrib['id'] = self.period_id
        self.__element.attrib['start'] = isodate.duration_isoformat(datetime.timedelta(seconds=self.start))
        self.__element.attrib['duration'] = isodate.duration_isoformat(datetime.timedelta(seconds=self.duration))
