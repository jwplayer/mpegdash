#### Installation

```bash
pip install mpegdash
```

#### Usage

```bash
from mpegdash.mpd import MPD
from mpegdash.period import Period

mpd = MPD(profiles='urn:mpeg:dash:profile:isoff-on-demand:2011', min_buffer_time=1)

period = Period(id='0', start=0, duration=47.175)

mpd.append_period(period)

print mpd.to_xml()
```

```xml
<?xml version='1.0' encoding='UTF-8'?>
<MPD xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:mpeg:DASH:schema:MPD:2011"
     minBufferTime="PT1S" profiles="urn:mpeg:dash:profile:isoff-on-demand:2011"
     xsi:schemaLocation="urn:mpeg:DASH:schema:MPD:2011 DASH-MPD.xsd" type="static">
    <Period id="0" start="P0D" duration="PT47.175S"/>
</MPD>
```

#### Development

```bash
git clone git@github.com:pinge/mpegdash.git
cd mpegdash
python setup.py test
python setup.py install
```

#### Test suite

```bash
python setup.py test
```

execute tests including stdout
```bash
python setup.py test --addopts '-s'
```

execute only benchmarking tests
```bash
python setup.py test --addopts '--benchmark-only'
```

#### Benchmarks

```bash
python setup.py test --addopts './tests/benchmark/'
```

![python setup.py test --addopts './tests/benchmark/'](http://i.imgur.com/BzouoGR.png)
