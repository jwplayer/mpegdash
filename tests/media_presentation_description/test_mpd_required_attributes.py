# -*- coding: utf-8 -*-

import datetime
import unittest

import isodate
from lxml import etree

from dashifest import MediaPresentationDescription


DASH_PROFILE = 'urn:mpeg:dash:profile:isoff-on-demand:2011'
MINIMUM_BUFFER_TIME = 1


class MPDXMLSerializationTest(unittest.TestCase):

    def setUp(self):
        self.mpd = MediaPresentationDescription(profile=DASH_PROFILE, minimum_buffer_time=MINIMUM_BUFFER_TIME)
        self.xml = etree.fromstring(str(self.mpd.to_xml()))

    def test_mpd_node_required_attributes(self):
        duration = datetime.timedelta(seconds=MINIMUM_BUFFER_TIME)
        assert self.xml.attrib.get('minBufferTime') == isodate.duration_isoformat(duration)
        assert self.xml.attrib.get('profiles') == DASH_PROFILE
