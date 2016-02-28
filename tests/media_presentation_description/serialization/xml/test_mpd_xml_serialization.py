# -*- coding: utf-8 -*-

import unittest

from tests import is_instance_method
from dashifest import MediaPresentationDescription


class MPDXMLSerializationTest(unittest.TestCase):

    def setUp(self):
        self.mpd = MediaPresentationDescription(profile='urn:mpeg:dash:profile:isoff-on-demand:2011',
                                                minimum_buffer_time=1)

    def test_mpd_instance_should_have_to_xml_getter(self):
        assert 'to_xml' in dir(self.mpd)
        assert is_instance_method(self.mpd.to_xml)

    def test_mpd_xml_serialization_encoding(self):
        xml = self.mpd.to_xml()
        assert isinstance(xml, unicode)
