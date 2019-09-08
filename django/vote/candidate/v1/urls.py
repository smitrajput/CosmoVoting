from django.conf.urls import url

from candidate.v1 import views

urlpatterns = [
    # url(r'^otp/send/(?P<mob_number>[0-9]+)/', views.SendOtp.as_view(),
    #     name='v1_send'),
    # url(r'^otp/verify/(?P<mob_number>[0-9]+)/(?P<otp>[0-9]+)', views.VerifyOtp.as_view(), name='v1_verify'),
    # url(r'^otp/logout/$', views.UserLogout.as_view(), name='v1_UserLogout'),
]
