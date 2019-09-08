from __future__ import unicode_literals
from django.db import models
from common.models import LifeTimeTrackingModel, ActiveModel


class Constituency(ActiveModel):
    
    
    name = models.CharField(max_length=255,
                             blank=True,
                             null=True)
    # address = models.CharField(max_length=255,
    #                          blank=True,
    #                          null=True) 
    state = models.CharField(max_length=255,
                             blank=True,
                             null=True)                           
    # state = models.BooleanField(default=False)
    # secret_key = models.CharField(max_length=16)
    # status = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     db_table = 'user'
    def __str__(self):
        return "%s__%s" % (str(self.name),
                                   str(self.state))

    # def __unicode__(self):
    #     return "%s__%s" % (str(self.name),
    #                                str(self.state))

