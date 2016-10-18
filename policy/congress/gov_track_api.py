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

