from django.conf.urls import url, include

urlpatterns = [
    url(r'^v1/', include('admin_user.v1.urls'), name='v1_admin_user'),
]
