from django.conf.urls import url, include

urlpatterns = [
    url(r'^v1/', include('otp.v1.urls'), name='v1_otp'),
]
