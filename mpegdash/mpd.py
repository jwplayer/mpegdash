# -*- coding: utf-8 -*-

import mpegdash
import mpegdash.period


class MPD(mpegdash.DASHModel):

    TAG = 'MPD'

    def __init__(self, profiles, min_buffer_time, type=u'static', media_presentation_duration=None):
        super(MPD, self).__init__()
        if min_buffer_time is None or not isinstance(min_buffer_time, int):
            raise TypeError('MPD: minimum buffer time should be an integer')
        self.set_attribute('profiles', profiles)
        self.set_attribute('minBufferTime', min_buffer_time)
        self.set_attribute('type', type)
        self.set_attribute('mediaPresentationDuration', media_presentation_duration)
        self._periods = []

    @property
    def profiles(self):
        if 'profiles' in self._attributes:
            return self._attributes.get('profiles')
        return None

    def periods(self):
        return self._periods

    def append_period(self, period):
        if not isinstance(period, mpegdash.period.Period):
            raise TypeError('MPD: add_period(): invalid period')
        self._periods.append(period)
        self._xml_append_element(period._xml_element)

    def apply_profile_rules(self):
        if self.profiles == 'urn:mpeg:dash:profile:isoff-on-demand:2011':
            self.set_attribute('type', 'static')

    def to_xml(self, xml_declaration=False, encoding='UTF-8', pretty_print=False):
        return super(MPD, self).to_xml(xml_declaration=True, encoding=encoding, pretty_print=pretty_print)

    def _xml_initialize_element(self, tag=None, nsmap=None, attributes=None):
        xml_schema_instance = 'http://www.w3.org/2001/XMLSchema-instance'
        xml_schema_instance_schema_location = 'urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd'
        nsmap = {
            None: 'urn:mpeg:dash:schema:mpd:2011',
            'xsi': xml_schema_instance
        }
        schema_location_attribute_name = '{{{}}}schemaLocation'.format(xml_schema_instance)
        attributes = {
            schema_location_attribute_name: xml_schema_instance_schema_location
        }
        super(MPD, self)._xml_initialize_element(tag, nsmap, attributes)
