import json
import requests
from .models import LocationVO

def get_locations():
    url = "http://wardrobe-api:8000/api/locations/"
    response = requests.get(url)
    content = json.loads(response.content)
    for location in content["locations"]:
        LocationVO.objects.update_or_create(
           
                import_href = location['href'],
                defaults = {'closet_name' :location["closet_name"],
                'section_number':location["section_number"],
                'shelf_number' :location["shelf_number"],}
                id = location["id"]
                

        )
