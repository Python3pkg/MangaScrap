__author__     = "Luca Fuhl"
__copyright__  = "Copyright 2017, Luca Fuhl"
__version__    = "0.1"
__maintainer__ = "Luca Fuhl"

import Scrapper

if __name__ == '__main__':
    scrapper = Scrapper.Scrapper('http://www.mangapanda.com')
    #print(scrapper.check_new_chapters('fairy-tail'))
    scrapper.download_chapter('http://www.mangapanda.com/fairy-tail/519')