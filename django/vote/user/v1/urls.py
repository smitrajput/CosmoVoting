from django.conf.urls import url

from user.v1 import views

urlpatterns = [
    url(r'^user/register/', views.UserRegistration.as_view(),
        name='v1_UserRegistration'),
    url(r'^user/login/', views.UserLogin.as_view(), name='v1_UserLogin'),
    url(r'^user/logout/$', views.UserLogout.as_view(), name='v1_UserLogout'),
]
