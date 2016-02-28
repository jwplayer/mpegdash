#### Installation

```bash
pip install dashifest
```

#### Usage

```bash
from dashifest import MediaPresentationDescription

mpd = MediaPresentationDescription(profiles='urn:mpeg:dash:profile:isoff-on-demand:2011', minimum_buffer_time=1)
mpd.to_xml()
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
