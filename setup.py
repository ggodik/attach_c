import os
from setuptools import setup

setup(name='attach_c',
      version='0.1',
      description='attach_c command for gdb',
      author='George Godik',
      author_email='ggodik@gmail.com',
      py_modules=['choose','setup'],
      packages=['tests'],
      test_suite='tests'
      )
