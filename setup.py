#!/usr/bin/env python

from setuptools import setup


setup(name='predictivo_api',
      version='0.1',
      description='Predictivo API Wrapper written in python',
      author='Nerio Rincon',
      author_email='nrincon.mr@gmail.com',
      url='https://github.com/GearPlug/predictivo_api',
      packages=['predictivo_api'],
      install_requires=[
          'requests',
      ],
      keywords='predictivo_api',
      zip_safe=False,
      license='GPL',
     )