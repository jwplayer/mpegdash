# -*- coding: utf-8 -*-

import unittest

from mpegdash.adaptation_set import AdaptationSet


class AdaptationSetModelTest(unittest.TestCase):

    def test_adaptation_set_class(self):
        assert 'TAG' in dir(AdaptationSet)
        assert AdaptationSet.TAG == 'AdaptationSet'
        assert 'AVAILABLE_DASH_PROFILES' in dir(AdaptationSet)

    def test_adaptation_set_model_constructor_with_degenerate_input(self):
        self.assertRaises(TypeError, AdaptationSet, profile='')
        self.assertRaises(TypeError, AdaptationSet, profile=u'')
        self.assertRaises(TypeError, AdaptationSet, profile=0)
        self.assertRaises(TypeError, AdaptationSet, profile=0.0)
        self.assertRaises(TypeError, AdaptationSet, profile=[])
        self.assertRaises(TypeError, AdaptationSet, profile={})

    def test_adaptation_set_model_properties(self):
        model = AdaptationSet()
        assert 'profile' in dir(model)
        assert 'period' in dir(model)

    # def test_period_model_default_profile(self):
    #     model = Period()
    #     assert model.profile == Period.AVAILABLE_DASH_PROFILES[0]
    #     model = Period(profile=None)
    #     assert model.profile == Period.AVAILABLE_DASH_PROFILES[0]
