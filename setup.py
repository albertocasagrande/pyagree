#!/usr/bin/env python

from setuptools import setup, find_packages
from pyagree import __version__

with open('README.md') as f:
    long_desc = f.read()

setup(name='pyagree',
      version=__version__,
      description=('A simple Python package to compute some inter-rater ' +
                   'agreement measures.'),
      long_description=long_desc,
      long_description_content_type='text/markdown',
      keywords='inter-rater agreement measures',
      author='Alberto Casagrande',
      author_email='acasagrande@units.it',
      license='MIT License',
      url='https://github.com/albertocasagrande/pyagree',
      packages=find_packages(),
      install_requires=[
          'numpy',
      ],
      extras_require={
          'doc': ['sphinxcontrib.bibtex', 'sphinxcontrib.katex', 'numpy']
      },
      classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
      ],
      python_requires='>=3.6',
      )
