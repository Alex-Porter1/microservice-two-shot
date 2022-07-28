from django.shortcuts import render
from django.http import JsonResponse
from common.json import ModelEncoder
from .models import Hat, LocationVO
from django.views.decorators.http import require_http_methods
import json


class LocationVOListEncoder(ModelEncoder):
    model = LocationVO
    properties = ['closet_name']

class LocationVoDetailEncoder(ModelEncoder):
    model = LocationVO
    properties = ['closet_name','section_number','shelf_number']



class HatListEncoder(ModelEncoder):
    model = Hat
    properties = ["name", "location"]

    encoders = {
        "location": LocationVOListEncoder(),
    }

class HatDetailEncoder(ModelEncoder):
    model = Hat
    properties = ["name","fabric","color","url","location"]



@require_http_methods(["GET", "POST"])
def api_list_hats(request):
    if request.method == "GET":
        hats = Hat.objects.all()
        return JsonResponse(
            {"hats": hats},
            encoder=HatListEncoder,
        )

    else:
        content = json.loads(request.body)

        # Get the Location object and put it in the content dict
        try:

            location = LocationVO.objects.get(id=content["location"])
            content["location"] = location
        except LocationVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid location id"},
                status=400,
            )

        hat = Hat.objects.create(**content)
        return JsonResponse(
            hat,
            encoder=HatListEncoder,
            safe=False,
        )


@require_http_methods(["GET", "PUT", "DELETE"])
def api_show_hat(request, pk):
    if request.method == "GET":
        hat = Hat.objects.get(id=pk)
        return JsonResponse(
            hat,
            encoder=HatDetailEncoder,
            safe=False,
        )
    else:
     
        count, _ = Hat.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})

    # else:
    #     # copied from create
    #     content = json.loads(request.body)
    #     try:
    #         # new code
    #         if "hat" in content:
    #             hat = Hat.objects.get(id=content["hat"])
    #             content["hat"] = hat
    #             # new code

    #     except Hat.DoesNotExist:
    #         return JsonResponse(
    #             {"message": "Invalid location abbreviation"},
    #             status=400,
    #         )

    #     Hat.objects.filter(id=pk).update(**content)

    #     # copied from get detail
    #     hat = Hat.objects.get(id=pk)
    #     return JsonResponse(
    #         hat,
    #         encoder=HatDetailEncoder,
    #         safe=False,
    #     )