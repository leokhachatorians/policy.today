import json
import os
import requests
from django.http import HttpResponse, Http404
from django.shortcuts import (
        render, get_list_or_404, redirect,
        get_object_or_404)
from . import models, gov_track_api

def index(request, template='congress/index.html'):
    return render(request, template)

def state(request, state, template='congress/state_overview.html'):
    queryset = get_list_or_404(models.CongressPerson, state=state)
    return render(request, template, {'state':state, 'queryset':queryset})

def ajax_locate_district(request):
    try:
        key = os.environ['SUNLIGHT']
        lat = request.GET.get('lat', '')
        lon = request.GET.get('lon', '')
        r = requests.get(
            "https://congress.api.sunlightfoundation.com/districts/locate?latitude={}&longitude={}&apikey={}".format(
                lat, lon, key))
        return HttpResponse(json.dumps(r.json()['results'][0]), content_type="application/json")
    except:
        raise Http404("Mutumbo does not approve")


def my_district(request, state, district, template="congress/my_district.html"):
    senators = get_list_or_404(models.CongressPerson, state=state, title="Senator")
    rep = get_object_or_404(models.CongressPerson, state=state, district=district)
    return render(request, template, {
        "senators":senators, "rep":rep})

def voting_record(request, govtrack_id, template='congress/voting_record.html'):
    api = gov_track_api.GovTrack()
    query = api.vote_voter(limit='30', person=govtrack_id, order_by='-created')['objects']
    print(query)
    name = "{} {} {}".format(
            query[0]['person_role']['role_type_label'],
            query[0]['person']['firstname'],
            query[0]['person']['lastname'])
    return render(request, template, {'query':query, "name":name, "id":govtrack_id})
