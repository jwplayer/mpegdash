# -*- coding: utf-8 -*-

import unittest

from mpegdash.adaptation_set import AdaptationSet


class AdaptationSetModelTest(unittest.TestCase):

    def test_adaptation_set_class(self):
        assert 'TAG' in dir(AdaptationSet)
        assert AdaptationSet.TAG == 'AdaptationSet'
