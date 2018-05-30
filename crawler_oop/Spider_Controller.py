# -*- coding: utf-8 -*-

#from crawler_oop.UrlManager import UrlManager
from crawler_oop.HtmlDownloader import HtmlDownloader
from crawler_oop.HtmlParser import HtmlParser
from crawler_oop.MongoDBOutput import MongoDBOutput

class SpiderControl(object):
    def __init__(self):
        #self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = MongoDBOutput(db_name = 'Taifex', collection_name = 'TXO_PCR_daily')
        
    def crawler(self, root_url):
        try:
            # begin web crawler process
            content = self.downloader.download(root_url)
            result_tb = self.parser.parser(root_url, content)
            # insert data tp MongoDB
            self.output.insert_to_mongo(result_tb)
            print('Crawler successfully done.')    
        except Exception:
            print('Crawler failed.')
        
if __name__ == "__main__":
    spider = SpiderControl()
    spider.crawler("http://www.taifex.com.tw/chinese/3/PCRatio.asp")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        