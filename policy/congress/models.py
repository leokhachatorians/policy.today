from django.db import models

class CongressPerson(models.Model):
    firstname = models.TextField()
    lastname = models.TextField()
    party = models.TextField()
    title = models.TextField()
    description = models.TextField()

    bioguide_id = models.TextField()
    govtrack_id = models.TextField()
    cspan_id = models.TextField(null=True)
    os_id = models.TextField(null=True)
    pvs_id = models.TextField(null=True)

    address = models.TextField()
    state = models.TextField()
    district = models.TextField(null=True)
    fax = models.TextField()
    twitter = models.TextField(null=True)
    youtube = models.TextField(null=True)
    website = models.TextField(null=True)
