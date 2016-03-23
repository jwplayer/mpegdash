# -*- coding: utf-8 -*-

from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='mpegdash',
      version='0.1.0',
      description='MPEG-DASH manifest generation and validation',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Multimedia :: Sound/Audio :: Conversion',
      ],
      keywords='dash mpeg-dash mpd manifest .mpd generator xml mpegdash',
      url='http://github.com/pinge/mpegdash',
      author='Nuno Pinge',
      author_email='nuno@pinge.org',
      license='MIT',
      packages=[
          'mpegdash'
      ],
      setup_requires=[
          'pytest-runner',
      ],
      tests_require=[
          'pytest==2.8.7',
          'pytest-benchmark==3.0.0'
      ],
      install_requires=[
          'lxml==3.5.0',
          'isodate==0.5.4'
      ],
      include_package_data=True,
      zip_safe=False)
