import json
import os
import requests
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, redirect
from . import models, gov_track_api

def index(request, template='congress/index.html'):
    return render(request, template)

def state(request, state, template='congress/state_overview.html'):
    queryset = get_list_or_404(models.CongressPerson, state=state)
    return render(request, template, {'state':state, 'queryset':queryset})

def ajax_locate_district(request):
    key = os.environ['SUNLIGHT']
    lat = request.GET.get('lat', '')
    lon = request.GET.get('lon', '')
    r = requests.get(
        "https://congress.api.sunlightfoundation.com/districts/locate?latitude={}&longitude={}&apikey={}".format(
            lat, lon, key))

    return HttpResponse(json.dumps(r.json()['results'][0]), content_type="application/json")

def my_district(request, state, district, template="congress/my_district.html"):
    return render(request)

def congress_person(request, govtrack_id, template='congress/person.html'):
    api = gov_track_api.GovTrack()
    query = api.vote_voter(limit='30', person=govtrack_id, order_by='-created')['objects']
    return render(request, template, {'query':query})
