import json

from django.core.serializers import serialize
from django.http import HttpResponse
from .models import *


def index(request):
    return HttpResponse("The application is functioning correctly!")


def all_parking(response):
    all_parking_data = Parking.objects.all()
    all_parking_data = serialize('geojson', all_parking_data, geometry_field='geom')
    return HttpResponse(all_parking_data, content_type='application/json')


def all_gare(response):
    all_gare_data = Gare.objects.all()
    all_gare_data = serialize('geojson', all_gare_data, geometry_field='geom')
    return HttpResponse(all_gare_data, content_type='application/json')


def all_commerce(response):
    all_commerce_data = Commerce.objects.all()
    all_commerce_data = serialize('geojson', all_commerce_data, geometry_field='geom')
    return HttpResponse(all_commerce_data, content_type='application/json')


def all_passage(response):
    all_passage_data = Passage.objects.all()
    all_passage_data = serialize('geojson', all_passage_data, geometry_field='geom')
    return HttpResponse(all_passage_data, content_type='application/json')


def all_piste(response):
    all_piste_data = Piste.objects.all()
    all_piste_data = serialize('geojson', all_piste_data, geometry_field='geom')
    return HttpResponse(all_piste_data, content_type='application/json')
