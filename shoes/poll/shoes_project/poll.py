import json
import requests

from shoes.api.shoes_rest.models import BinVO

def get_bins():
    url = "http://wardrobe-api:8000/api/bins/"
    response = requests.get(url)
    content = json.loads(response.content)
    for bin in content["bins"]:
        BinVO.objects.update_or_create(
           import_href=bin["href"], 
           defaults={"name": bin["closet_name"]},
           bin_number=bin["bin_number"],
           bin_size=bin["bin_size"],
           id=bin["id"],
        )