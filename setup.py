#!/usr/bin/env python

from setuptools import setup, find_packages, find_namespace_packages
import pathlib

# Dir containing this file
HERE = pathlib.Path(__file__).parent

# README
README = (HERE / "README.md").read_text()

# https://docs.python.org/3/distutils/setupscript.html#meta-data
setup(name='opencastapi',
      version='1.0.11',
      description='Provides object-oriented abstraction over the Opencast API',
      long_description=README,
      long_description_content_type='text/markdown',
      author='Jonathan L. Komar',
      author_email='komar.jonathan@gmail.com',
      license='MIT',
      classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
      ],
      url='https://github.com/metzenseifner/py_opencastapi',
      package_dir={'': 'src/main'},
      packages=find_packages(where='src/main', exclude=()),
      include_package_data=True,
      install_requires=[''],
      setup_requires=[''],
      tests_require=[''],
      #entry_points={},
      #package_data=[]
     )
