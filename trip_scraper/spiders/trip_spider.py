import scrapy
import random
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

        
        extracted_data = script_content[start_index:end_index]
        
        extracted_data=extracted_data[17:-17]
        
        # Save the extracted data to a file
        # with open('data.json', 'w', encoding='utf-8') as file:
        #     file.write(extracted_data)
        # extracted_data = extracted_data.replace("'", '"')
        new_dog_data = json.loads(extracted_data)
        extracted_data=json.dumps(extracted_data) 
        # print(extracted_data)

        data=new_dog_data.get('initData').get('htlsData')
        # print("extracted_data.htlsData ",new_dog_data.get('initData').get('htlsData'))
        all_keys = list(data.keys())
        selected_keys = random.sample(all_keys, 3)
        # print("Randomly selected keys:")
        for key in selected_keys:
            selected_city = random.choice(data[key])
            print("Data ",key,", city: ", selected_city)

        
