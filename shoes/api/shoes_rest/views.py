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

def api_list_binVOs(request):
    if request.method == "GET":
        binVOs = BinVO.objects.all()
        return JsonResponse(
            {"BinVOs": binVOs},
            encoder=BinVOListEncoder,
            safe=False
        )



@require_http_methods(["GET", "POST"])
def api_list_shoes(request, bin_vo_id=None):
    if request.method == "GET":
        if bin_vo_id is not None:
            shoes = Shoe.objects.filter(bin=bin_vo_id)
        else:
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
