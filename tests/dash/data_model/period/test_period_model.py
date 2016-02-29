# -*- coding: utf-8 -*-

import unittest

from mpegdash.period import Period


class PeriodModelTest(unittest.TestCase):

    def test_period_class(self):
        assert 'TAG' in dir(Period)
        assert Period.TAG == 'Period'
        assert 'AVAILABLE_DASH_PROFILES' in dir(Period)

    def test_period_model_constructor_with_degenerate_input(self):
        self.assertRaises(TypeError, Period, profile='')
        self.assertRaises(TypeError, Period, profile=u'')
        self.assertRaises(TypeError, Period, profile=0)
        self.assertRaises(TypeError, Period, profile=0.0)
        self.assertRaises(TypeError, Period, profile=[])
        self.assertRaises(TypeError, Period, profile={})

    def test_period_model_properties(self):
        model = Period()
        assert 'profile' in dir(model)
        assert 'mpd' in dir(model)

    def test_period_model_default_profile(self):
        model = Period()
        assert model.profile == Period.AVAILABLE_DASH_PROFILES[0]
        model = Period(profile=None)
        assert model.profile == Period.AVAILABLE_DASH_PROFILES[0]
