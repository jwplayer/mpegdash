# -*- coding: utf-8 -*-

import datetime
import unittest

from isodate import duration_isoformat
from lxml import etree

from mpegdash.mpd import MPD


class MPDAttributesTest(unittest.TestCase):

    def test_mpd_type_attribute_for_on_demand_profile(self):
        mpd = MPD(profiles='urn:mpeg:dash:profile:isoff-on-demand:2011', min_buffer_time=1)
        print mpd.to_xml()
        xml = etree.fromstring(mpd.to_xml())
        assert 'type' in xml.attrib
        assert xml.attrib.get('type') == 'static'

    def test_mpd_media_presentation_duration_attribute(self):
        duration = 47.175000
        mpd = MPD(profiles='urn:mpeg:dash:profile:isoff-on-demand:2011', min_buffer_time=1)
        mpd.set_attribute('mediaPresentationDuration', duration)
        xml = etree.fromstring(str(mpd.to_xml()))
        assert 'mediaPresentationDuration' in xml.attrib
        assert xml.attrib.get('mediaPresentationDuration') == duration_isoformat(datetime.timedelta(seconds=duration))
        assert xml.attrib.get('mediaPresentationDuration') == 'PT47.175S'

        duration = 90001.234
        mpd.set_attribute('mediaPresentationDuration', duration)
        xml = etree.fromstring(str(mpd.to_xml()))
        assert 'mediaPresentationDuration' in xml.attrib
        assert xml.attrib.get('mediaPresentationDuration') == duration_isoformat(datetime.timedelta(seconds=duration))
        assert xml.attrib.get('mediaPresentationDuration') == 'P1DT1H1.234S'

