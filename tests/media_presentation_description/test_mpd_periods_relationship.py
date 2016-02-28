# -*- coding: utf-8 -*-

import datetime
import unittest

from isodate import duration_isoformat
from lxml import etree

from tests import is_instance_method
from dashifest import MediaPresentationDescription, Period


class MPDPeriodsRelationshipTest(unittest.TestCase):

    def setUp(self):
        self.mpd = MediaPresentationDescription(profile='urn:mpeg:dash:profile:isoff-on-demand:2011',
                                                minimum_buffer_time=1)

    def test_mpd_periods_relationship(self):
        assert is_instance_method(self.mpd.periods)
        assert self.mpd.periods() == []

    def test_mpd_add_period_with_degenerate_input(self):
        assert is_instance_method(self.mpd.add_period)
        self.assertRaises(TypeError, self.mpd.add_period, None)
        self.assertRaises(TypeError, self.mpd.add_period, '')
        self.assertRaises(TypeError, self.mpd.add_period, 0)
        self.assertRaises(TypeError, self.mpd.add_period, 0.0)

    def test_mpd_add_single_period(self):
        period_start = 0
        period_duration = 47.175
        period = Period(period_id='0', start=period_start, duration=period_duration)
        self.mpd.add_period(period)
        xml = etree.fromstring(str(self.mpd.to_xml()))
        assert len(xml.getchildren()) > 0
        period_element = xml.getchildren()[0]
        assert period_element.attrib.get('id') == '0'
        assert period_element.attrib.get('start') == duration_isoformat(datetime.timedelta(seconds=period_start))
        assert period_element.attrib.get('start') == 'P0D'  # isodate uses D by default for 0
        assert period_element.attrib.get('duration') == duration_isoformat(datetime.timedelta(seconds=period_duration))
        assert period_element.attrib.get('duration') == 'PT47.175S'
