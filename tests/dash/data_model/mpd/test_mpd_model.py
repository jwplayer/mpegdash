# -*- coding: utf-8 -*-

import unittest

from mpegdash.mpd import MPD

DASH_PROFILE = 'urn:mpeg:dash:profile:isoff-on-demand:2011'


class MPDModelTest(unittest.TestCase):

    def test_mpd_class(self):
        assert 'TAG' in dir(MPD)
        assert MPD.TAG == 'MPD'

    def test_mpd_model_constructor_with_degenerate_input(self):
        self.assertRaises(TypeError, MPD, profiles='', min_buffer_time=1)
        self.assertRaises(TypeError, MPD, profiles=u'', min_buffer_time=1)
        self.assertRaises(TypeError, MPD, profiles=0, min_buffer_time=1)
        self.assertRaises(TypeError, MPD, profiles=0.0, min_buffer_time=1)
        self.assertRaises(TypeError, MPD, profiles=[], min_buffer_time=1)
        self.assertRaises(TypeError, MPD, profiles={}, min_buffer_time=1)

    def test_mpd_model_properties(self):
        model = MPD(profiles=DASH_PROFILE, min_buffer_time=1)
        assert 'profiles' in dir(model)
        assert 'periods' in dir(model)
