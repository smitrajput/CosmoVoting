from django.conf.urls import url

from otp.v1 import views

urlpatterns = [
    url(r'^otp/send/uuid/(?P<uuid>[0-9]+)/', views.SendOtpUuid.as_view(),
        name='v1_send_uuid'),
    url(r'^otp/send/(?P<mob_number>[0-9]+)/', views.SendOtp.as_view(),
        name='v1_send'),
    url(r'^otp/verify/uuid/(?P<uuid>[0-9]+)/(?P<otp>[0-9]+)', views.VerifyOtpUuid.as_view(), name='v1_verify_uuid'),
    
    url(r'^otp/verify/(?P<mob_number>[0-9]+)/(?P<otp>[0-9]+)', views.VerifyOtp.as_view(), name='v1_verify'),
    # url(r'^otp/logout/$', views.UserLogout.as_view(), name='v1_UserLogout'),
]
