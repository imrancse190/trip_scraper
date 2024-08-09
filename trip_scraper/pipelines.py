import os
from sqlalchemy.orm import sessionmaker
from .models import Property, engine
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class TripScraperPipeline:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        property = Property(
            title=item['title'],
            rating=float(item['rating']) if item['rating'] else None,
            location=item['location'],
            latitude=float(item['latitude']) if item['latitude'] else None,
            longitude=float(item['longitude']) if item['longitude'] else None,
            room_type=item['room_type'],
            price=item['price'],
            image_paths=','.join(item.get('images', []))
        )
        session.add(property)
        session.commit()
        session.close()
        return item

class CustomImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x) for x in item.get(self.images_urls_field, [])]

    def file_path(self, request, response=None, info=None, *, item=None):
        return f'images/{os.path.basename(request.url)}'

    def item_completed(self, results, item, info):
        item['images'] = [x['path'] for ok, x in results if ok]
        return item