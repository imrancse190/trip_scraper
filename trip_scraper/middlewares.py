# trip_scraper/middlewares.py

import random
from scrapy import signals

class TripScraperSpiderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        pass

    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class TripScraperDownloaderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)



# Custom Proxy Middleware
import random
from scrapy.exceptions import NotConfigured

class RotateProxyMiddleware:
    def __init__(self, proxies):
        self.proxies = proxies

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('ROTATE_PROXY_ENABLED'):
            raise NotConfigured
        
        proxies = crawler.settings.get('PROXY_LIST')
        if not proxies:
            raise NotConfigured
        
        return cls(proxies)

    def process_request(self, request, spider):
        if 'dont_proxy' in request.meta:
            return
        
        request.meta['proxy'] = random.choice(self.proxies)