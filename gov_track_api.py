import requests

BASE = "http://www.govtrack.us/api/v2/"

class GovTrack(object):
    def _call(self, sub_url, **kwargs):
        r = requests.get(BASE  + sub_url, params=kwargs)
        if not r.status_code == 200:
            return r.text
        return r.json()

    def bill(self, **kwargs):
        return self._call("bill", **kwargs)

    def cosponsorship(self, **kwargs):
        return self._call("cosponsorship", **kwargs)

    def person(self, **kwargs):
        return self._call("person", **kwargs)

    def role(self, **kwargs):
        return self._call("role", **kwargs)

    def vote(self, **kwargs):
        return self._call("vote", **kwargs)

    def vote_voter(self, **kwargs):
        return self._call("vote_voter", **kwargs)


c = GovTrack()
bill = c.vote_voter(limit=441, vote=118802)

for i in bill['objects']:
    firstname = i['person']['firstname']
    lastname = i['person']['lastname']
    voted = i['option']['value']
    print("{} {} voted <{}>".format(
        firstname, lastname, voted))

bills = c.vote_voter(limit='120', person=400047, order_by='-created')

for i in bills['objects']:
    print("Voted:", i['option']['value'])
    print("Bill:",  i['vote']['question'])
    print("Bill ID:", i['vote']['id'])
    break
