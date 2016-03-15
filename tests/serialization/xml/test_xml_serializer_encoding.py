# -*- coding: utf-8 -*-

import unittest

from lxml import etree

from mpegdash.serialization import XMLSerializer


class Serializable(XMLSerializer):

    TAG = 'A'


class MPDXMLSerializerEncodingTest(unittest.TestCase):

    def test_xml_serializer_default_encoding(self):
        serializable = Serializable()
        xml = etree.fromstring(serializable.to_xml())
        assert xml.getroottree().docinfo.encoding == 'UTF-8'

    def test_xml_serializer_utf8_encoding(self):
        serializable = Serializable()
        xml = etree.fromstring(serializable.to_xml(encoding='UTF-8'))
        assert xml.getroottree().docinfo.encoding == 'UTF-8'

    def test_xml_serializer_ascii_encoding(self):
        serializable = Serializable()
        xml = etree.fromstring(serializable.to_xml(xml_declaration=True, encoding='ASCII'))
        assert xml.getroottree().docinfo.encoding == 'ASCII'
        xml = etree.fromstring(serializable.to_xml(encoding='ASCII'))
        assert xml.getroottree().docinfo.encoding == 'UTF-8'

    def test_xml_serializer_invalid_encoding(self):
        serializable = Serializable()
        self.assertRaises(LookupError, serializable.to_xml, encoding='UTF-0')
#