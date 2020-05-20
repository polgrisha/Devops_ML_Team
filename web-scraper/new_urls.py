import http.client
import urllib
from typing import List

import pandas as pd
import scrapy
import scrapy.crawler as crawler
import vk
from goose3 import Goose
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from tqdm import tqdm

from metrics.preprocessor import Preprocessor

data = pd.read_csv('cleared.csv')

new_urls = pd.read_csv('all_urls.csv')
old_urls = pd.read_csv('all_urls_old.csv')

diff = []
for url in new_urls.urls.values:
    if not url in old_urls.urls.values:
        diff.append(url)

urls = pd.DataFrame(diff, columns=['urls'])
urls.to_csv('diff.csv')
