from django.db import models

STATUS = (
    ('Pending','Pending'),
    ('Accepted','Accepted'),
    ('Rejected','Rejected'),
)

class Proposal(models.Model):
    title = models.TextField(max_length=255, blank=True, null=True)
    cost_pax = models.IntegerField(blank=True, null=True)
    about = models.TextField(max_length=1500, blank=True, null=True)
    status = models.TextField(choices=STATUS, default='Pending')
