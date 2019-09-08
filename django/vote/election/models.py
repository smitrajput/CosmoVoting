from __future__ import unicode_literals
from django.db import models
from common.models import LifeTimeTrackingModel, ActiveModel

class Election(ActiveModel):
    
   
    label = models.CharField(max_length=255,
                             blank=True,
                             null=True)
    start_time = models.CharField(max_length=255,
                             blank=True,
                             null=True)  
    end_time = models.CharField(max_length=255,
                             blank=True,
                             null=True)                    
    status = models.IntegerField(blank=True,
                             null=True)
                            
    def __str__(self):
        return "%s__%s__%s" % (str(self.label),
                                   str(self.start_time),
                                   str(self.end_time))

