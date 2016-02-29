# -*- coding: utf-8 -*-

import unittest

from lxml import etree

from mpegdash.period import Period


class PeriodXMLSerializationTest(unittest.TestCase):

    def test_period_xml_serialization(self):
        period = Period()
        assert 'to_xml' in dir(period)
        assert isinstance(period.to_xml(), basestring)
        assert period.to_xml().startswith('<?xml')
        assert etree.fromstring(period.to_xml()).tag == 'Period'
