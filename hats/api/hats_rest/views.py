from django.shortcuts import render
from django.http import JsonResponse
from common.json import ModelEncoder
import json
from django.views.decorators.http import require_http_methods
from .models import LocationVO, Hat
# Create your views here.


class LocationVODetailEncoder(ModelEncoder):
    model = LocationVO
    properties = ["name", "import_href"]


class HatListEncoder(ModelEncoder):
    model = Hat
    properties = ["id", "name"]


class HatDetailEncoder(ModelEncoder):
    model = Hat
    properties = ["id", "name", "color", "fabric", "style", "picture_url","location"]
    encoders = {
        "location": LocationVODetailEncoder(),
    }


@require_http_methods(["GET", "POST"])
def api_list_hats(request, location_vo_id=None):
    if request.method == "GET":
        if location_vo_id is not None:
            hats = Hat.objects.filter(location=location_vo_id)
        else:
            hats = Hat.objects.all()
        return JsonResponse(
            {"hats": hats},
            encoder=HatListEncoder,
        )
    else:
        content = json.loads(request.body)
        print("CONTENT", content)
        try:
            location_href = content["location"]
            location = LocationVO.objects.get(import_href=location_href)
            content["location"] = location
        except LocationVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid LocationVO Id"},
                status=400,
            )
        
        hat = Hat.objects.create(**content)
        return JsonResponse(
            hat,
            encoder=HatDetailEncoder,
            safe=False,
        )


@require_http_methods(["GET", "PUT", "DELETE"])
def api_show_hat(request, pk):
    hat = Hat.objects.get(id=pk)
    if request.method == "GET":
        return JsonResponse(
            hat,
            encoder=HatDetailEncoder,
            safe=False,
        )
    elif request.method == "DELETE":
        count, _ = Hat.objects.filter(id=pk).delete()
        return JsonResponse({"delete": count > 0})
    else:
        content = json.loads(request.body)
        if "location" in content:
            try:
                location = LocationVO.objects.get(id=content["location"])
                content["location"] = location
            except LocationVO.DoesNotExist:
                return JsonResponse(
                    {"message": "Invalid Location Id"},
                    status=400,
                )
        
        Hat.objects.filter(id=pk).update(**content)
        return JsonResponse(
            hat,
            encoder=HatDetailEncoder,
            safe=False,
        )