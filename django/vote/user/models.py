# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from common.models import LifeTimeTrackingModel, ActiveModel


class User(ActiveModel):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=40)
    email = models.CharField(max_length=255,
                             blank=True,
                             null=True)
    password_hash = models.CharField(max_length=20)
    secret_key = models.CharField(max_length=16)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user'

    def __unicode__(self):
        return "%s__%s__%s__%s" % (str(self.id),
                                   str(self.user_name),
                                   str(self.email),
                                   str(self.status))


class Login(LifeTimeTrackingModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    session_token = models.CharField(
        editable=False, blank=True, null=True, max_length=64)

    class Meta:
        db_table = 'user_login'

    def __unicode__(self):
        return "%s__%s" % (str(self.user), str(self.session_token))
