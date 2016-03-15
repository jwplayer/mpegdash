# -*- coding: utf-8 -*-

from datetime import timedelta

from lxml import etree
import isodate


class Serializer(object):

    pass


class XMLSerializer(Serializer):

    ATTRIBUTES_VALIDATION = {
        'MPD': {
            'profiles': [
                # 'urn:mpeg:dash:profile:full:2011',
                'urn:mpeg:dash:profile:isoff-on-demand:2011',
                # 'urn:mpeg:dash:profile:isoff-live:2011',
                # 'urn:mpeg:dash:profile:isoff-main:2011',
                # 'urn:mpeg:dash:profile:mp2t-main:2011',
                # 'urn:mpeg:dash:profile:mp2t-simple:2011'
            ]
        }
    }

    ATTRIBUTES_TYPES = {
        'MPD': {
            'minBufferTime': 'xs:duration',
            'mediaPresentationDuration': 'xs:duration'
        },
        'Period': {
            'start': 'xs:duration',
            'duration': 'xs:duration'
        },
        'AdaptationSet': {
            'bitstreamSwitching': 'xs:boolean',
            'subsegmentAlignment': 'xs:boolean'
        }
    }

    def __init__(self, tag=None):
        self._xml_initialize_element(tag or self.__class__.TAG)

    def to_xml(self, xml_declaration=False, encoding='UTF-8', pretty_print=False):
        if self._xml_element is not None:
            return etree.tostring(self._xml_element, xml_declaration=xml_declaration, encoding=encoding,
                                  pretty_print=pretty_print)
        raise ValueError('XMLSerializer: to_xml(): element is None')

    def _xml_initialize_element(self, tag=None, nsmap=None, attributes=None):
        if tag is None:
            raise TypeError("XMLSerializer: _xml_initialize_element(): tag can't be None")
        if nsmap is None:
            nsmap = {}
        if attributes is None:
            attributes = {}
        self._xml_element = etree.Element(tag, nsmap=nsmap, attrib=attributes)

    def _xml_append_element(self, element):
        self._xml_element.append(element)

    def _xml_set(self, attribute, value):
        if value is None:
            if attribute in self._xml_element.attrib:
                return self._xml_element.attrib.pop(attribute)
        else:
            if attribute in XMLSerializer.ATTRIBUTES_TYPES.get(self._xml_element.tag, {}):
                if XMLSerializer.ATTRIBUTES_TYPES[self._xml_element.tag][attribute] == 'xs:duration':
                    value = self._xml_to_duration(value)
                elif XMLSerializer.ATTRIBUTES_TYPES[self._xml_element.tag][attribute] == 'xs:boolean':
                    value = self._xml_to_bool(value)
            if attribute in XMLSerializer.ATTRIBUTES_VALIDATION.get(self._xml_element.tag, {}):
                if isinstance(XMLSerializer.ATTRIBUTES_VALIDATION[self._xml_element.tag][attribute], list):
                    if value not in XMLSerializer.ATTRIBUTES_VALIDATION[self._xml_element.tag][attribute]:
                        raise TypeError("{} '{}' attribute: '{}' is invalid".format(self._xml_element.tag, attribute, value))
            if not isinstance(value, basestring):
                value = str(value)
            self._xml_element.set(attribute, value)

    def _xml_to_duration(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError('XMLSerializer: _xml_to_duration(): value is not int')
        return isodate.duration_isoformat(timedelta(seconds=value))

    def _xml_to_bool(self, value):
        if not isinstance(value, bool):
            raise TypeError('XMLSerializer: _xml_to_bool(): value is not bool')
        return 'true' if value else 'false'
