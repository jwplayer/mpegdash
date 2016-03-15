# -*- coding: utf-8 -*-

import unittest

from mpegdash.period import Period


class PeriodSpecTest(unittest.TestCase):
    """

    from ISO/IEC 23009-1:

    Overview:

    A Media Presentation consists of one or more Periods. A Period is defined by a Period element in the MPD element.

    - Each Period contains one or more Adaptation Sets as described in 5.3.3.

    - Each Period may contain one or more Subsets that restrict combination of Adaptation Sets for presentation


    supported attributes for the urn:mpeg:dash:profile:isoff-on-demand:2011 profile:

    - 'id' (Optional)

      specifies an identifier for this Period. The identifier shall be unique within the scope of the Media
      Presentation.

      If the MPD@type is "dynamic", then this attribute shall be present and shall not change in case the MPD is
      updated.

      If not present, no identifier for the Period is provided.

    - 'start' (Optional)

      if present, specifies the PeriodStart time of the Period. The PeriodStart time is used as an anchor to determine
      the MPD start time of each Media Segment as well as to determine the presentation time of each access unit in the
      Media Presentation timeline.

    - 'duration' (Optional)

      if present specifies the duration of the Period to determine the PeriodStart time of the next Period.

    """

    def test_period_spec(self):
        period = Period(id='0', start=None, duration=None)
        print period
        raise NotImplemented

