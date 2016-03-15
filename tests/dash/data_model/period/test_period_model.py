# -*- coding: utf-8 -*-

import unittest

from mpegdash.period import Period


class PeriodModelTest(unittest.TestCase):

    def test_period_class(self):
        assert 'TAG' in dir(Period)
        assert Period.TAG == 'Period'
