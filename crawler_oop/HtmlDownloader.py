# -*- coding: utf-8 -*-

from datetime import datetime
import requests

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        # use own user agent
        user_agent = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        headers = {'User-Agent' : user_agent}
        # input the dates on which user intend to download
        start_date_str = input('\nEnter start date (xxxx/xx/xx):')
        end_date_str = input('\nEnter end date(xxxx/xx/xx):')
        # convert string to datetime
        start_datetime = datetime.strptime(start_date_str, '%Y/%m/%d')
        end_dateime = datetime.strptime(end_date_str, '%Y/%m/%d')
        # given limitation of Taifex website
        if (end_dateime - start_datetime).days > 30:
            print('Days between cannot be greater than 30 days.')
        
        payload = {'datestart' : start_date_str, 'dateend' : end_date_str}
        r = requests.post(url, params = payload, headers = headers)
        
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None

        

        
        
    