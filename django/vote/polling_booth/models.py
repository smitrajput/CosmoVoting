from __future__ import unicode_literals
from django.db import models
from common.models import LifeTimeTrackingModel, ActiveModel
from constituency.models import Constituency

class PollingBooth(ActiveModel):
    
   
    address = models.CharField(max_length=255,
                             blank=True,
                             null=True)
    officer = models.CharField(max_length=255,
                             blank=True,
                             null=True)                         
    # age = models.IntegerField(max_length=255,
    #                          blank=True,
    #                          null=True)
    constituency = models.ForeignKey(Constituency,
                             related_name='polling_booths',
                             on_delete=models.CASCADE,
                             blank=True,
                             null=True)                          
                               
    # state = models.BooleanField(default=False)
    # secret_key = models.CharField(max_length=16)
    # status = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     db_table = 'user'


    def __str__(self):
        return "%s__%s" % (str(self.address),
                                   str(self.constituency))

