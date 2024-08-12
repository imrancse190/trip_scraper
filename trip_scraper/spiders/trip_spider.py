import scrapy
import re
import json
from ..items import PropertyItem


class TripSpider(scrapy.Spider):
    name = 'trip'
    start_urls = ['https://uk.trip.com/hotels/?locale=en-GB&curr=GBP']
    custom_settings = {
        'ROBOTSTXT_OBEY': False
    }
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, dont_filter=True, meta={'dont_proxy': True})

    def parse(self, response):

        script_content = response.css('body > script:nth-child(11)::text').get()

        start_marker = 'window.IBU_HOTEL='
        end_marker = '//SET_IBU_HOTEL_END;'

        start_index = script_content.find(start_marker)
        end_index = script_content.find(end_marker)

        if start_index != -1 and end_index != -1:
            extracted_data = script_content[start_index:end_index]
            
            extracted_data=extracted_data[17:-17]
            
            # Save the extracted data to a file
            with open('script_content.json', 'w', encoding='utf-8') as file:
                file.write(extracted_data)
        else:
            self.log("Markers not found in the page content", level=scrapy.log.WARNING)


        # for property in data['properties']:
        #     item = PropertyItem()
        #     item['name'] = property['name']
        #     item['address'] = property['address']
        #     item['price'] = property['price']
        #     item['rating'] = property['rating']
        #     item['image_url'] = property['image_url']
        #     yield item
