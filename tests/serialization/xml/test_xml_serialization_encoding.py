# -*- coding: utf-8 -*-

import unittest

from lxml import etree

from mpegdash.mpd import MPD


class MPDXMLSerializationEncodingTest(unittest.TestCase):

    def test_default_xml_encoding(self):
        mpd = MPD(profile='urn:mpeg:dash:profile:full:2011', minimum_buffer_time=1)
        xml = etree.fromstring(mpd.to_xml())
        assert xml.getroottree().docinfo.encoding == 'UTF-8'

    def test_default_utf8_encoding(self):
        mpd = MPD(profile='urn:mpeg:dash:profile:full:2011', minimum_buffer_time=1)
        xml = etree.fromstring(mpd.to_xml(encoding='UTF-8'))
        assert xml.getroottree().docinfo.encoding == 'UTF-8'

    def test_default_ascii_encoding(self):
        mpd = MPD(profile='urn:mpeg:dash:profile:full:2011', minimum_buffer_time=1)
        xml = etree.fromstring(mpd.to_xml(encoding='ASCII'))
        assert xml.getroottree().docinfo.encoding == 'ASCII'

    def test_invalid_encoding(self):
        mpd = MPD(profile='urn:mpeg:dash:profile:full:2011', minimum_buffer_time=1)
        self.assertRaises(LookupError, mpd.to_xml, encoding='UTF-0')
