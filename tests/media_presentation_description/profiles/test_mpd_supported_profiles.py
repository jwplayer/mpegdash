# -*- coding: utf-8 -*-

import unittest

from dashifest import MediaPresentationDescription


class MPDSupportedDASHProfilesTest(unittest.TestCase):
    """

    from http://dashif.org/identifiers/profiles/

    Profiles of DASH are defined to enable interoperability and the signaling of the use of features.
    Profiles are signaled in the @profiles parameter which may be present on different levels of the MPD.

    Such a profile can also be understood as permission for DASH clients that implement the features required by the
    profile to process the Media Presentation (MPD document and Segments).

    Available DASH profiles:

     Identifier                                   Abstract

     urn:mpeg:dash:profile:full:2011              identifier for MPEG-DASH Full profile
     urn:mpeg:dash:profile:isoff-on-demand:2011   identifier for MPEG-DASH ISO Base media file format On Demand profile
     urn:mpeg:dash:profile:isoff-live:2011        identifier for MPEG-DASH ISO Base media file format live profile
     urn:mpeg:dash:profile:isoff-main:2011        identifier for MPEG-DASH ISO Base media file format main profile
     urn:mpeg:dash:profile:mp2t-main:2011         identifier for MPEG-DASH MPEG-2 TS main profile
     urn:mpeg:dash:profile:mp2t-simple:2011       identifier for MPEG-DASH MPEG-2 TS simple profile
     urn:3GPP:PSS:profile:DASH10                  identifier for 3GP-DASH Release-10 profile

    """

    def test_required_attribute_profiles_with_degenerate_input(self):
        self.assertRaises(TypeError, MediaPresentationDescription)
        self.assertRaises(TypeError, MediaPresentationDescription, minimum_buffer_time='')
        self.assertRaises(TypeError, MediaPresentationDescription, profile='', minimum_buffer_time='')
        self.assertRaises(TypeError, MediaPresentationDescription, profile=None, minimum_buffer_time=None)
        self.assertRaises(TypeError, MediaPresentationDescription, profile='urn:mpeg:dash:profile:full:2011', minimum_buffer_time='')
        self.assertRaises(TypeError, MediaPresentationDescription, profile='urn:mpeg:dash:profile:full:2011', minimum_buffer_time=0.0)
        self.assertRaises(TypeError, MediaPresentationDescription, profile=0, minimum_buffer_time=0)
        self.assertRaises(TypeError, MediaPresentationDescription, profile=0.0, minimum_buffer_time=0)
        self.assertRaises(TypeError, MediaPresentationDescription, profile='', minimum_buffer_time=0)

    def test_supported_dash_profiles(self):
        self.assertRaises(TypeError, MediaPresentationDescription, profile='urn:mpeg:dash:profile:full:2012', minimum_buffer_time=0)
        MediaPresentationDescription(profile='urn:mpeg:dash:profile:full:2011', minimum_buffer_time=0)
        MediaPresentationDescription(profile='urn:mpeg:dash:profile:isoff-on-demand:2011', minimum_buffer_time=0)
        MediaPresentationDescription(profile='urn:mpeg:dash:profile:isoff-live:2011', minimum_buffer_time=0)
        MediaPresentationDescription(profile='urn:mpeg:dash:profile:isoff-main:2011', minimum_buffer_time=0)
        MediaPresentationDescription(profile='urn:mpeg:dash:profile:mp2t-main:2011', minimum_buffer_time=0)
        MediaPresentationDescription(profile='urn:mpeg:dash:profile:mp2t-simple:2011', minimum_buffer_time=0)
        MediaPresentationDescription(profile='urn:3GPP:PSS:profile:DASH10', minimum_buffer_time=0)
