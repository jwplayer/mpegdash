# -*- coding: utf-8 -*-


class DASHProfile(object):

    AVAILABLE_DASH_PROFILES = [
        'urn:mpeg:dash:profile:full:2011',
        'urn:mpeg:dash:profile:isoff-on-demand:2011',
        'urn:mpeg:dash:profile:isoff-live:2011',
        'urn:mpeg:dash:profile:isoff-main:2011',
        'urn:mpeg:dash:profile:mp2t-main:2011',
        'urn:mpeg:dash:profile:mp2t-simple:2011',
    ]

    def __init__(self, uri=None):
        if uri is None or not isinstance(uri, basestring):
            raise TypeError('DASHProfile: invalid profile uri')
        if uri not in DASHProfile.AVAILABLE_DASH_PROFILES:
            raise TypeError("DASHProfile: '{}' profile is not supported".format(uri))

    def required_attributes(self):
        raise NotImplementedError('DASHProfile: required_attributes not implemented')

    def apply_rules(self):
        raise NotImplementedError('DASHProfile: apply_rules not implemented')

