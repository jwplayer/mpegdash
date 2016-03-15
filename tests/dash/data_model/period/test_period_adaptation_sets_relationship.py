# -*- coding: utf-8 -*-

import unittest

from lxml import etree

from tests import is_instance_method
from mpegdash.period import Period
from mpegdash.adaptation_set import AdaptationSet


class PeriodAdaptationSetsRelationshipTest(unittest.TestCase):

    def setUp(self):
        self.period = Period()

    def test_period_adaptation_sets_relationship(self):
        assert is_instance_method(self.period.adaptation_sets)
        assert self.period.adaptation_sets() == []

    def test_period_add_adaptation_set_with_degenerate_input(self):
        assert is_instance_method(self.period.append_adaptation_set)
        self.assertRaises(TypeError, self.period.append_adaptation_set, None)
        self.assertRaises(TypeError, self.period.append_adaptation_set, '')
        self.assertRaises(TypeError, self.period.append_adaptation_set, 0)
        self.assertRaises(TypeError, self.period.append_adaptation_set, 0.0)

    def test_period_add_single_adaptation_Set(self):
        adaptation_set = AdaptationSet()
        self.period.append_adaptation_set(adaptation_set)
        xml = etree.fromstring(self.period.to_xml())
        assert len(xml.getchildren()) > 0
