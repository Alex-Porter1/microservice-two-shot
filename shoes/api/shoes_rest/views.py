from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import json

from common.json import ModelEncoder
from .models import Shoe, BinVO

# Create your views here.

class BinVOEncoder(ModelEncoder):
    model = BinVO
    properties = ["closet_name", "bin_number", "bin_size"]

class ShoeDetailEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "id",
        "name",
        "manufacturer",
        "model_name",
        "color",
        "picture_url",
        "bin",
    ]
    encoders = {
        "bin": BinVOEncoder(),
    }


class ShoeEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "id",
        "name",
        "manufacturer",
        "model_name",
        "color",
        "picture_url",
        "bin",
    ]
    encoders = {
        "bin": BinVOEncoder(),
    }

@require_http_methods(["GET", "POST"])
def api_shoes(request):
    if request.method == "GET":
        # show all shoes
        shoes = Shoe.objects.all()
        print("shoes all", shoes)
        print("type", type(shoes))
        return JsonResponse(
            {"shoes": shoes},
            encoder=ShoeEncoder,
        )
    else: # POST
        content = json.loads(request.body)
        print("content", content)
        try:
            if "bin" in content:
                real_bin = content["bin"]
                bin = BinVO.objects.get(import_href=real_bin)               
                content["bin"] = bin
            else:
                content["bin"] = None
        except BinVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid bin vo"},
                status=400,
            )

        shoe = Shoe.objects.create(**content)
        print("shoe object type", type(shoe))
        return JsonResponse(
            shoe,
            encoder=ShoeEncoder,
            safe=False,
        )

@require_http_methods(["DELETE", "GET", "PUT"])
def api_shoe(request, pk):
    if request.method == "DELETE":
        count, _ = Shoe.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})
    elif request.method == "GET":
        shoe = Shoe.objects.get(id=pk)
        return JsonResponse(
            shoe,
            encoder=ShoeDetailEncoder,
            safe=False,
        )
    else: # PUT
        content = json.loads(request.body)
        try:
            if "bin" in content:
                bin = BinVO.objects.get(import_href=content["bin"])
                content["bin"] = bin
        except BinVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid bin vo"},
                status=400,
            )
        Shoe.objects.filter(id=pk).update(**content)
        shoe = Shoe.objects.get(id=pk)
        return JsonResponse(
            shoe,
            encoder=ShoeDetailEncoder,
            safe=False,
        )
