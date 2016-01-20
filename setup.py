import os
from setuptools import setup

setup(name='attach_c',
      version='0.1',
      description='attach_c command for gdb',
      author='George Godik',
      author_email='ggodik@gmail.com',
      py_modules=['setup'],
      packages=['tests','attach_c'],
      test_suite='tests',
      install_requires=['psutil==3.0.1']
      )
