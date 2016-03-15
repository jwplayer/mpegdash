# -*- coding: utf-8 -*-

import datetime
import unittest

from isodate import duration_isoformat
from lxml import etree

from tests import is_instance_method
from mpegdash.mpd import MPD
import mpegdash.period


class MPDPeriodsRelationshipTest(unittest.TestCase):

    def setUp(self):
        self.mpd = MPD(profiles='urn:mpeg:dash:profile:isoff-on-demand:2011', min_buffer_time=1)

    def test_mpd_periods_relationship(self):
        assert is_instance_method(self.mpd.periods)
        assert self.mpd.periods() == []

    def test_mpd_append_period_with_degenerate_input(self):
        assert is_instance_method(self.mpd.append_period)
        self.assertRaises(TypeError, self.mpd.append_period, None)
        self.assertRaises(TypeError, self.mpd.append_period, '')
        self.assertRaises(TypeError, self.mpd.append_period, 0)
        self.assertRaises(TypeError, self.mpd.append_period, 0.0)

    def test_mpd_add_single_period(self):
        period_start = 0
        period_duration = 47.175
        period = mpegdash.period.Period(id='0', start=period_start, duration=period_duration)
        self.mpd.append_period(period)
        xml = etree.fromstring(self.mpd.to_xml())
        assert len(xml.getchildren()) > 0
        period_element = xml.getchildren()[0]
        assert period_element.attrib.get('id') == '0'
        assert period_element.attrib.get('start') == duration_isoformat(datetime.timedelta(seconds=period_start))
        assert period_element.attrib.get('start') == 'P0D'  # isodate uses D by default for 0
        assert period_element.attrib.get('duration') == duration_isoformat(datetime.timedelta(seconds=period_duration))
        assert period_element.attrib.get('duration') == 'PT47.175S'
