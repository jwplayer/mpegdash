# -*- coding: utf-8 -*-

import unittest

from mpegdash.mpd import MPD


class MPDSupportedDASHProfilesTest(unittest.TestCase):
    """

    from http://dashif.org/identifiers/profiles/

    Profiles of DASH are defined to enable interoperability and the signaling of the use of features.
    Profiles are signaled in the @profiles parameter which may be present on different levels of the MPD.

    Such a profile can also be understood as permission for DASH clients that implement the features required by the
    profile to process the Media Presentation (MPD document and Segments).

    The available DASH profiles are from ISO/IEC 23009-1 2nd edition 2014-05-15:

    This part of ISO/IEC 23009 defines six profiles:

     Identifier                                   Abstract

     urn:mpeg:dash:profile:full:2011              identifier for MPEG-DASH Full profile
     urn:mpeg:dash:profile:isoff-on-demand:2011   identifier for MPEG-DASH ISO Base media file format On Demand profile
     urn:mpeg:dash:profile:isoff-live:2011        identifier for MPEG-DASH ISO Base media file format live profile
     urn:mpeg:dash:profile:isoff-main:2011        identifier for MPEG-DASH ISO Base media file format main profile
     urn:mpeg:dash:profile:mp2t-main:2011         identifier for MPEG-DASH MPEG-2 TS main profile
     urn:mpeg:dash:profile:mp2t-simple:2011       identifier for MPEG-DASH MPEG-2 TS simple profile

    """

    def test_mpd_model_with_degenerate_input(self):
        self.assertRaises(TypeError, MPD)
        self.assertRaises(TypeError, MPD, min_buffer_time='')
        self.assertRaises(TypeError, MPD, profiles='', min_buffer_time='')
        self.assertRaises(TypeError, MPD, profiles=None, min_buffer_time=None)
        self.assertRaises(TypeError, MPD, profiles='urn:mpeg:dash:profile:full:2011', min_buffer_time='')
        self.assertRaises(TypeError, MPD, profiles='urn:mpeg:dash:profile:full:2011', min_buffer_time=0.0)
        self.assertRaises(TypeError, MPD, profiles=0, min_buffer_time=0)
        self.assertRaises(TypeError, MPD, profiles=0.0, min_buffer_time=0)
        self.assertRaises(TypeError, MPD, profiles='', min_buffer_time=0)

    def test_mpd_model_with_supported_dash_profiles(self):
        self.assertRaises(TypeError, MPD, profiles='urn:mpeg:dash:profile:full:2012', min_buffer_time=0)
        MPD(profiles='urn:mpeg:dash:profile:isoff-on-demand:2011', min_buffer_time=0)

    def test_mped_model_with_unsupported_dash_profiles(self):
        self.assertRaises(TypeError, MPD, profiles='urn:mpeg:dash:profile:full:2011', min_buffer_time=0)
        self.assertRaises(TypeError, MPD, profiles='urn:mpeg:dash:profile:isoff-main:2011', min_buffer_time=0)
        self.assertRaises(TypeError, MPD, profiles='urn:mpeg:dash:profile:isoff-live:2011', min_buffer_time=0)
        self.assertRaises(TypeError, MPD, profiles='urn:mpeg:dash:profile:mp2t-main:2011', min_buffer_time=0)
        self.assertRaises(TypeError, MPD, profiles='urn:mpeg:dash:profile:mp2t-simple:2011', min_buffer_time=0)
        self.assertRaises(TypeError, MPD, profiles='urn:3GPP:PSS:profile:DASH10', min_buffer_time=0)
