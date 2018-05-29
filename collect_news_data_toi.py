# Author : Manishanker Talusani

# Python file to collect urls and data from Times of india news paper
# !/usr/bin/python -tt
# -*- coding: utf-8 -*-

import codecs

UTF8Writer = codecs.getwriter('utf8')

import urllib2
import random

from goose import Goose
from bs4 import BeautifulSoup
from datetime import datetime, date

section_dict = {}
g = Goose()
rn = 42732  # This is the cms number for day 28-12-2016
rd = datetime(2016, 12, 28)

FREQUENCY = 100
OUTPUT_FILE = "TOI_CONTENT.txt"
OUTPUT_URL = "TOI_URLS.txt"
CITY_STRING = "http://timesofindia.indiatimes.com//city"
LOG="log_collecturls_toi.txt"

def get_urls(main_url):
    try:
        resp = urllib2.urlopen(main_url)
        html_doc = resp.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        tables = soup.find_all('table')
        with open(OUTPUT_URL, 'a') as u:
            urls = []
            temp = tables[1].find_all('a')[3:-25]
            for x in temp:
                if not x.get('href') in urls:
                    urls.append(x.get('href'))
                    if not (x.get('href') is None):
                        url = x.get('href')
                        if CITY_STRING in url:
                            u.write(url + "\n")
                            get_main_text(url)
    except:
        pass


def get_main_text(main_url):
    article = g.extract(url=main_url)
    with open(OUTPUT_FILE, 'a') as ut:
        ut = UTF8Writer(ut)
        ut.write("\n")
        ut.write('###########################################################')
        ut.write("\n")
        ut.write(article.cleaned_text)


def get_random_article(rn, rd):  # rn reference number, rd reference data in datetime format
    year = random.randint(2001, 2016)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    random_date = datetime(year, month, day)
    delta = rd - random_date
    cms_id = rn - delta.days
    return (random_date, cms_id)


def main():
    for i in range(FREQUENCY):
        (rd1, rn1) = get_random_article(rn, rd)
        #print (rd1, rn1)
        main_url = 'http://timesofindia.indiatimes.com/' + str(rd1.year) + '/' + str(rd1.month) + '/' + str(rd1.day) + '/archivelist/year-' + str(rd1.year) + ',month-' + str(rd1.month) + ',starttime-' + str(rn1) + '.cms'
        with open(LOG, 'a') as l:
            l.write(main_url + "\n")
            #print "main_url : ", main_url
        get_urls(main_url)


if __name__ == '__main__':
    main()
