from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from trip_scraper.spiders.trip_spider import TripSpider

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl(TripSpider)
    process.start()