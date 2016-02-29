# -*- coding: utf-8 -*-

from lxml import etree


class DASHModel(object):

    AVAILABLE_DASH_PROFILES = [
        'urn:mpeg:dash:profile:full:2011',
        'urn:mpeg:dash:profile:isoff-on-demand:2011',
        'urn:mpeg:dash:profile:isoff-live:2011',
        'urn:mpeg:dash:profile:isoff-main:2011',
        'urn:mpeg:dash:profile:mp2t-main:2011',
        'urn:mpeg:dash:profile:mp2t-simple:2011',
    ]

    PROFILE_RULES = {}

    def __init__(self, profile=None):
        if profile is not None and profile not in DASHModel.AVAILABLE_DASH_PROFILES:
            raise TypeError("DASHModel: profile '{}' is invalid".format(str(profile)))
        self.profile = profile or DASHModel.AVAILABLE_DASH_PROFILES[0]
        self.element = None

    def element(self):
        return self.__lxml__().element

    def __lxml__(self):
        """

        This function is responsible for initializing the lxml Element instance if it doesn't exist (in this case we can
        emulate a lazy loading behavior which could be beneficial in situations like map reduce.
        Any profile rules are also processed here

        @rtype: DASHModel
        @return: the instance itself

        """
        if self.element is None and 'TAG' in dir(self.__class__):
            self.element = etree.Element(self.__class__.TAG)
        [rule(self) for rule in self.__class__.PROFILE_RULES.get(None, [])]
        [rule(self) for rule in self.__class__.PROFILE_RULES.get(self.profile, [])]
        return self

    def to_xml(self, encoding='UTF-8'):
        return self.__lxml__().__str__(encoding=encoding)

    def __str__(self, encoding='UTF-8'):
        if self.element is not None:
            return etree.tostring(self.element, xml_declaration=True, encoding=encoding)
        return super(DASHModel, self).__str__()
