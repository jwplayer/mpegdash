# -*- coding: utf-8 -*-

import unittest

from lxml import etree

from mpegdash.mpd import MPD
from mpegdash.period import Period
from mpegdash.adaptation_set import AdaptationSet


class MPDXMLSerializationTest(unittest.TestCase):

    def test_mpd_xml_serialization(self):
        mpd = MPD(profiles='urn:mpeg:dash:profile:isoff-on-demand:2011', min_buffer_time=1)
        assert 'to_xml' in dir(mpd)
        assert isinstance(mpd.to_xml(), basestring)
        assert mpd.to_xml().startswith('<?xml')
        etree.fromstring(mpd.to_xml())

    def test_complete_mpd(self):
        mpd = MPD(profiles='urn:mpeg:dash:profile:isoff-on-demand:2011', min_buffer_time=1)
        period_start = 0
        period_duration = 47.175
        period = Period(id='0',
                        start=period_start,
                        duration=period_duration)
        mpd.append_period(period)
        adaptation_set = AdaptationSet()
        period.append_adaptation_set(adaptation_set)

