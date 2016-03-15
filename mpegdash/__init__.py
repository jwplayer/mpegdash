# -*- coding: utf-8 -*-

from lxml import etree

from mpegdash.serialization import XMLSerializer


class DASHModel(XMLSerializer):

    PROFILE_RULES = {}

    def __init__(self, **kwargs):
        super(DASHModel, self).__init__(**kwargs)
        self._attributes = {}

    def set_attribute(self, attribute, value):
        self._attributes[attribute] = value
        self._xml_set(attribute, value)

    def to_xml(self, xml_declaration=False, encoding='UTF-8', pretty_print=False):
        if 'apply_profile_rules' in dir(self):
            self.apply_profile_rules()
        return super(DASHModel, self).to_xml(xml_declaration=True, encoding=encoding, pretty_print=pretty_print)
