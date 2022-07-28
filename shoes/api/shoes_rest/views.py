from django.shortcuts import render
from common.json import ModelEncoder
from django.http import JsonResponse
import json
from django.views.decorators.http import require_http_methods
from .models import BinVO, Shoe


class BinVOListEncoder(ModelEncoder):
    model = BinVO
    properties = [
        "import_href",
        "closet_name",
    ]

class ShoeListEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "manufacturer",
        "name",
        "color",
        "picture_url",
    ]
    encoders = {
        "bin": BinVOListEncoder(),
    }



@require_http_methods(["GET", "POST"])
def api_list_shoes(request):
    if request.method == "GET":
        shoes = Shoe.objects.all()
        return JsonResponse(
            {"shoes": shoes},
            encoder=ShoeListEncoder,
        )
    else:
        content = json.loads(request.body)

        # Get the Location object and put it in the content dict
        try:
            bin_href = content["bin"]
            bin = BinVO.objects.get(import_href=bin_href)
            content["bin"] = bin
        except BinVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid bin id"},
                status=400,
            )

        shoes = Shoe.objects.create(**content)
        return JsonResponse(
            shoes,
            encoder=ShoeListEncoder,
            safe=False,
        )

@require_http_methods('DELETE')
def api_delete_shoes(request, pk):

    try:
        shoe = Shoe.objects.get(id=pk)
        shoe.delete()
        return JsonResponse(
            shoe,
            encoder=ShoeListEncoder,
            safe=False
        )
    except Shoe.DoesNotExist:
        return JsonResponse({'message': 'Does not exist'})
