# -*- coding: utf-8 -*-

import datetime
import unittest

import isodate
from lxml import etree

from mpegdash.mpd import MPD


DASH_PROFILE = 'urn:mpeg:dash:profile:isoff-on-demand:2011'
MINIMUM_BUFFER_TIME = 1


class MPDXMLSerializationTest(unittest.TestCase):

    def setUp(self):
        self.mpd = MPD(profiles=DASH_PROFILE, min_buffer_time=MINIMUM_BUFFER_TIME)
        self.xml = etree.fromstring(str(self.mpd.to_xml()))

    def test_mpd_node_required_attributes(self):
        duration = datetime.timedelta(seconds=MINIMUM_BUFFER_TIME)
        assert self.xml.attrib.get('minBufferTime') == isodate.duration_isoformat(duration)
        assert self.xml.attrib.get('profiles') == DASH_PROFILE
