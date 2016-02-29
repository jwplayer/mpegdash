# -*- coding: utf-8 -*-

import unittest

from mpegdash.mpd import MPD


class MPDModelTest(unittest.TestCase):

    def test_mpd_class(self):
        assert 'TAG' in dir(MPD)
        assert MPD.TAG == 'MPD'
        assert 'AVAILABLE_DASH_PROFILES' in dir(MPD)

    def test_mpd_model_constructor_with_degenerate_input(self):
        self.assertRaises(TypeError, MPD, profile='', minimum_buffer_time=1)
        self.assertRaises(TypeError, MPD, profile=u'', minimum_buffer_time=1)
        self.assertRaises(TypeError, MPD, profile=0, minimum_buffer_time=1)
        self.assertRaises(TypeError, MPD, profile=0.0, minimum_buffer_time=1)
        self.assertRaises(TypeError, MPD, profile=[], minimum_buffer_time=1)
        self.assertRaises(TypeError, MPD, profile={}, minimum_buffer_time=1)

    def test_mpd_model_properties(self):
        model = MPD(minimum_buffer_time=1)
        assert 'profile' in dir(model)
        assert 'periods' in dir(model)

    def test_mpd_model_default_profile(self):
        model = MPD(minimum_buffer_time=1)
        assert model.profile == MPD.AVAILABLE_DASH_PROFILES[0]
        model = MPD(profile=None, minimum_buffer_time=1)
        assert model.profile == MPD.AVAILABLE_DASH_PROFILES[0]
