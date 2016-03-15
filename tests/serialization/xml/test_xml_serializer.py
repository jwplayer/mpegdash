# -*- coding: utf-8 -*-

import unittest
import inspect

from mpegdash.serialization import Serializer, XMLSerializer

DEFAULT_DASH_PROFILE = 'urn:mpeg:dash:profile:isoff-on-demand:2011'


class XMLSerializerTest(unittest.TestCase):

    def test_xml_serializer_class(self):
        assert issubclass(XMLSerializer, Serializer)

    def test_xml_serializer_properties(self):
        serializer = XMLSerializer()
        assert '_element' in dir(serializer)

    def test_xml_serializer_methods(self):
        serializer = XMLSerializer()
        assert '_XMLSerializer__xml_initialize_element' in dir(serializer)
        assert 'to_xml' in dir(serializer)

    def test_xml_serializer_attribute_setter(self):
        serializer = XMLSerializer()
        assert 'set' in dir(serializer)
        assert len(inspect.getargspec(serializer.set).args) == 3
        assert 'attribute' in inspect.getargspec(serializer.set).args
        assert 'value' in inspect.getargspec(serializer.set).args

        serializer.set('a', 'b')
        assert 'a' in serializer._element.attrib
        assert serializer._element.attrib['a'] == 'b'

    def test_xml_serializer_attribute_setter_with_null_value(self):
        serializer = XMLSerializer()
        serializer.set('a', 'b')
        assert 'a' in serializer._element.attrib
        assert serializer._element.attrib['a'] == 'b'
        serializer.set('a', None)
        assert 'a' not in serializer._element.attrib

    def test_xml_serializer_to_xml(self):
        serializer = XMLSerializer()
        serializer.set('a', 'b')
        xml = serializer.to_xml()
        assert xml.startswith('<?xml')
        assert xml.endswith('<root a="b"/>')

    def test_xml_serializer_to_xml_with_mpd(self):
        serializer = XMLSerializer(tag='MPD')
        serializer.set('profiles', DEFAULT_DASH_PROFILE)
        serializer.set('type', 'static')
        xml = serializer.to_xml()
        assert 'profiles="{}"'.format(DEFAULT_DASH_PROFILE) in xml
        assert 'type="static"' in xml

