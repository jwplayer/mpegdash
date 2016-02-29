# -*- coding: utf-8 -*-

import unittest

from lxml import etree

from mpegdash.period import Period


class PeriodOnDemandProfileTest(unittest.TestCase):
    """

    neither the Period.SegmentList element nor the Period.SegmentTemplate element shall be present

    !!!!! MPD@type shall be “static”.
    !!! move to mpd

    """

    def test_period_segment_list_and_segment_template_attributes(self):
        period = Period(profile='urn:mpeg:dash:profile:isoff-on-demand:2011')
        xml = etree.fromstring(period.to_xml())
        assert xml.find('SegmentList') is None
        assert xml.find('SegmentTemplate') is None
