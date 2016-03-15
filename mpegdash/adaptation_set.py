# -*- coding: utf-8 -*-

import mpegdash
import mpegdash.representation


class AdaptationSet(mpegdash.DASHModel):

    TAG = 'AdaptationSet'

    def __init__(self, id=None, mime_type=None, codecs=None, lang=None, bitstream_switching=None,
                 subsegment_alignment=None, subsegment_starts_with_sap=None, audio_sampling_rate=None):
        super(AdaptationSet, self).__init__()
        self.set_attribute('id', id)
        self.set_attribute('mimeType', mime_type)
        self.set_attribute('codecs', codecs)
        self.set_attribute('lang', lang)
        self.set_attribute('bitstreamSwitching', bitstream_switching)
        self.set_attribute('subsegmentAlignment', subsegment_alignment)
        self.set_attribute('subsegmentStartsWithSAP', subsegment_starts_with_sap)
        self.set_attribute('audioSamplingRate', audio_sampling_rate)
        self._representations = []

    def representations(self):
        return self._representations

    def append_representation(self, representation):
        if not isinstance(representation, mpegdash.representation.Representation):
            raise TypeError('AdaptationSet: add_representation(): invalid representation')
        self._representations.append(representation)
        self._xml_append_element(representation._xml_element)
