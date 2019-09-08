from __future__ import unicode_literals

from django.db import models

from common.models import LifeTimeTrackingModel, ActiveModel


class Otp_session(ActiveModel):
    mobile = models.IntegerField()
    session_id = models.CharField(max_length=40)
    # email = models.CharField(max_length=255,
    #                          blank=True,
    #                          null=True)
    # password_hash = models.CharField(max_length=20)
    # secret_key = models.CharField(max_length=16)
    # status = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     db_table = 'user'

    def __str__(self):
        return "%s__%s" % (str(self.mobile),
                                   str(self.session_id))

