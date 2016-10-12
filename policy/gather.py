import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "policy.settings")
import django
django.setup()

from congress import models

r = requests.get("https://www.govtrack.us/api/v2/role?current=true&limit=540")
for i in r.json()['objects']:
    cp = models.CongressPerson()
    cp.firstname=i['person']['firstname']
    cp.lastname=i['person']['lastname']
    cp.party=i['party']
    cp.title=i['title_long']
    cp.description=i['description']
    cp.bioguide_id=i['person']['bioguideid']
    cp.govtrack_id=i['person']['id']
    cp.cspan_id=i['person']['cspanid']
    cp.os_id=i['person']['osid']
    cp.pvs_id=i['person']['pvsid']
    cp.state=i['state']
    cp.twitter=i['person']['twitterid']
    cp.youtube=i['person']['youtubeid']
    cp.website=i['website']

    if i['title_long'] == 'Senator':
        cp.district = ''
    else:
        cp.district = i['district']

    try:
        cp.fax=i['extra']['fax']
    except Exception:
        cp.fax = ''

    try:
        cp.address=i['extra']['address']
    except Exception:
        cp.address = ''


    cp.save()

