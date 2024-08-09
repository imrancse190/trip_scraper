
BOT_NAME = "trip_scraper"

SPIDER_MODULES = ["trip_scraper.spiders"]
NEWSPIDER_MODULE = "trip_scraper.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


# Database settings
from config import Config
DATABASE_URL = Config.SQLALCHEMY_DATABASE_URI


# Proxy settings
ROTATE_PROXY_ENABLED = True
PROXY_LIST = [
    'http://196.51.200.84:8800',
    'http://196.51.202.192:8800',
    'http://196.51.200.234:8800',
    'http://196.51.202.134:8800',
    'http://196.51.202.138:8800'
]

# Enable the proxy middleware
DOWNLOADER_MIDDLEWARES = {
    'trip_scraper.middlewares.RotateProxyMiddleware': 750,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 751,
}

# Retry settings
RETRY_ENABLED = True
RETRY_TIMES = 10  # Number of retries for each request
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 408]

# Enable retry middleware
DOWNLOADER_MIDDLEWARES.update({
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
})

# Add a delay between requests
DOWNLOAD_DELAY = 2  # 2 seconds of delay