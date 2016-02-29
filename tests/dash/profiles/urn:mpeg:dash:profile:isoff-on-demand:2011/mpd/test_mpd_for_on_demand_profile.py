# -*- coding: utf-8 -*-

import unittest

from lxml import etree

from mpegdash.mpd import MPD


class PeriodOnDemandProfileTest(unittest.TestCase):
    """

    MPD@type shall be “static”.

    """

    def test_mpd_type_attribute(self):
        mpd = MPD(profile='urn:mpeg:dash:profile:isoff-on-demand:2011', minimum_buffer_time=1)
        xml = etree.fromstring(mpd.to_xml())
        assert 'type' in xml.attrib and xml.attrib.get('type') == 'static'
