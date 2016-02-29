# -*- coding: utf-8 -*-

import unittest

from mpegdash import DASHModel


class DASHModelTest(unittest.TestCase):

    def test_dash_model_class(self):
        assert 'TAG' not in dir(DASHModel)
        assert 'AVAILABLE_DASH_PROFILES' in dir(DASHModel)

    def test_dash_model_constructor_with_degenerate_args(self):
        self.assertRaises(TypeError, DASHModel, profile='')
        self.assertRaises(TypeError, DASHModel, profile=u'')
        self.assertRaises(TypeError, DASHModel, profile=0)
        self.assertRaises(TypeError, DASHModel, profile=0.0)
        self.assertRaises(TypeError, DASHModel, profile=[])
        self.assertRaises(TypeError, DASHModel, profile={})

    def test_dash_model_properties(self):
        model = DASHModel()
        assert 'profile' in dir(model)
        assert 'element' in dir(model)

    def test_dash_model_default_profile(self):
        model = DASHModel()
        assert model.profile == 'urn:mpeg:dash:profile:full:2011'

    def test_dash_model_profiles(self):
        dash_on_demand_profile = 'urn:mpeg:dash:profile:isoff-on-demand:2011'
        assert DASHModel(profile=dash_on_demand_profile).profile == dash_on_demand_profile

    def test_dash_model_lxml_representation(self):
        model = DASHModel()
        assert '__lxml__' in dir(model)
        assert model.__lxml__() is model

    def test_dash_model_str_representation(self):
        model = DASHModel()
        assert '__str__' in dir(model)
        assert 'mpegdash.DASHModel' in model.__str__()
        model.__str__(encoding='UTF-8')
        model.__str__(encoding='ASCII')
        # TODO check if there's performance impact when checking the encoding in advance
        # self.assertRaises(LookupError, model.__str__, encoding='UTF-0')
