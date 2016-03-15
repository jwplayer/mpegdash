# -*- coding: utf-8 -*-

import time
import pytest

from mpegdash.mpd import MPD
from mpegdash.period import Period

DEFAULT_DASH_PROFILE = 'urn:mpeg:dash:profile:isoff-on-demand:2011'


@pytest.mark.benchmark(
    group='MPD Generation',
    min_time=0.1,
    max_time=2,
    min_rounds=5,
    timer=time.time,
    disable_gc=True,
    warmup=False
)
def test_mpd_with_1_period(benchmark):
    @benchmark
    def result():
        mpd = MPD(profiles=DEFAULT_DASH_PROFILE, min_buffer_time=1)
        mpd.append_period(Period(start=0, duration=10))
        return mpd.to_xml()

    assert result is not None


@pytest.mark.benchmark(
    group='MPD Generation',
    min_time=0.1,
    max_time=2,
    min_rounds=5,
    timer=time.time,
    disable_gc=True,
    warmup=False
)
def test_mpd_with_10_periods(benchmark):
    @benchmark
    def result():
        mpd = MPD(profiles=DEFAULT_DASH_PROFILE, min_buffer_time=1)
        [mpd.append_period(Period(start=0, duration=10)) for _ in range(0, 10)]
        return mpd.to_xml()

    assert result is not None


@pytest.mark.benchmark(
    group='MPD Generation',
    min_time=0.1,
    max_time=2,
    min_rounds=5,
    timer=time.time,
    disable_gc=True,
    warmup=False
)
def test_mpd_with_100_periods(benchmark):
    @benchmark
    def result():
        mpd = MPD(profiles=DEFAULT_DASH_PROFILE, min_buffer_time=1)
        [mpd.append_period(Period(start=0, duration=10)) for _ in range(0, 100)]
        return mpd.to_xml()

    assert result is not None
