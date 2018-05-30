# -*- coding: utf-8 -*-

import pandas as pd
from bs4 import BeautifulSoup

class HtmlParser(object):
    def parser(self, url, html_content):
        if url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, 'lxml')
        # find target table 
        tbl = soup.find('table', attrs={ 'border' : '0', 'cellspacing' : 0 })
        if tbl is None:
            return
        # find column names
        rows = tbl.find_all('tr')
        col = rows[6].find_all('th')
        col = [x.text.strip() for x in col]
        # find data values
        templist = []
        for row in rows[8:]:
            cols = row.find_all('td')
            cols = [x.text.strip() for x in cols]
            templist.append(cols)
        # insert data into a dataframe
        tempdf = pd.DataFrame(templist, columns = col)
        # convert to dictionary to save in MongoDB
        datas_dict = tempdf.to_dict(orient='records')
        return datas_dict
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        