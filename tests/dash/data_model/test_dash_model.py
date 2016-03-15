# -*- coding: utf-8 -*-

import unittest

from mpegdash import DASHModel

DEFAULT_DASH_PROFILE = 'urn:mpeg:dash:profile:isoff-on-demand:2011'


class Concrete(DASHModel):

    TAG = 'MPD'


class DASHModelTest(unittest.TestCase):

    def test_dash_model_initialization(self):
        self.assertRaises(AttributeError, DASHModel)

    def test_dash_model_properties(self):
        model = Concrete()
        assert '_attributes' in dir(model)

    def test_dash_model_methods(self):
        model = Concrete()
        assert 'set_attribute' in dir(model)

    def test_dash_model_xml_serialization(self):
        model = Concrete()
        assert 'to_xml' in dir(model)
        assert model.to_xml().startswith("<?xml ")
        assert model.to_xml().endswith("<MPD/>")
