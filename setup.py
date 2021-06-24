#from distutils.core import setup
from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
  name = 'textgameengine',
  version = '0.37',
  license='MIT',
  description = 'A game engine made in python which uses text as its graphic interface instead of regular 2d shapes and sprites.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Daniel Pagano',
  author_email = 'danielpagano202@gmail.com',
  url = 'https://github.com/toasterstrudelz/Text-Based-Game-Engine',
  download_url = 'https://github.com/toasterstrudelz/Text-Based-Game-Engine/archive/refs/tags/v_0.4.tar.gz',    # I explain this later on
  keywords = ['Python', 'Text', 'Game-Engine'],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)