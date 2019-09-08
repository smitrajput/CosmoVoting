from django.conf.urls import url, include

urlpatterns = [
    url(r'^v1/', include('polling_booth.v1.urls'), name='v1_otp'),
]
