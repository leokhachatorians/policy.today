from django.shortcuts import render, get_list_or_404, get_object_or_404
from . import models, gov_track_api

def index(request, template='congress/index.html'):
    return render(request, template)

def state(request, state, template='congress/state.html'):
    queryset = get_list_or_404(models.CongressPerson, state=state)
    return render(request, template, {'state':state, 'queryset':queryset})

def congress_person(request, govtrack_id, template='congress/person.html'):
    api = gov_track_api.GovTrack()
    query = api.vote_voter(limit='30', person=govtrack_id, order_by='-created')['objects']
    return render(request, template, {'query':query})
