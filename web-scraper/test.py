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


def get_server_status_code(url):
    host, path = urllib.parse.urlparse(url)[1:3]
    try:
        conn = http.client.HTTPConnection(host)
        conn.request('HEAD', path)
        return conn.getresponse().status
    except Exception:
        return None
 
def check_url(url):
    good_codes = [http.client.OK, http.client.FOUND, http.client.MOVED_PERMANENTLY]

    print(url)
    print(get_server_status_code(url))
    return get_server_status_code(url) in good_codes


print(urllib.parse.urlparse('http://yandex.ru'))
print(check_url('www.yandex.ru'))

data = pd.read_csv('cleared_10.csv')

# for i in range(data.shape[0]):
#     curr_row = data.iloc[i, 2:]
#     print(curr_row.values)
#     if curr_row.empty:
#         print(i)

#print(data.columns)
columns = list(data.columns[2:])
columns.remove('title')

new_data = data.dropna(how='all', subset=columns)
new_data = new_data.drop(columns = ['Unnamed: 0'])
new_data.reset_index(inplace=True, drop=True)

preprocessor = Preprocessor('default')

for i in range(new_data.shape[0]):
    new_data.loc[i, 'phone'] = preprocessor._phone_number_preproc(new_data.loc[i, 'phone'])


# print(new_data.iloc[22, :])
new_data.to_csv('cleared.csv')
