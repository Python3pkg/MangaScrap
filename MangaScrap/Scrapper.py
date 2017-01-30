"""
    Author: Luca Fuhl <luca@fuhl.it>

"""

import shutil
import requests
import re
from bs4 import BeautifulSoup

class Scrapper:
    """
        Offers functions to scrap mangas and check for new chapters
        of mangas
    """

    def __init__(self, site_url='http://www.mangapanda.com', save_location="./mangas/"):
        """
            Create new instace of Scrapper class
        """
        self.site_url = site_url
        self.save_location = save_location

    def check_new_chapters(self, search_term):
        """
            Checks latest realeses of mangapanda for new released chapter of
            given manga to search and returns the link if found
        """

        chapter_link = ''

        parsed_html = self._get_parsed_html(self.site_url)

        for link in parsed_html.find_all('a'):
            if search_term in str(link) \
            and link.has_attr('class') \
            and link['class'][0] == 'chaptersrec':
                chapter_link = '{}{}'.format(self.site_url, link['href'])
                break
        return chapter_link

    def download_chapter(self, chapter_url):
        """
            Downloads complete chapter from given url
        """
        chapter_url = chapter_url + '/1'
        while chapter_url:
            term = re.compile(r"(\d/)([\d]{1,2})")
            match = term.findall(chapter_url)
            if match:
                file_name = match[0][1]
                file_name = '{}.jpg'.format(file_name)
                self._download_img(self._get_img_url(chapter_url), file_name)
            chapter_url = self._get_next_page(chapter_url)

    def _get_parsed_html(self, url):
        """
            return parsed html with BeautifulSoup
        """
        response = requests.get(url)
        return BeautifulSoup(response.text, 'html.parser')

    def _get_img_url(self, current_page):
        """
            return parsed html with BeautifulSoup
        """
        html = self._get_parsed_html(current_page)

        page_img = html.find('img', {'id': 'img'})
        if page_img:
            return page_img['src']

    def _download_img(self, img_url, file_name):
        """
            Downloads an image from given url and saves it on local filesystem
        """
        if not img_url or not file_name:
            raise TypeError

        response = requests.get(img_url, stream=True)
        if file_name == '.jpg':
            print("FUFUFUFFU")
            file_name = '1' + file_name
        file_name = self.save_location + file_name
        with open(file_name, 'wb') as img_file:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, img_file)

    def _get_next_page(self, current_page):
        """
            return parsed html with BeautifulSoup
        """

        html = self._get_parsed_html(current_page)
        link_tag = html.find('div', {'id': 'imgholder'}).find('a')
        next_url = '{}{}'.format(self.site_url, link_tag['href'])
        if 'fairy-tail' in next_url:
            return next_url
        else:
            return ""
