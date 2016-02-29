# -*- coding: utf-8 -*-

import unittest

from lxml import etree

from mpegdash.mpd import MPD
from mpegdash.period import Period
from mpegdash.adaptation_set import AdaptationSet


class MPDXMLSerializationTest(unittest.TestCase):

    def test_mpd_xml_serialization(self):
        mpd = MPD(minimum_buffer_time=1)
        assert 'to_xml' in dir(mpd)
        assert isinstance(mpd.to_xml(), basestring)
        assert mpd.to_xml().startswith('<?xml')
        etree.fromstring(mpd.to_xml())

    def test_complete_mpd(self):
        mpd = MPD(profile='urn:mpeg:dash:profile:isoff-on-demand:2011', minimum_buffer_time=1)
        period_start = 0
        period_duration = 47.175
        period = Period(profile='urn:mpeg:dash:profile:isoff-on-demand:2011',
                        period_id='0',
                        start=period_start,
                        duration=period_duration)
        mpd.add_period(period)
        adaptation_set = AdaptationSet(profile='urn:mpeg:dash:profile:isoff-on-demand:2011')
        period.add_adaptation_set(adaptation_set)
        # print dir(adaptation_set.__lxml__().element)
        # print adaptation_set.__lxml__().element
        print mpd.to_xml()

