from django.conf.urls import url, include

urlpatterns = [
    url(r'^v1/', include('candidate.v1.urls'), name='v1_candidate'),
]
