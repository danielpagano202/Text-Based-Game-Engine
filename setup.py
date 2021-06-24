from distutils.core import setup
setup(
  name = 'textgameengine',
  packages = ['textgameengine'],
  version = '0.1',
  license='APACHE',
  description = 'A game engine made in python which uses text as its graphic interface instead of regular 2d shapes and sprites.',
  author = 'Daniel Pagano',
  author_email = 'danielpagano202@gmail.com',
  url = 'https://github.com/toasterstrudelz/Text-Based-Game-Engine',
  download_url = 'https://github.com/toasterstrudelz/Text-Based-Game-Engine/archive/refs/tags/v_0.3.tar.gz',    # I explain this later on
  keywords = ['Python', 'Text', 'Game-Engine'],
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
