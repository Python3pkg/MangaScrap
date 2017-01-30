from setuptools import setup, find_packages
from MangaScrap import __version__

setup(name='MangaScrap',
      version=__version__,
      description='A manga scrapper for mangapanda.com',
      keywords='manga scraper',
      url='https://github.com/kassuro/MangaScrap',
      license='MIT',

      author='Luca Fuhl',
      maintainer='Luca Fuhl',
      author_email='luca@fuhl.it',

      packages=find_packages(),

      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 3',
          'Topic :: Internet :: WWW/HTTP :: Indexing/Search'
      ],

      install_requires=[
          'requests',
          'beautifulsoup4'
      ],
     )
