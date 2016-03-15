# -*- coding: utf-8 -*-

from lxml import etree

import mpegdash


class Representation(mpegdash.DASHModel):

    TAG = 'Representation'

    # width and height are not in the spec ??
    def __init__(self, id, bandwidth, width=None, height=None):
        super(Representation, self).__init__()
        self.set_attribute('id', id)
        self.set_attribute('bandwidth', bandwidth)
        self.set_attribute('width', width)
        self.set_attribute('height', height)

    def add_segment_information(self, base_url, byte_range_index, byte_range):
        """

        Representations are assigned Segment Information through the presence of the elements BaseURL, SegmentBase,
        SegmentTemplate and/or SegmentList. The Segment Information provides information on the location, availability
        and properties of all Segments contained in one Representation. Specifically, information on the presence and
        location of Initialization, Media, Index and Bitstream Switching Segments is provided.

        Each Representation has assigned at most one Initialization Segment.

        """
        base_url_element = etree.Element('BaseURL')
        base_url_element.text = base_url
        segment_base_element = etree.Element('SegmentBase', attrib={'indexRange': byte_range_index})
        initialization_element = etree.Element('Initialization', attrib={'range': byte_range})
        segment_base_element.append(initialization_element)
        self._xml_append_element(base_url_element)
        self._xml_append_element(segment_base_element)
