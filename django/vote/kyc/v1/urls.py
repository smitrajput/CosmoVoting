from django.conf.urls import url

from kyc.v1 import views

urlpatterns = [
    url(r'^kyc/info/add/', views.AddKycData.as_view(),
        name='v1_kyc_add'),
    url(r'^kyc/info/list/', views.GetKycList.as_view(),
        name='v1_kyc_list'),
    url(r'^kyc/info/voter_id/', views.UpdateVoterId.as_view(),
        name='v1_kyc_info'),
    url(r'^kyc/info/verify/', views.VerifyKycData.as_view(),
        name='v1_kyc_info_verify'),
    url(r'^kyc/info/(?P<uuid>[0-9]+)/', views.GetKycData.as_view(),
        name='v1_kyc_info'),
    

    # url(r'^otp/verify/(?P<mob_number>[0-9]+)/(?P<otp>[0-9]+)', views.VerifyOtp.as_view(), name='v1_verify'),
    # url(r'^otp/logout/$', views.UserLogout.as_view(), name='v1_UserLogout'),
]
