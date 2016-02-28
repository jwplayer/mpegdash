# -*- coding: utf-8 -*-

import datetime
import unittest

from isodate import duration_isoformat
from lxml import etree

from dashifest import MediaPresentationDescription


class MPDAttributesTest(unittest.TestCase):

    def test_mpd_type_attribute_for_on_demand_profile(self):
        mpd = MediaPresentationDescription(profile='urn:mpeg:dash:profile:isoff-on-demand:2011', minimum_buffer_time=1)
        xml = etree.fromstring(str(mpd.to_xml()))
        assert 'type' in xml.attrib
        assert xml.attrib.get('type') == 'static'

    def test_mpd_type_attribute_for_live_profile(self):
        mpd = MediaPresentationDescription(profile='urn:mpeg:dash:profile:isoff-live:2011', minimum_buffer_time=1)
        xml = etree.fromstring(str(mpd.to_xml()))
        assert 'type' in xml.attrib
        assert xml.attrib.get('type') == 'dynamic'

    def test_mpd_media_presentation_duration_attribute(self):
        duration = 47.175000
        mpd = MediaPresentationDescription(profile='urn:mpeg:dash:profile:isoff-on-demand:2011', minimum_buffer_time=1)
        mpd.set_duration(seconds=duration)
        xml = etree.fromstring(str(mpd.to_xml()))
        assert 'mediaPresentationDuration' in xml.attrib
        assert xml.attrib.get('mediaPresentationDuration') == duration_isoformat(datetime.timedelta(seconds=duration))
        assert xml.attrib.get('mediaPresentationDuration') == 'PT47.175S'

        duration = 90001.234
        mpd.set_duration(seconds=duration)
        xml = etree.fromstring(str(mpd.to_xml()))
        assert 'mediaPresentationDuration' in xml.attrib
        assert xml.attrib.get('mediaPresentationDuration') == duration_isoformat(datetime.timedelta(seconds=duration))
        assert xml.attrib.get('mediaPresentationDuration') == 'P1DT1H1.234S'

