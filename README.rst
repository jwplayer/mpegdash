dashifest
---------

dashifest is a simple MPEG-DASH manifest generator that uses lxml under the hood


To use, simply do::

    >>> from dashifest import MediaPresentationDescription
    >>> mpd = MediaPresentationDescription(profile='urn:mpeg:dash:profile:isoff-on-demand:2011', minimum_buffer_time=1)
    >>> print mpd.to_xml()
