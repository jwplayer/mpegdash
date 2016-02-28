#### Installation

```bash
pip install dashifest
```

#### Usage

```bash
from dashifest import MediaPresentationDescription

mpd = MediaPresentationDescription(profile='urn:mpeg:dash:profile:isoff-on-demand:2011',
                                   minimum_buffer_time=1)

print mpd.to_xml()
```

```xml
<?xml version='1.0' encoding='UTF-8'?>
<MPD xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:mpeg:DASH:schema:MPD:2011"
     minBufferTime="PT1S" profiles="urn:mpeg:dash:profile:isoff-on-demand:2011"
     xsi:schemaLocation="urn:mpeg:DASH:schema:MPD:2011 DASH-MPD.xsd" type="static"/>'
```

#### Development

```bash
git clone git@github.com:pinge/dashifest.git
cd dashifest
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
