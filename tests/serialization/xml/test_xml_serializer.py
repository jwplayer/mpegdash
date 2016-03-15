# -*- coding: utf-8 -*-

import unittest
import inspect

from mpegdash.serialization import XMLSerializer


class Serializable(XMLSerializer):

    TAG = 'A'


class XMLSerializerTest(unittest.TestCase):

    def test_xml_serializer_class(self):
        assert issubclass(XMLSerializer, object)

    def test_xml_serializer_mixin(self):
        self.assertRaises(AttributeError, XMLSerializer)

    def test_xml_serializer_properties(self):
        serializable = Serializable()
        assert '_xml_element' in dir(serializable)

    def test_xml_serializer_methods(self):
        serializable = Serializable()
        assert '_xml_initialize_element' in dir(serializable)
        assert 'to_xml' in dir(serializable)

    def test_xml_serializer_attribute_setter(self):
        serializable = Serializable()
        assert '_xml_set' in dir(serializable)
        assert len(inspect.getargspec(serializable._xml_set).args) == 3
        assert 'attribute' in inspect.getargspec(serializable._xml_set).args
        assert 'value' in inspect.getargspec(serializable._xml_set).args

        serializable._xml_set('a', 'b')
        assert 'a' in serializable._xml_element.attrib
        assert serializable._xml_element.attrib['a'] == 'b'

    def test_xml_serializer_attribute_setter_with_null_value(self):
        serializable = Serializable()
        serializable._xml_set('a', 'b')
        assert 'a' in serializable._xml_element.attrib
        assert serializable._xml_element.attrib['a'] == 'b'
        serializable._xml_set('a', None)
        assert 'a' not in serializable._xml_element.attrib

    def test_xml_serializer_to_xml(self):
        serializable = Serializable()
        serializable._xml_set('a', 'b')
        xml = serializable.to_xml()
        assert xml.endswith('<A a="b"/>')
