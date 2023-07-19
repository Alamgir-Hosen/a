from django.shortcuts import render
from django.http import JsonResponse
from api.models import Breed
from api.serializer import BreedSerializer
def get_all_dogs(request):
    print("request method:", request.method)
    return JsonResponse({"msg": "all dogs returned"})

def get_all_breeds(request):
    breeds = Breed.objects.all()
    breeds_serializer = BreedSerializer(breeds, many=True)
    return JsonResponse(breeds_serializer)

