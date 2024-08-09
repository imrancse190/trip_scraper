import scrapy
import random
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
        full_page =response.text
        

        # with open('full_page.html', 'w', encoding='utf-8') as file:
        #     file.write(full_page)

        start_marker = 'window.IBU_HOTEL='
        end_marker = '//SET_IBU_HOTEL_END;'

        start_index = full_page.find(start_marker)
        end_index = full_page.find(end_marker)

        if start_index != -1 and end_index != -1:
            extracted_data = full_page[start_index:end_index + len(end_marker)]
            self.log(f"Extracted Data: {extracted_data}")

            # Save the extracted data to a file
            with open('extracted_data.js', 'w', encoding='utf-8') as file:
                file.write(extracted_data)
        else:
            self.log("Markers not found in the page content", level=scrapy.log.WARNING)


        
  
    def parse_location(self, response):
        properties = response.css('div.hotel-item')
        for prop in properties:
            item = PropertyItem()
            item['title'] = prop.css('h3.hotel-name::text').get()
            item['rating'] = prop.css('span.score::text').get()
            item['location'] = prop.css('div.location::text').get()
            item['latitude'] = prop.css('::attr(data-lat)').get()
            item['longitude'] = prop.css('::attr(data-lng)').get()
            item['room_type'] = prop.css('div.room-type::text').get()
            item['price'] = prop.css('span.price::text').get()
            item['image_urls'] = prop.css('img.hotel-image::attr(src)').getall()
            yield item