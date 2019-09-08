# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from common.models import LifeTimeTrackingModel, ActiveModel


class AdminUser(ActiveModel):
    admin_user_id = models.AutoField(primary_key=True)
    admin_user_name = models.CharField(max_length=40)
    email = models.CharField(max_length=255,
                             blank=True,
                             null=True)
    password_hash = models.CharField(max_length=20)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'admin_user'

    def __unicode__(self):
        return "%s__%s__%s__%s" % (str(self.id),
                                   str(self.admin_user_name),
                                   str(self.email),
                                   str(self.status))


class AdminLogin(LifeTimeTrackingModel):
    admin_user = models.ForeignKey('admin_user.AdminUser', on_delete=models.CASCADE)
    session_token = models.CharField(
        editable=False, blank=True, null=True, max_length=64)

    class Meta:
        db_table = 'admin_user_login'

    def __unicode__(self):
        return "%s__%s" % (str(self.admin_user), str(self.session_token))


class Config(ActiveModel):

    attribute_name = models.CharField(max_length=255)
    attribute_type = models.CharField(max_length=255)
    attribute_value = models.CharField(max_length=255)

    class Meta:
        db_table = 'config'
