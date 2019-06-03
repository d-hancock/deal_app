from django.db import models
from django.urls import reverse

import uuid as uuid_lib

from deal_app.users.models import User

"""
Portfolio model that groups related properties owned by user. 
"""


class Portfolio(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    unit_cashflow_criteria = models.IntegerField()
    uuid = models.UUIDField(  # Used by the API to look up the record
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolios:detail', kwargs={'pk': self.pk})


