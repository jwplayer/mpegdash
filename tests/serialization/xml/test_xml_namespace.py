# -*- coding: utf-8 -*-

import unittest

from lxml import etree

from mpegdash.mpd import MPD

XML_SCHEMA_INSTANCE = 'http://www.w3.org/2001/XMLSchema-instance'
DEFAULT_DASH_PROFILE = 'urn:mpeg:dash:profile:isoff-on-demand:2011'
MINIMUM_BUFFER_TIME = 1


class MPDXMLNamespace(unittest.TestCase):

    def setUp(self):
        self.mpd = MPD(profiles=DEFAULT_DASH_PROFILE, min_buffer_time=MINIMUM_BUFFER_TIME)
        self.xml = etree.fromstring(str(self.mpd.to_xml()))

    def test_mpd_xml_schema_instance(self):
        assert 'xsi' in self.xml.nsmap
        assert self.xml.nsmap.get('xsi') == XML_SCHEMA_INSTANCE

    def test_mpd_xml_namespace(self):
        assert None in self.xml.nsmap
        assert self.xml.nsmap.get(None) == 'urn:mpeg:DASH:schema:MPD:2011'

        xsi_schema_location_attrib = '{{{}}}schemaLocation'.format(XML_SCHEMA_INSTANCE)
        assert xsi_schema_location_attrib in self.xml.attrib
        assert self.xml.attrib.get(xsi_schema_location_attrib) == 'urn:mpeg:DASH:schema:MPD:2011 DASH-MPD.xsd'
